import random
from math import ceil
from functools import wraps


#=======================#
# Crossover decorators: #
#=======================#

def _check_weight(individual_method):
    """Checks if the weight is between 0 and 1 before running.
    Exception may occur when using ga.adapt, which will catch
    the error and try again with valid weight.
    """

    @wraps(individual_method)
    def new_method(ga, parent_1, parent_2, *, weight = individual_method.__kwdefaults__.get('weight', None)):

        if weight is None:
            individual_method(ga, parent_1, parent_2)
        elif 0 < weight < 1:
            individual_method(ga, parent_1, parent_2, weight = weight)
        else:
            raise ValueError(f"Weight must be between 0 and 1 when using {individual_method.__name__}.")

    return new_method

def _gene_by_gene(individual_method):
    """Perform crossover by making a single new chromosome by combining each gene by gene."""

    @wraps(individual_method)
    def new_method(ga, parent_1, parent_2, *, weight = individual_method.__kwdefaults__.get('weight', 'None')):

        ga.population.add_child(
            individual_method(ga, value_1, value_2)
            if weight == 'None' else
            individual_method(ga, value_1, value_2, weight = weight)
            for value_1, value_2
            in zip(parent_1.gene_value_iter, parent_2.gene_value_iter)
        )

    return new_method


#====================#
# Parent decorators: #
#====================#

def _check_selection_probability(selection_method):
    """Raises a ValueError if the selection_probability is not between 0 and 1 inclusively.
    Otherwise runs the selection method."""

    @wraps(selection_method)
    def new_method(ga):
        if 0 <= ga.selection_probability <= 1:
            selection_method(ga)
        else:
            raise ValueError("Selection probability must be between 0 and 1 to select parents.")

    return new_method


def _check_positive_fitness(selection_method):
    """Raises a ValueError if the population contains a chromosome with negative fitness.
    Otherwise runs the selection method."""

    @wraps(selection_method)
    def new_method(ga):
        if ga.get_chromosome_fitness(0) > 0 and ga.get_chromosome_fitness(-1) >= 0:
            selection_method(ga)
        else:
            raise ValueError("Converted fitness values can't have negative values or be all 0."
                             + " Consider using rank selection or stochastic selection instead.")

    return new_method

def _ensure_sorted(selection_method):
    """Sorts the population by fitness and then runs the selection method."""

    @wraps(selection_method)
    def new_method(ga):
        ga.sort_by_best_fitness()
        selection_method(ga)

    return new_method

def _compute_parent_amount(selection_method):
    """Computes the amount of parents needed to be selected,
    and passes it as another argument for the method."""

    @wraps(selection_method)
    def new_method(ga):
        parent_amount = max(2, round(len(ga.population)*ga.parent_ratio))
        selection_method(ga, parent_amount)

    return new_method


#======================#
# Mutation decorators: #
#======================#


def _check_chromosome_mutation_rate(population_method):
    """Checks if the chromosome mutation rate is a float between 0 and 1 before running."""

    @wraps(population_method)
    def new_method(ga):

        if not isinstance(ga.chromosome_mutation_rate, float):
            raise TypeError("Chromosome mutation rate must be a float.")

        elif 0 < ga.chromosome_mutation_rate < 1:
            population_method(ga)

        else:
            raise ValueError("Chromosome mutation rate must be between 0 and 1.")

    return new_method


def _check_gene_mutation_rate(individual_method):
    """Checks if the gene mutation rate is a float between 0 and 1 before running."""

    @wraps(individual_method)
    def new_method(ga, index):

        if not isinstance(ga.gene_mutation_rate, float):
            raise TypeError("Gene mutation rate must be a float.")

        elif 0 < ga.gene_mutation_rate <= 1:
            individual_method(ga, index)

        else:
            raise ValueError("Gene mutation rate must be between 0 and 1.")

    return new_method


def _reset_fitness(individual_method):
    """Resets the fitness value of the chromosome."""

    @wraps(individual_method)
    def new_method(ga, chromosome):
        chromosome.fitness = None
        individual_method(ga, chromosome)

    return new_method


def _loop_random_mutations(individual_method):
    """Runs the individual method until enough
    genes are mutated on the indexed chromosome."""

    # Change input to include the gene index being mutated.
    @wraps(individual_method)
    def new_method(ga, chromosome):

        sample_space = range(len(chromosome))
        sample_size  = ceil(len(chromosome)*ga.gene_mutation_rate)

        # Loop the individual method until enough genes are mutated.
        for index in random.sample(sample_space, sample_size):
            individual_method(ga, chromosome, index)

    return new_method


#======================#
# Survivor decorators: #
#======================#


#=========================#
# Termination decorators: #
#=========================#

def _add_by_fitness_goal(termination_method):
    """Adds termination by fitness goal to the method."""

    @wraps(termination_method)
    def new_method(ga):

        # Try to check the fitness goal
        try:

            # If minimum fitness goal reached, stop ga.
            if ga.target_fitness_type == 'min' and ga.population[0].fitness <= ga.fitness_goal:
                return False

            # If maximum fitness goal reached, stop ga.
            elif ga.target_fitness_type == 'max' and ga.population[0].fitness >= ga.fitness_goal:
                return False

        # Fitness or fitness goals are None, or Population not initialized
        except (TypeError, AttributeError):
            pass

        # Check other termination methods
        return termination_method(ga)

    return new_method


def _add_by_generation_goal(termination_method):
    """Adds termination by generation goal to the method."""

    @wraps(termination_method)
    def new_method(ga):

        # If generation goal is set, check it.
        if ga.generation_goal is not None and ga.current_generation >= ga.generation_goal:
            return False

        # Check other termination methods
        return termination_method(ga)

    return new_method


def _add_by_tolerance_goal(termination_method):
    """Adds termination by tolerance goal to the method."""

    @wraps(termination_method)
    def new_method(ga):

        # If tolerance is set, check it, if possible.
        try:
            best_fitness = ga.population[0].fitness
            threshhold_fitness = ga.population[round(ga.percent_converged*len(ga.population))].fitness
            tol = ga.tolerance_goal * (1 + abs(best_fitness))

            # Terminate if the specified amount of the population has converged to the specified tolerance
            if abs(best_fitness - threshhold_fitness) < tol:
                return False

        # Fitness or tolerance goals are None, or population is not initialized
        except (TypeError, AttributeError):
            pass

        # Check other termination methods
        return termination_method(ga)

    return new_method

