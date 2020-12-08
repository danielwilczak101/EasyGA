import random
from math import ceil

def _check_chromosome_mutation_rate(population_method):
    """Checks if the chromosome mutation rate is a float between 0 and 1 before running."""

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

    def new_method(ga, index):

        if not isinstance(ga.gene_mutation_rate, float):
            raise TypeError("Gene mutation rate must be a float.")

        elif 0 < ga.gene_mutation_rate < 1:
            individual_method(ga, index)

        else:
            raise ValueError("Gene mutation rate must be between 0 and 1.")

    return new_method


def _reset_fitness(individual_method):
    """Resets the fitness value of the chromosome."""

    def new_method(ga, chromosome):
        chromosome.fitness = None
        individual_method(ga, chromosome)

    return new_method


def _loop_random_selections(population_method):
    """Runs the population method until enough chromosomes are mutated.
    Provides the indexes of selected chromosomes to mutate using
    random.sample to get all indexes fast.
    """

    def new_method(ga):

        sample_space = range(len(ga.population))
        sample_size  = ceil(len(ga.population)*ga.chromosome_mutation_rate)

        # Loop the population method until enough chromosomes are mutated.
        for index in random.sample(sample_space, sample_size):
            population_method(ga, index)

    return new_method


def _loop_random_mutations(individual_method):
    """Runs the individual method until enough
    genes are mutated on the indexed chromosome.
    """

    # Change input to include the gene index being mutated.
    def new_method(ga, chromosome):

        sample_space = range(len(chromosome))
        sample_size  = ceil(len(chromosome)*ga.gene_mutation_rate)

        # Loop the individual method until enough genes are mutated.
        for index in random.sample(sample_space, sample_size):
            individual_method(ga, chromosome, index)

    return new_method


class Mutation_Methods:

    _check_chromosome_mutation_rate = _check_chromosome_mutation_rate
    _check_gene_mutation_rate       = _check_gene_mutation_rate
    _reset_fitness = _reset_fitness
    _loop_random_selections = _loop_random_selections
    _loop_random_mutations  = _loop_random_mutations


    class Population:
        """Methods for selecting chromosomes to mutate"""

        @_check_chromosome_mutation_rate
        @_loop_random_selections
        def random_selection(ga, index):
            """Selects random chromosomes."""

            ga.mutation_individual_impl(ga, ga.population[index])


        @_check_chromosome_mutation_rate
        @_loop_random_selections
        def random_avoid_best(ga, index):
            """Selects random chromosomes while avoiding the best chromosomes. (Elitism)"""

            if index > ga.percent_converged*len(ga.population)*3/16:
                ga.mutation_individual_impl(ga, ga.population[index])


    class Individual:
        """Methods for mutating a single chromosome."""

        @_check_gene_mutation_rate
        @_reset_fitness
        @_loop_random_mutations
        def individual_genes(ga, chromosome, index):
            """Mutates a random gene in the chromosome."""

            # Using the chromosome_impl
            if ga.chromosome_impl is not None:
                chromosome[index] = ga.make_gene(ga.chromosome_impl()[index])

            # Using the gene_impl
            elif ga.gene_impl is not None:
                chromosome[index] = ga.make_gene(ga.gene_impl())

            # Exit because no gene creation method specified
            else:
                raise Exception("Did not specify any initialization constraints.")


        class Arithmetic:
            """Methods for mutating a chromosome
            by numerically modifying the genes."""

            @_check_gene_mutation_rate
            @_reset_fitness
            @_loop_random_mutations
            def reflect_genes(ga, chromosome, index):
                """Reflects genes against the best chromosome."""

                difference = ga.population[0][index].value - chromosome[index].value
                value = ga.population[0][index].value + 2*difference
                chromosome[index] = ga.make_gene(value)


        class Permutation:
            """Methods for mutating a chromosome
            by changing the order of the genes."""

            @_check_gene_mutation_rate
            @_reset_fitness
            @_loop_random_mutations
            def swap_genes(ga, chromosome, index):
                """Swaps two random genes in the chromosome."""

                # Indexes of genes to swap
                index_one = index
                index_two = random.randrange(len(chromosome))

                # Swap genes
                chromosome[index_one], chromosome[index_two] = chromosome[index_two], chromosome[index_one]
