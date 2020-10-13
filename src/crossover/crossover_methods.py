import random

class Crossover_Methods:

    class Population:
        """Methods for selecting chromosomes to crossover"""

        def sequential_selection(ga):
            """Select sequential pairs from the mating pool.
            Every parent is paired with the previous parent.
            The first parent is paired with the last parent.
            """

            mating_pool = ga.population.get_mating_pool()
            return ga.make_population([ga.crossover_individual_impl(ga, mating_pool[index], mating_pool[index-1]) for index in range(len(mating_pool))])


        def random_selection(ga):
            """Select random pairs from the mating pool.
            Every parent is paired with a random parent.
            """

            mating_pool = ga.population.get_mating_pool()
            return ga.make_population([ga.crossover_individual_impl(ga, parent, random.choice(mating_pool)) for parent in mating_pool])


    class Individual:
        """Methods for crossing parents"""

        def single_point_crossover(ga, parent_one, parent_two):
            """Cross two parents by swapping genes at one random point"""

            index = random.randint(0, parent_one.size()-1)
            return ga.make_chromosome(parent_one.get_gene_list()[:index] + parent_two.get_gene_list()[index:])


        def multi_point_crossover(ga, parent_one, parent_two):
            """Cross two parents by swapping genes at multiple points"""
            pass
