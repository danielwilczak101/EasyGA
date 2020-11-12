import random

class Mutation_Methods:

    class Population:
        """Methods for selecting chromosomes to mutate"""

        def random_selection(ga):
            """Selects random chromosomes"""
            mutation_count = 0

            # Loop until enough mutations occur
            while mutation_count < ga.population.size()*ga.chromosome_mutation_rate:

                # Loop through the population
                for index in range(ga.population.size()):

                    # Randomly apply mutations
                    if random.uniform(0, 1) < ga.chromosome_mutation_rate:
                        mutation_count += 1
                        ga.population.set_chromosome(ga.mutation_individual_impl(ga, ga.population.get_chromosome(index)), index)


        def random_selection_then_cross(ga):
            """Selects random chromosomes and self-crosses with parent"""
            mutation_count = 0

            # Loop until enough mutations occur
            while mutation_count < ga.population.size()*ga.chromosome_mutation_rate:

                # Loop through the population
                for index in range(ga.population.size()):

                    chromosome = ga.population.get_chromosome(index)

                    # Randomly apply mutations
                    if random.uniform(0, 1) < ga.chromosome_mutation_rate:
                        mutation_count += 1
                        ga.population.set_chromosome(
                            ga.crossover_individual_impl(
                                ga,
                                chromosome,
                                ga.mutation_individual_impl(ga, chromosome)
                            ),
                            index
                        )


    class Individual:
        """Methods for mutating a single chromosome"""


        def individual_genes(ga, old_chromosome):
            """Mutates a random gene in the chromosome and resets the fitness."""
            chromosome = ga.make_chromosome(old_chromosome.get_gene_list())
            mutation_count = 0

            # Loops until enough mutations occur
            while mutation_count < chromosome.size()*ga.gene_mutation_rate:
                mutation_count += 1

                # Using the chromosome_impl
                if ga.chromosome_impl != None:
                    index = random.randint(0, chromosome.size()-1)
                    chromosome.set_gene(ga.make_gene(ga.chromosome_impl()[index]), index)

                # Using the gene_impl
                elif ga.gene_impl != None:
                    index = random.randint(0, chromosome.size()-1)
                    chromosome.set_gene(ga.make_gene(ga.gene_impl()), index)

                # Exit because no gene creation method specified
                else:
                    print("You did not specify any initialization constraints.")
                    break

            return chromosome
