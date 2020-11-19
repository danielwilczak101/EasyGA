import random
from math import ceil

class Mutation_Methods:

    class Population:
        """Methods for selecting chromosomes to mutate"""

        def random_selection(ga):
            """Selects random chromosomes"""

            # Loop until enough mutations occur
            for n in range(ceil(len(ga.population)*ga.chromosome_mutation_rate)):
                index = random.randint(0, len(ga.population)-1)
                ga.population[index] = ga.mutation_individual_impl(ga, ga.population[index])


        def random_selection_then_cross(ga):
            """Selects random chromosomes and self-crosses with parent"""

            # Loop until enough mutations occur
            for n in range(ceil(len(ga.population)*ga.chromosome_mutation_rate)):
                index = random.randint(0, len(ga.population)-1)
                chromosome = ga.population[index]

                # Cross the chromosome with its mutation
                ga.population[index] = ga.crossover_individual_impl(ga, chromosome, ga.mutation_individual_impl(ga, chromosome))


    class Individual:
        """Methods for mutating a single chromosome"""


        def individual_genes(ga, old_chromosome):
            """Mutates a random gene in the chromosome and resets the fitness."""
            chromosome = ga.make_chromosome(old_chromosome.get_gene_list())

            # Loops until enough mutations occur
            for n in range(ceil(len(chromosome)*ga.gene_mutation_rate)):
                index = random.randint(0, len(chromosome)-1)

                # Using the chromosome_impl
                if ga.chromosome_impl is not None:
                    chromosome[index] = ga.make_gene(ga.chromosome_impl()[index])

                # Using the gene_impl
                elif ga.gene_impl is not None:
                    chromosome[index] = ga.make_gene(ga.gene_impl())

                # Exit because no gene creation method specified
                else:
                    print("You did not specify any initialization constraints.")
                    break

            return chromosome


            class Permutation:
                """Methods for mutating a chromosome
                by changing the order of the genes."""

                def swap_genes(ga, old_chromosome):
                    """Mutates a random gene in the chromosome and resets the fitness."""
                    chromosome = ga.make_chromosome(old_chromosome.get_gene_list())

                    # Loops until enough mutations occur
                    for n in range(ceil(len(chromosome)*ga.gene_mutation_rate)):
                        index_one = random.randint(0, len(chromosome)-1)
                        index_two = random.randint(0, len(chromosome)-1)

                        chromosome[index_one], chromosome[index_two] = chromosome[index_two], chromosome[index_one]

                    return chromosome
