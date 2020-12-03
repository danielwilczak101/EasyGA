import random

def _check_selection_probability(selection_method):
    """Raises an exception if the selection_probability
    is not between 0 and 1. Otherwise runs the selection
    method.
    """

    def new_method(ga):
        if 0 < ga.selection_probability < 1:
            selection_method(ga)
        else:
            raise Exception("Selection probability must be between 0 and 1 to select parents.")

    return new_method


def _check_positive_fitness(selection_method):
    """Raises an exception if the population contains a
    chromosome with negative fitness. Otherwise runs
    the selection method.
    """

    def new_method(ga):
        if ga.get_chromosome_fitness(0) > 0 and ga.get_chromosome_fitness(-1) >= 0:
            selection_method(ga)
        else:
            raise Exception("Converted fitness values can't have negative values or be all 0. Consider using rank selection or stochastic selection instead.")

    return new_method


def _ensure_sorted(selection_method):
    """Sorts the population by fitness
    and then runs the selection method.
    """

    def new_method(ga):
        ga.population.sort_by_best_fitness(ga)
        selection_method(ga)

    return new_method


def _compute_parent_amount(selection_method):
    """Computes the amount of parents
    needed to be selected, and passes it
    as another argument for the method.
    """

    def new_method(ga):
        parent_amount = max(2, round(len(ga.population)*ga.parent_ratio))
        selection_method(ga, parent_amount)

    return new_method


class Parent_Selection:

    # Allowing access to decorators when importing class
    _check_selection_probability = _check_selection_probability
    _check_positive_fitness      = _check_positive_fitness
    _ensure_sorted               = _ensure_sorted
    _compute_parent_amount       = _compute_parent_amount


    class Rank:
        """Methods for selecting parents based on their rankings in the population
        i.e. the n-th best chromosome has a fixed probability of being selected,
        regardless of their chances"""

        @_check_selection_probability
        @_ensure_sorted
        @_compute_parent_amount
        def tournament(ga, parent_amount):
            """
            Will make tournaments of size tournament_size and choose the winner (best fitness) 
            from the tournament and use it as a parent for the next generation. The total number 
            of parents selected is determined by parent_ratio, an attribute to the GA object.
            """

            # Choose the tournament size.
            # Use no less than 5 chromosomes per tournament.
            tournament_size = int(len(ga.population)*ga.tournament_size_ratio)
            if tournament_size < 5:
                tournament_size = min(5, len(ga.population))

            # Repeat tournaments until the mating pool is large enough.
            while True:

                # Generate a random tournament group and sort by fitness.
                tournament_group = sorted(random.sample(
                    range(len(ga.population)),
                    k = tournament_size
                ))

                # For each chromosome, add it to the mating pool based on its rank in the tournament.
                for index in range(tournament_size):

                    # Probability required is selection_probability * (1-selection_probability) ^ index
                    # Each chromosome is (1-selection_probability) times
                    # more likely to become a parent than the next ranked.
                    if random.random() < ga.selection_probability * pow(1-ga.selection_probability, index):
                        ga.population.set_parent(tournament_group[index])

                        # Stop tournament selection if enough parents are selected
                        if len(ga.population.mating_pool) >= parent_amount:
                            return


        @_check_selection_probability
        @_ensure_sorted
        @_compute_parent_amount
        def stochastic(ga, parent_amount):
            """
            Selects parents using the same probability approach as tournament selection,
            but doesn't create tournaments. Uses random.choices with weighted values to
            select parents and may produce duplicate parents.
            """

            # Set the weights of each parent based on their rank.
            # Each chromosome is (1-selection_probability) times
            # more likely to become a parent than the next ranked.
            weights = [
                (1-ga.selection_probability) ** i
                for i
                in range(len(ga.population))
            ]

            # Set the mating pool.
            ga.population.mating_pool = random.choices(ga.population, weights, k = parent_amount)


    class Fitness:

        @_check_selection_probability
        @_ensure_sorted
        @_check_positive_fitness
        @_compute_parent_amount
        def roulette(ga, parent_amount):
            """Roulette selection works based off of how strong the fitness is of the
            chromosomes in the population. The stronger the fitness the higher the probability
            that it will be selected. Using the example of a casino roulette wheel.
            Where the chromosomes are the numbers to be selected and the board size for
            those numbers are directly proportional to the chromosome's current fitness. Where
            the ball falls is a randomly generated number between 0 and 1.
            """

            # The sum of all the fitnessess in a population
            fitness_sum = sum(
                ga.get_chromosome_fitness(index)
                for index
                in range(len(ga.population))
            )

            # A list of ranges that represent the probability of a chromosome getting chosen
            probability = [ga.selection_probability]

            # The chance of being selected increases incrementally
            for index in range(len(ga.population)):
                probability.append(probability[-1]+ga.get_chromosome_fitness(index)/fitness_sum)

            probability = probability[1:]

            # Loops until it reaches a desired mating pool size
            while len(ga.population.mating_pool) < parent_amount:

                # Spin the roulette
                rand_number = random.random()

                # Find where the roulette landed.
                for index in range(len(probability)):
                    if (probability[index] >= rand_number):
                        ga.population.set_parent(index)
                        break


        @_check_selection_probability
        @_ensure_sorted
        @_compute_parent_amount
        def stochastic(ga, parent_amount):
            """
            Selects parents using the same probability approach as roulette selection,
            but doesn't spin a roulette for every selection. Uses random.choices with
            weighted values to select parents and may produce duplicate parents.
            """

            # All fitnesses are the same, select randomly.
            if ga.get_chromosome_fitness(-1) == ga.get_chromosome_fitness(0):
                offset = 1-ga.get_chromosome_fitness(-1)

            # Some chromosomes have negative fitness, shift them all into positives.
            elif ga.get_chromosome_fitness(-1) < 0:
                offset = -ga.get_chromosome_fitness(-1)

            # No change needed.
            else:
                offset = 0

            # Set the weights of each parent based on their fitness + offset.
            weights = [
                ga.get_chromosome_fitness(index) + offset
                for index
                in range(len(ga.population))
            ]

            inflation = sum(weights) * (1 - ga.selection_probability)

            # Rescale and adjust using selection_probability so that
            #   if selection_probability is high, a low inflation is used,
            #     making selection mostly based on fitness.
            #   if selection_probability is low, a high offset is used,
            #     so everyone has a more equal chance.
            weights = [
                weight + inflation
                for weight
                in weights
            ]

            # Set the mating pool.
            ga.population.mating_pool = random.choices(ga.population, weights, k = parent_amount)
