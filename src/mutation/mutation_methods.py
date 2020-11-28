import random
from math import ceil

def check_chromosome_mutation_rate(population_method):
    """Checks if the chromosome mutation rate is a float between 0 and 1 before running."""

    def new_method(ga):

        if not isinstance(ga.chromosome_mutation_rate, float):
            raise TypeError("Chromosome mutation rate must be a float.")

        elif 0 < ga.chromosome_mutation_rate < 1:
            population_method(ga)

        else:
            raise ValueError("Chromosome mutation rate must be between 0 and 1.")

    return new_method


def check_gene_mutation_rate(individual_method):
    """Checks if the gene mutation rate is a float between 0 and 1 before running."""

    def new_method(ga, index):

        if not isinstance(ga.gene_mutation_rate, float):
            raise TypeError("Gene mutation rate must be a float.")

        elif 0 < ga.gene_mutation_rate < 1:
            individual_method(ga, index)

        else:
            raise ValueError("Gene mutation rate must be between 0 and 1.")

    return new_method


def loop_selections(population_method):
    """Runs the population method until enough chromosomes are mutated."""

    def new_method(ga):

        # Loop the population method until enough chromosomes are mutated.
        for _ in range(ceil(len(ga.population)*ga.chromosome_mutation_rate)):
            population_method(ga)

    return new_method


def loop_mutations(individual_method):
    """Runs the individual method until enough
    genes are mutated on the indexed chromosome.
    """

    # Change input from index to chromosome.
    def new_method(ga, index):

        # Loop the individual method until enough genes are mutated.
        for _ in range(ceil(len(ga.population[index])*ga.gene_mutation_rate)):
            individual_method(ga, ga.population[index])

    return new_method


class Mutation_Methods:

    # Private method decorators, see above.
    _check_chromosome_mutation_rate = check_chromosome_mutation_rate
    _check_gene_mutation_rate       = check_gene_mutation_rate
    _loop_selections = loop_selections
    _loop_mutations  = loop_mutations


    class Population:
        """Methods for selecting chromosomes to mutate"""

        @check_chromosome_mutation_rate
        @loop_selections
        def random_selection(ga):
            """Selects random chromosomes."""

            index = random.randrange(len(ga.population))
            ga.mutation_individual_impl(ga, index)


        @check_chromosome_mutation_rate
        @loop_selections
        def random_avoid_best(ga):
            """Selects random chromosomes while avoiding the best chromosomes. (Elitism)"""

            index = random.randrange(
                ceil(len(ga.population)/8),
                len(ga.population)
            )
            ga.mutation_individual_impl(ga, index)


    class Individual:
        """Methods for mutating a single chromosome."""

        @check_gene_mutation_rate
        @loop_mutations
        def individual_genes(ga, chromosome):
            """Mutates a random gene in the chromosome."""

            index = random.randrange(len(chromosome))

            # Using the chromosome_impl
            if ga.chromosome_impl is not None:
                chromosome[index] = ga.make_gene(ga.chromosome_impl()[index])

            # Using the gene_impl
            elif ga.gene_impl is not None:
                chromosome[index] = ga.make_gene(ga.gene_impl())

            # Exit because no gene creation method specified
            else:
                raise Exception("Did not specify any initialization constraints.")


        class Permutation:
            """Methods for mutating a chromosome
            by changing the order of the genes."""

            @check_gene_mutation_rate
            @loop_mutations
            def swap_genes(ga, chromosome):
                """Swaps two random genes in the chromosome."""

                # Indexes of genes to swap
                index_one = random.randrange(len(chromosome))
                index_two = random.randrange(len(chromosome))

                # Swap genes
                chromosome[index_one], chromosome[index_two] = chromosome[index_two], chromosome[index_one]
