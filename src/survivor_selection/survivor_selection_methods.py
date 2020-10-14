import random

class Survivor_Selection:
    """Survivor selection determines which individuals should be brought to the next generation"""

    def fill_in_best(ga, next_population):
        """Fills in the next population with the best chromosomes from the last population"""

        ga.population.set_chromosome_list(ga.population.get_chromosome_list()[:ga.population.size()-next_population.size()] + next_population.get_chromosome_list())


    def fill_in_random(ga, next_population):
        """Fills in the next population with random chromosomes from the last population"""

        ga.population.set_chromosome_list([
                              random.choice(ga.population.get_chromosome_list())
                          for n in range(ga.population.size()-next_population.size())]
                      + next_population.get_chromosome_list())


    def fill_in_parents_then_random(ga, next_population):
        """Fills in the next population with all parents followed by random chromosomes from the last population"""

        ga.population.set_chromosome_list([
                              random.choice(ga.population.get_chromosome_list())
                          for n in range(ga.population.size()-len(ga.population.get_mating_pool())-next_population.size())]
                      + ga.population.get_mating_pool() + next_population.get_chromosome_list())
