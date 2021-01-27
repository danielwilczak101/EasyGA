import random

# Import all survivor decorators
from decorators import *


def fill_in_best(ga):
    """Fills in the next population with the best chromosomes from the last population"""

    needed_amount = len(ga.population) - len(ga.population.next_population)
    ga.population.append_children(ga.population[:needed_amount])


def fill_in_random(ga):
    """Fills in the next population with random chromosomes from the last population"""

    needed_amount = len(ga.population) - len(ga.population.next_population)
    ga.population.append_children(random.sample(ga.population, needed_amount))


def fill_in_parents_then_random(ga):
    """Fills in the next population with all parents followed by random chromosomes from the last population"""

    # Remove dupes from the mating pool
    mating_pool = set(ga.population.mating_pool)

    needed_amount = len(ga.population) - len(ga.population.next_population)
    parent_amount = min(needed_amount, len(mating_pool))
    random_amount = needed_amount - parent_amount

    # Only parents are used.
    if random_amount == 0:
        ga.population.append_children(
            chromosome
            for i, chromosome
            in enumerate(mating_pool)
            if i < parent_amount
        )

    # Parents need to be removed from the random sample to avoid dupes.
    else:
        ga.population.append_children(mating_pool)
        ga.population.append_children(
               random.sample(
                  set(ga.population) - mating_pool,
                  random_amount
              )
        )
