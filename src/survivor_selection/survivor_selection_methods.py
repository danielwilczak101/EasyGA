import random

def append_to_next_population(survivor_method):
    """Appends the selected chromosomes to the next population."""
    return lambda ga: ga.population.append_children(survivor_method(ga))


class Survivor_Selection:
    """Survivor selection determines which individuals should be brought to the next generation"""

    # Private method decorator, see above.
    def __append_to_next_population(survivor_method):
        return append_to_next_population(survivor_method)


    @append_to_next_population
    def fill_in_best(ga):
        """Fills in the next population with the best chromosomes from the last population"""

        needed_amount = len(ga.population) - ga.population.total_children
        return ga.population[:needed_amount]


    @append_to_next_population
    def fill_in_random(ga):
        """Fills in the next population with random chromosomes from the last population"""

        needed_amount = len(ga.population) - ga.population.total_children
        return random.choices(ga.population, k=needed_amount)


    @append_to_next_population
    def fill_in_parents_then_random(ga):
        """Fills in the next population with all parents followed by random chromosomes from the last population"""

        needed_amount = len(ga.population) - ga.population.total_children
        parent_amount = min(ga.population.total_parents, needed_amount)
        random_amount = needed_amount - parent_amount

        return ga.population.get_mating_pool()[:parent_amount] + random.choices(ga.population, k=random_amount)
