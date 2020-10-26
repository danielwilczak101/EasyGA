import random

class Crossover_Methods:

    class Population:
        """Methods for selecting chromosomes to crossover."""

        def sequential_selection(ga):
            """Select sequential pairs from the mating pool.
            Every parent is paired with the previous parent.
            The first parent is paired with the last parent.
            """

            mating_pool = ga.population.get_mating_pool()

            for index in range(len(mating_pool)):  # for each parent in the mating pool
                ga.population.add_child(           #     add a child
                    ga.crossover_individual_impl(  #         by crossing
                        ga,                        #
                        mating_pool[index],        #             the parent and
                        mating_pool[index-1]       #             the previous parent
                    )
                )


        def random_selection(ga):
            """Select random pairs from the mating pool.
            Every parent is paired with a random parent.
            """

            mating_pool = ga.population.get_mating_pool()

            for parent in mating_pool:              # for each parent in the mating pool
                ga.population.add_child(            #     add a child
                    ga.crossover_individual_impl(   #         by crossing
                        ga,                         #
                        parent,                     #             the parent and
                        random.choice(mating_pool)  #             a random parent
                    )
                )


    class Individual:
        """Methods for crossing parents."""

        def single_point(ga, parent_one, parent_two):
            """Cross two parents by swapping genes at one random point."""

            index = random.randint(0, parent_one.size()-1)
            return ga.make_chromosome(parent_one.get_gene_list()[:index] + parent_two.get_gene_list()[index:])


        def multi_point(ga, parent_one, parent_two):
            """Cross two parents by swapping genes at multiple points."""
            pass


        def uniform(ga, parent_one, parent_two):
            """Cross two parents by swapping all genes randomly."""

            return ga.make_chromosome([                 # Make a new chromosome
                       random.choice([                  #     by selecting random genes from
                           parent_one.get_gene(i),      #         each parent
                           parent_two.get_gene(i)       # 
                       ])                               # 
                   for i in range(parent_one.size())])  #     for each gene

        class Arithmetic:
            """Crossover methods for numerical genes."""

            def int_random(ga, parent_one, parent_two):
                """Cross two parents by taking a random integer value between each of the genes."""

                return ga.make_chromosome([                             # Make a new chromosome
                           ga.make_gene(                                #     filled with new genes
                               random.randint(*sorted([                 #         by choosing random integers between
                                   parent_one.get_gene(i).get_value(),  #             the parents' genes
                                   parent_two.get_gene(i).get_value()   # 
                               ])))                                     # 
                       for i in range(parent_one.size())])              #     for each gene


            def int_weighted(ga, parent_one, parent_two):
                """Cross two parents by taking a a weighted average of the genes."""

                # the percentage of genes taken from the first gene
                weight = 0.25

                return ga.make_chromosome([                                   # Make a new chromosome
                           ga.make_gene(int(                                  #     filled with new integer genes
                               weight*parent_one.get_gene(i).get_value()+     #         with weight% from parent one and
                               (1-weight)*parent_two.get_gene(i).get_value()  #         (100-weight)% from parent two
                           ))                                                 # 
                       for i in range(parent_one.size())])                    #     for each gene


            def float_random(ga, parent_one, parent_two):
                """Cross two parents by taking a random numeric value between each of the genes."""

                return ga.make_chromosome([                             # Make a new chromosome
                           ga.make_gene(                                #     filled with new genes
                               random.uniform(                          #         by taking a random float between
                                   parent_one.get_gene(i).get_value(),  #             the parents' genes
                                   parent_two.get_gene(i).get_value()   # 
                               )                                        # 
                           )                                            # 
                       for i in range(parent_one.size())])              #     for each gene


            def float_weighted(ga, parent_one, parent_two):
                """Cross two parents by taking a a weighted average of the genes."""

                # the percentage of genes taken from the first gene
                weight = 0.25

                return ga.make_chromosome([                                   # Make a new chromosome
                           ga.make_gene(                                      #     filled with new float genes
                               weight*parent_one.get_gene(i).get_value()+     #         with weight% from parent one and
                               (1-weight)*parent_two.get_gene(i).get_value()  #         (100-weight)% from parent two
                           )                                                  # 
                       for i in range(parent_one.size())])                    #     for each gene
