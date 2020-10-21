import random

class Survivor_Selection:
    """Survivor selection determines which individuals should be brought to the next generation"""

    def fill_in_best(ga):
        """Fills in the next population with the best chromosomes from the last population"""

        # add in chromosomes starting from
        # the first chromosome in the population
        # until the next population is full
        ga.population.append_children(
            ga.population.get_chromosome_list()[:ga.population.size()-len(ga.population.next_population)]
        )


    def fill_in_random(ga):
        """Fills in the next population with random chromosomes from the last population"""

        ga.population.append_children([              # add in chromosomes
            random.choice(                           #     randomly
                ga.population.get_chromosome_list()  #         from the population
            )                                        # until the next population is full
        for n in range(ga.population.size()-ga.population.total_children())])


    def fill_in_parents_then_random(ga):
        """Fills in the next population with all parents followed by random chromosomes from the last population"""

        ga.population.append_children(               # add in chromosomes
            ga.population.get_mating_pool()          #     from the mating pool
        )                                            #

        ga.population.append_children([              # add in chromosomes
            random.choice(                           #     randomly
                ga.population.get_chromosome_list()  #         from the population
            )                                        # until the next population is full
        for n in range(ga.population.size()-ga.population.total_children())])
