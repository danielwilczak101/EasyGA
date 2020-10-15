import random

class Mutation_Methods:

    class Population:
        """Methods for selecting chromosomes to mutate"""

        def random_selection(ga):
            """Selects random chromosomes"""

            # Loop through the population
            for index in range(ga.population.size()):

                # Randomly apply mutations
                if random.uniform(0, 1) < ga.mutation_rate:
                    ga.population.set_chromosome(ga.mutation_individual_impl(ga, ga.population.get_chromosome(index)), index)


    class Individual:
        """Methods for mutating a single chromosome"""

        def whole_chromosome(ga, chromosome):
            """Makes a completely random chromosome filled with new genes."""

            # Using the chromosome_impl to set every index inside of the chromosome
            if ga.chromosome_impl != None:
                return ga.make_chromosome([
                           ga.make_gene(value)
                       for value in ga.chromosome_impl()])

            # Using the gene_impl
            elif ga.gene_impl != None:
                return ga.make_chromosome([
                           ga.make_gene(ga.gene_impl())
                       for j in range(chromosome.size())])

            # Exit because no gene creation method specified
            else:
                print("You did not specify any initialization constraints.")
                return None


        def single_gene(ga, chromosome):
            """Mutates a random gene in the chromosome and resets the fitness."""
            chromosome.set_fitness(None)

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

            return chromosome
