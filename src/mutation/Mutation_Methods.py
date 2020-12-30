from EasyGA import function_info
import random
from math import ceil


@function_info
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


@function_info
def _check_gene_mutation_rate(individual_method):
    """Checks if the gene mutation rate is a float between 0 and 1 before running."""

    def new_method(ga, index):

        if not isinstance(ga.gene_mutation_rate, float):
            raise TypeError("Gene mutation rate must be a float.")

        elif 0 < ga.gene_mutation_rate <= 1:
            individual_method(ga, index)

        else:
            raise ValueError("Gene mutation rate must be between 0 and 1.")

    return new_method


@function_info
def _reset_fitness(individual_method):
    """Resets the fitness value of the chromosome."""

    def new_method(ga, chromosome):
        chromosome.fitness = None
        individual_method(ga, chromosome)

    return new_method


@function_info
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


class Population:
    """Methods for selecting chromosomes to mutate"""

    @_check_chromosome_mutation_rate
    def random_selection(ga):
        """Selects random chromosomes."""

        sample_space = range(len(ga.population))
        sample_size  = ceil(len(ga.population)*ga.chromosome_mutation_rate)

        # Loop the individual method until enough genes are mutated.
        for index in random.sample(sample_space, sample_size):
            ga.mutation_individual_impl(ga.population[index])


    @_check_chromosome_mutation_rate
    def random_avoid_best(ga):
        """Selects random chromosomes while avoiding the best chromosomes. (Elitism)"""

        sample_space = range(ceil(ga.percent_converged*len(ga.population)*3/16), len(ga.population))
        sample_size  = ceil(ga.chromosome_mutation_rate*len(ga.population))

        for index in random.sample(sample_space, sample_size):
            ga.mutation_individual_impl(ga.population[index])


    @_check_chromosome_mutation_rate
    def best_replace_worst(ga):
        """Selects the best chromosomes, copies them, and replaces the worst chromosomes."""

        mutation_amount = ceil(ga.chromosome_mutation_rate*len(ga.population))

        for i in range(mutation_amount):
            ga.population[-i-1] = ga.make_chromosome(ga.population[i])
            ga.mutation_individual_impl(ga.population[-i-1])


class Individual:
    """Methods for mutating a single chromosome."""

    @_check_gene_mutation_rate
    @_reset_fitness
    @_loop_random_mutations
    def individual_genes(ga, chromosome, index):
        """Mutates random genes by making completely new genes."""

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
        """Methods for mutating a chromosome by numerically modifying the genes."""

        @_check_gene_mutation_rate
        @_reset_fitness
        @_loop_random_mutations
        def average(ga, chromosome, index):
            """Mutates random genes by making completely new genes
            and then averaging them with the old genes. May cause
            premature convergence. Weight is the reciprocal of the
            number of generations run."""

            weight = 1/max(1, ga.current_generation)

            # Using the chromosome_impl
            if ga.chromosome_impl is not None:
                new_value = ga.chromosome_impl()[index]

            # Using the gene_impl
            elif ga.gene_impl is not None:
                new_value = ga.gene_impl()

            # Exit because no gene creation method specified
            else:
                raise Exception("Did not specify any initialization constraints.")

            chromosome[index] = ga.make_gene((1-weight)*chromosome[index].value + weight*new_value)


        @_check_gene_mutation_rate
        @_reset_fitness
        @_loop_random_mutations
        def reflect_genes(ga, chromosome, index):
            """Reflects genes against the best chromosome.
            Requires large genetic variety to work well but
            when it does it may be very fast."""

            difference = ga.population[0][index].value - chromosome[index].value
            value = ga.population[0][index].value + 2*difference
            chromosome[index] = ga.make_gene(value)


    class Permutation:
        """Methods for mutating a chromosome by changing the order of the genes."""

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


        @_check_gene_mutation_rate
        @_reset_fitness
        def swap_segments(ga, chromosome):
            """Splits the chromosome into 3 segments and shuffle them."""

            # Chromosome too short to mutate
            if len(chromosome) < 3:
                return

            # Indexes to split the chromosome
            index_two = random.randrange(2, len(chromosome))
            index_one = random.randrange(1, index_two)

            # Extract segments and shuffle them
            segments = [chromosome[:index_one], chromosome[index_one:index_two], chromosome[index_two:]]
            random.shuffle(segments)

            # Put segments back together
            chromosome.gene_list = segments[0] + segments[1] + segments[2]
