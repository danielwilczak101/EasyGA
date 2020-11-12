import random
from math import ceil

class Mutation_Methods:

    class Population:
        """Methods for selecting chromosomes to mutate"""

        def random_selection(ga):
            """Selects random chromosomes"""

            # Loop until enough mutations occur
            for n in range(ceil(ga.population.size()*ga.chromosome_mutation_rate)):
                index = random.randint(0, ga.population.size()-1)
                ga.population.set_chromosome(ga.mutation_individual_impl(ga, ga.population.get_chromosome(index)), index)


        def random_selection_then_cross(ga):
            """Selects random chromosomes and self-crosses with parent"""

            # Loop until enough mutations occur
            for n in range(ceil(ga.population.size()*ga.chromosome_mutation_rate)):
                index = random.randint(0, ga.population.size()-1)
                chromosome = ga.population.get_chromosome(index)

                ga.population.set_chromosome(
                    ga.crossover_individual_impl(ga, chromosome, ga.mutation_individual_impl(ga, chromosome)),
                    index
                )


    class Individual:
        """Methods for mutating a single chromosome"""


        def individual_genes(ga, old_chromosome):
            """Mutates a random gene in the chromosome and resets the fitness."""
            chromosome = ga.make_chromosome(old_chromosome.get_gene_list())

            # Loops until enough mutations occur
            for n in range(ceil(chromosome.size()*ga.gene_mutation_rate)):
                index = random.randint(0, chromosome.size()-1)

                # Using the chromosome_impl
                if ga.chromosome_impl is not None:
                    chromosome.set_gene(ga.make_gene(ga.chromosome_impl()[index]), index)

                # Using the gene_impl
                elif ga.gene_impl is not None:
                    chromosome.set_gene(ga.make_gene(ga.gene_impl()), index)

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
                    for n in range(ceil(chromosome.size()*ga.gene_mutation_rate)):
                        index_one = random.randint(0, chromosome.size()-1)
                        index_two = random.randint(0, chromosome.size()-1)

                        gene_one = chromosome.get_gene(index_one)
                        gene_two = chromosome.get_gene(index_two)

                        chromosome.set_gene(gene_one, index_two)
                        chromosome.set_gene(gene_two, index_one)

                    return chromosome
