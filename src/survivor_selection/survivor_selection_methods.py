import random

class Survivor_Selection:
    """Survivor selection determines which individuals should be brought to the next generation"""

    def fill_in_best(ga):
        """Fills in the next population with the best chromosomes from the last population"""

        needed_amount = ga.population.size()-len(ga.population.next_population)
        ga.population.append_children(
            ga.population.get_chromosome_list()[:needed_amount]
        )


    def fill_in_random(ga):
        """Fills in the next population with random chromosomes from the last population"""

        needed_amount = ga.population.size()-ga.population.total_children()

        ga.population.append_children([              # add in chromosomes
            random.choice(                           #     randomly
                ga.population.get_chromosome_list()  #         from the population
            )                                        # 
        for n in range(needed_amount)])              # until the next population is full


    def fill_in_parents_then_random(ga):
        """Fills in the next population with all parents followed by random chromosomes from the last population"""

        needed_amount = ga.population.size()-ga.population.total_children()
        parent_amount = max(len(ga.population.get_mating_pool()), needed_amount)
        random_amount = needed_amount - parent_amount

        ga.population.append_children(                       # add in chromosomes
            ga.population.get_mating_pool()[:parent_amount]  #     from the mating pool
        )                                                    # 

        ga.population.append_children([              # add in chromosomes
            random.choice(                           #     randomly
                ga.population.get_chromosome_list()  #         from the population
            )                                        # 
        for n in range(random_amount)])              # until the next population is full
