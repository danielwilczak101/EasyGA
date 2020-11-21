import random
from math import ceil

def loop_selections(selection_method):
    """Runs the selection method until enough chromosomes are mutated."""
    def helper(ga):
        for n in range(ceil(len(ga.population)*ga.chromosome_mutation_rate)):
              selection_method(ga)
    return helper


def loop_mutations(mutation_method):
    """Runs the mutation method until enough genes are mutated."""
    def helper(ga, old_chromosome):
        chromosome = ga.make_chromosome(old_chromosome.gene_list)

        for n in range(ceil(len(chromosome)*ga.gene_mutation_rate)):
            mutation_method(ga, chromosome)

        return chromosome
    return helper


class Mutation_Methods:

    # Private method decorators, see above.
    def __loop_selections(selection_method):
        return loop_selections(selection_method)
    def __loop_mutations(mutation_method):
        return loop_mutations(mutation_method)


    class Population:
        """Methods for selecting chromosomes to mutate"""

        @loop_selections
        def random_selection(ga):
            """Selects random chromosomes."""

            index = random.randrange(len(ga.population))
            ga.population[index] = ga.mutation_individual_impl(ga, ga.population[index])


        @loop_selections
        def random_selection_then_cross(ga):
            """Selects random chromosomes and self-crosses with parent."""

            index = random.randrange(len(ga.population))
            chromosome = ga.population[index]
            ga.population[index] = ga.crossover_individual_impl(ga, chromosome, ga.mutation_individual_impl(ga, chromosome))


    class Individual:
        """Methods for mutating a single chromosome."""

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

            @loop_mutations
            def swap_genes(ga, chromosome):
                """Swaps two random genes in the chromosome."""

                index_one = random.randrange(len(chromosome))
                index_two = random.randrange(len(chromosome))

                chromosome[index_one], chromosome[index_two] = chromosome[index_two], chromosome[index_one]
