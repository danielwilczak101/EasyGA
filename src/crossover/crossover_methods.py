import random

def append_children_from_mating_pool(crossover_method):
    def helper(ga):
        mating_pool = ga.population.mating_pool
        ga.population.append_children(
            [chromosome for chromosome in crossover_method(ga, mating_pool)]
        )
    return helper

def values_to_chromosome(crossover_method):
    def helper(ga, parent_1, parent_2):
        return ga.make_chromosome([
                   ga.make_gene(value)
               for value in crossover_method(ga, parent_1, parent_2)])
    return helper


class Crossover_Methods:

    def __append_children_from_mating_pool(crossover_method):
        return append_children_from_mating_pool(crossover_method)
    def __values_to_chromosome(crossover_method):
        return values_to_chromosome(crossover_method)


    class Population:
        """Methods for selecting chromosomes to crossover."""


        @append_children_from_mating_pool
        def sequential_selection(ga, mating_pool):
            """Select sequential pairs from the mating pool.
            Every parent is paired with the previous parent.
            The first parent is paired with the last parent.
            """

            for index in range(len(mating_pool)):    # for each parent in the mating pool
                yield ga.crossover_individual_impl(  #     apply crossover to
                          ga,                        # 
                          mating_pool[index],        #         the parent and
                          mating_pool[index-1]       #         the previous parent
                      )


        @append_children_from_mating_pool
        def random_selection(ga, mating_pool):
            """Select random pairs from the mating pool.
            Every parent is paired with a random parent.
            """

            for parent in mating_pool:                # for each parent in the mating pool
                yield ga.crossover_individual_impl(   #     apply crossover to
                          ga,                         # 
                          parent,                     #         the parent and
                          random.choice(mating_pool)  #         a random parent
                      )


    class Individual:
        """Methods for crossing parents."""


        def single_point(ga, parent_1, parent_2):
            """Cross two parents by swapping genes at one random point."""

            swap_index = random.randint(0, len(parent_1)-1)
            return ga.make_chromosome(parent_1[:swap_index] + parent_2[swap_index:])


        def multi_point(ga, parent_1, parent_2):
            """Cross two parents by swapping genes at multiple points."""
            pass


        def uniform(ga, parent_1, parent_2):
            """Cross two parents by swapping all genes randomly."""

            return ga.make_chromosome([                          # Make a new chromosome
                    random.choice([gene_1, gene_2])              # by randomly selecting genes
                for gene_1, gene_2 in zip(parent_1, parent_2)])  # from each parent


        class Arithmetic:
            """Crossover methods for numerical genes."""

            @values_to_chromosome
            def int_random(ga, parent_1, parent_2):
                """Cross two parents by taking a random integer value between each of the genes."""

                value_list_1 = parent_1.gene_value_list
                value_list_2 = parent_2.gene_value_list

                for value_1, value_2 in zip(value_list_1, value_list_2):
                    yield random.randint(*sorted([value_1, value_2]))


            @values_to_chromosome
            def int_weighted(ga, parent_1, parent_2):
                """Cross two parents by taking a a weighted average of the genes."""

                # the percentage of genes taken from the first gene
                weight = 0.25

                value_list_1 = parent_1.gene_value_list
                value_list_2 = parent_2.gene_value_list

                for value_1, value_2 in zip(value_list_1, value_list_2):
                    yield int(weight*value_1+(1-weight)*value_2)


            @values_to_chromosome
            def float_random(ga, parent_one, parent_two):
                """Cross two parents by taking a random numeric value between each of the genes."""

                value_list_1 = parent_1.gene_value_list
                value_list_2 = parent_2.gene_value_list

                for value_1, value_2 in zip(value_list_1, value_list_2):
                    yield random.uniform([value_1, value_2])


            @values_to_chromosome
            def float_weighted(ga, parent_one, parent_two):
                """Cross two parents by taking a a weighted average of the genes."""

                # the percentage of genes taken from the first gene
                weight = 0.25

                value_list_1 = parent_1.gene_value_list
                value_list_2 = parent_2.gene_value_list
                
                for value_1, value_2 in zip(value_list_1, value_list_2):
                    yield weight*value_1+(1-weight)*value_2
