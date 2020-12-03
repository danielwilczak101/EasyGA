import random

def _append_to_next_population(survivor_method):
    """Appends the selected chromosomes to the next population."""

    return lambda ga:\
        ga.population.append_children(survivor_method(ga))


class Survivor_Selection:
    """Survivor selection determines which individuals should be brought to the next generation"""

    # Allowing access to decorators when importing class
    _append_to_next_population = _append_to_next_population


    @_append_to_next_population
    def fill_in_best(ga):
        """Fills in the next population with the best chromosomes from the last population"""

        needed_amount = len(ga.population) - len(ga.population.next_population)
        return ga.population[:needed_amount]


    @_append_to_next_population
    def fill_in_random(ga):
        """Fills in the next population with random chromosomes from the last population"""

        needed_amount = len(ga.population) - len(ga.population.next_population)
        return random.sample(ga.population, needed_amount)


    @_append_to_next_population
    def fill_in_parents_then_random(ga):
        """Fills in the next population with all parents followed by random chromosomes from the last population"""

        # Remove dupes from the mating pool
        mating_pool = set(ga.population.mating_pool)

        needed_amount = len(ga.population) - len(ga.population.next_population)
        parent_amount = min(needed_amount, len(mating_pool))
        random_amount = needed_amount - parent_amount

        # Only parents are used.
        if random_amount == 0:
            return ga.population.mating_pool[:parent_amount]

        # Parents need to be removed from the random sample to avoid dupes.
        else:
            return mating_pool \
                   + random.sample(
                       set(ga.population) - mating_pool,
                       random_amount
                   )
