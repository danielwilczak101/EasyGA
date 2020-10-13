import random
from initialization.chromosome_structure.chromosome import Chromosome
from initialization.population_structure.population import Population

class Crossover_Methods:

    class Population:
        """Methods for selecting chromosomes to crossover"""

        def sequential_selection(ga):
            """Select sequential pairs from the mating pool"""

            mating_pool = ga.population.mating_pool
            return Population([ga.crossover_individual_impl(mating_pool[index], mating_pool[index+1]) for index in range(len(mating_pool)-1)])


        def random_selection(ga):
            """Select random pairs from the mating pool"""

            mating_pool = ga.population.mating_pool
            return Population([ga.crossover_individual_impl(random.choice(mating_pool), random.choice(mating_pool)) for n in mating_pool])


    class Individual:
        """Methods for crossing parents"""

        def single_point_crossover(parent_one, parent_two):
            """Cross two parents by swapping genes at one random point"""

            index = random.randint(0, parent_one.size()-1)
            return Chromosome(parent_one.get_gene_list()[:index] + parent_two.get_gene_list()[index:])


        def multi_point_crossover(parent_one, parent_two):
            """Cross two parents by swapping genes at multiple points"""
            pass
