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

        def single_point(ga, parent_one, parent_two):
            """Cross two parents by swapping genes at one random point"""

            index = random.randint(0, parent_one.size()-1)
            return ga.make_chromosome(parent_one.get_gene_list()[:index] + parent_two.get_gene_list()[index:])


        def multi_point(ga, parent_one, parent_two):
            """Cross two parents by swapping genes at multiple points"""
            pass


        def uniform(ga, parent_one, parent_two):
            """Cross two parents by swapping all genes randomly"""
            return ga.make_chromosome([
                       random.choice([parent_one.get_gene(i), parent_two.get_gene(i)])
                   for i in range(parent_one.size())])

        class Arithmetic:
            """Crossover methods for numerical genes"""

            def int_random(ga, parent_one, parent_two):
                """Cross two parents by taking a random integer value between each of the genes"""
                return ga.make_chromosome([
                           ga.make_gene(random.randint(*sorted([parent_one.get_gene(i).get_value(), parent_two.get_gene(i).get_value()])))
                       for i in range(parent_one.size())])


            def int_weighted(ga, parent_one, parent_two):
                """Cross two parents by taking a a weighted average of the genes"""

                # the percentage of genes taken from the first gene
                weight = 0.25
                return ga.make_chromosome([
                           ga.make_gene(int(weight*parent_one.get_gene(i).get_value()+(1-weight)*parent_two.get_gene(i).get_value()))
                       for i in range(parent_one.size())])


            def float_random(ga, parent_one, parent_two):
                """Cross two parents by taking a random numeric value between each of the genes"""
                return ga.make_chromosome([
                           ga.make_gene(random.uniform(parent_one.get_gene(i).get_value(), parent_two.get_gene(i).get_value()))
                       for i in range(parent_one.size())])


            def float_weighted(ga, parent_one, parent_two):
                """Cross two parents by taking a a weighted average of the genes"""

                # the percentage of genes taken from the first gene
                weight = 0.25
                return ga.make_chromosome([
                           ga.make_gene(weight*parent_one.get_gene(i).get_value()+(1-weight)*parent_two.get_gene(i).get_value())
                       for i in range(parent_one.size())])
