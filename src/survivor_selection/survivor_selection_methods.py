import random

class Survivor_Selection:
    """Survivor selection determines which individuals should be brought to the next generation"""

    def fill_in_best(ga, next_population):
        """Fills in the next population with the best chromosomes from the last population until the population size is met."""
        return ga.make_population(ga.population.get_all_chromosomes()[:ga.population.size()-next_population.size()] + next_population.get_all_chromosomes())
