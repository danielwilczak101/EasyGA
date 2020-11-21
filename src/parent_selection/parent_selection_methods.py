import random

def check_selection_probability(selection_method):
    """Raises an exception if the selection_probability
    is not between 0 and 1. Otherwise runs the selection
    method.
    """
    def helper(ga):
        if 0 < ga.selection_probability < 1:
            selection_method(ga)
        else:
            raise Exception("Selection probability must be greater than 0 to select parents.")
    return helper


def check_positive_fitness(selection_method):
    """Raises an exception if the population contains a
    chromosome with negative fitness. Otherwise runs
    the selection method.
    """
    def helper(ga):
        if ga.get_chromosome_fitness(0) > 0 and ga.get_chromosome_fitness(-1) >= 0:
            selection_method(ga)
        else:
            raise Exception("Converted fitness values must be all positive. Consider using rank selection instead.")
    return helper


def ensure_sorted(selection_method):
    """Sorts the population by fitness
    and then runs the selection method.
    """
    def helper(ga):
        ga.population.sort_by_best_fitness(ga)
        selection_method(ga)
    return helper


class Parent_Selection:

    # Private method decorators, see above.
    def __check_selection_probability(selection_method):
        return check_selection_probability(selection_method)
    def __check_positive_fitness(selection_method):
        return check_positive_fitness(selection_method)
    def __ensure_sorted(selection_method):
        return ensure_sorted(selection_method)


    class Rank:

        @check_selection_probability
        @ensure_sorted
        def tournament(ga):
            """
            Will make tournaments of size tournament_size and choose the winner (best fitness) 
            from the tournament and use it as a parent for the next generation. The total number 
            of parents selected is determined by parent_ratio, an attribute to the GA object.
            """

            # Choose the tournament size.
            # Use no less than 5 chromosomes per tournament.
            tournament_size = int(len(ga.population)*ga.tournament_size_ratio)
            if tournament_size < 5:
                tournament_size = 5

            # Repeat tournaments until the mating pool is large enough.
            while (len(ga.population.get_mating_pool()) < len(ga.population)*ga.parent_ratio):

                # Generate a random tournament group and sort by fitness.
                tournament_group = sorted([random.randrange(len(ga.population)) for _ in range(tournament_size)])

                # For each chromosome, add it to the mating pool based on its rank in the tournament.
                for index in range(tournament_size):

                    # Probability required is selection_probability * (1-selection_probability) ^ index
                    # e.g. top ranked fitness has probability: selection_probability
                    #   second ranked fitness has probability: selection_probability * (1-selection_probability)
                    #   third  ranked fitness has probability: selection_probability * (1-selection_probability)^2
                    # etc.
                    if random.random() < ga.selection_probability * pow(1-ga.selection_probability, index):
                        ga.population.set_parent(tournament_group[index])

                        # Stop if parent ratio reached
                        if len(ga.population.get_mating_pool()) >= len(ga.population)*ga.parent_ratio:
                            break


    class Fitness:

        @check_selection_probability
        @check_positive_fitness
        @ensure_sorted
        def roulette(ga):
            """Roulette selection works based off of how strong the fitness is of the
            chromosomes in the population. The stronger the fitness the higher the probability
            that it will be selected. Using the example of a casino roulette wheel.
            Where the chromosomes are the numbers to be selected and the board size for
            those numbers are directly proportional to the chromosome's current fitness. Where
            the ball falls is a randomly generated number between 0 and 1.
            """

            # The sum of all the fitnessess in a population
            fitness_sum = sum(ga.get_chromosome_fitness(index) for index in range(len(ga.population)))

            # A list of ranges that represent the probability of a chromosome getting chosen
            probability = [ga.selection_probability]

            # The chance of being selected increases incrementally
            for index in range(len(ga.population)):
                probability.append(probability[-1]+ga.get_chromosome_fitness(index)/fitness_sum)

            probability = probability[1:]

            # Loops until it reaches a desired mating pool size
            while (len(ga.population.get_mating_pool()) < len(ga.population)*ga.parent_ratio):

                # Spin the roulette
                rand_number = random.random()

                # Find where the roulette landed.
                for index in range(len(probability)):
                    if (probability[index] >= rand_number):
                        ga.population.set_parent(index)
                        break


        @check_selection_probability
        @check_positive_fitness
        @ensure_sorted
        def stochastic(ga):
            """Stochastic roulette selection works based off of how strong the fitness is of the
            chromosomes in the population. The stronger the fitness the higher the probability
            that it will be selected. Instead of dividing the fitness by the sum of all fitnesses
            and incrementally increasing the chance something is selected, the stochastic method
            just divides by the highest fitness and selects randomly."""

            max_fitness = ga.get_chromosome_fitness(0)

            # Loops until it reaches a desired mating pool size
            while (len(ga.population.get_mating_pool()) < len(ga.population)*ga.parent_ratio):

                # Selected chromosome
                index = random.randrange(len(ga.population))

                # Probability of becoming a parent is fitness/max_fitness
                if random.uniform(ga.selection_probability, 1) < ga.get_chromosome_fitness(index)/max_fitness:
                    ga.population.set_parent(index)
