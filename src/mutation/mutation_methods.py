import random
from math import ceil

class Mutation_Methods:

    class Population:
        """Methods for selecting chromosomes to mutate"""

        def __loop_selections(selection_method):
            def helper(ga):
                # Loop until enough mutations occur
                for n in range(ceil(len(ga.population)*ga.chromosome_mutation_rate)):
                    selection_method(ga)
            return helper


        @__loop_selections
        def random_selection(ga):
            """Selects random chromosomes"""

            index = random.randint(0, len(ga.population)-1)
            ga.population[index] = ga.mutation_individual_impl(ga, ga.population[index])


        @__loop_selections
        def random_selection_then_cross(ga):
            """Selects random chromosomes and self-crosses with parent"""

            index = random.randint(0, len(ga.population)-1)
            chromosome = ga.population[index]
            ga.population[index] = ga.crossover_individual_impl(ga, chromosome, ga.mutation_individual_impl(ga, chromosome))


    class Individual:
        """Methods for mutating a single chromosome"""

        def __loop_mutations(mutation_method):
            def helper(ga, old_chromosome):
                chromosome = ga.make_chromosome(list(old_chromosome))

                # Loops until enough mutations occur
                for n in range(ceil(len(chromosome)*ga.gene_mutation_rate)):
                    mutation_method(ga, chromosome)

                return chromosome
            return helper


        @__loop_mutations
        def individual_genes(ga, chromosome):
            """Mutates a random gene in the chromosome and resets the fitness."""
            index = random.randint(0, len(chromosome)-1)

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

                @Individual._Individual__loop_mutations
                def swap_genes(ga, chromosome):
                    """Mutates a random gene in the chromosome and resets the fitness."""

                    index_one = random.randint(0, len(chromosome)-1)
                    index_two = random.randint(0, len(chromosome)-1)

                    chromosome[index_one], chromosome[index_two] = chromosome[index_two], chromosome[index_one]
