import random

class Parent_Selection:

    class Rank:

        def tournament(ga):
            """
            Will make tournaments of size tournament_size and choose the winner (best fitness) 
            from the tournament and use it as a parent for the next generation. The total number 
            of parents selected is determined by parent_ratio, an attribute to the GA object.
            """

            # Error if can't select parents
            if ga.selection_probability <= 0:
                print("Selection probability must be greater than 0 to select parents.")
                return

            # Make sure the population is sorted by fitness
            ga.population.sort_by_best_fitness(ga)

            # Choose the tournament size.
            # Use no less than 5 chromosomes per tournament.
            tournament_size = int(ga.population.size()*ga.tournament_size_ratio)
            if tournament_size < 5:
                tournament_size = 5

            # Repeat tournaments until the mating pool is large enough.
            while (len(ga.population.get_mating_pool()) < ga.population.size()*ga.parent_ratio):

                # Generate a random tournament group and sort by fitness.
                tournament_group = sorted([random.randint(0, ga.population.size()-1) for n in range(tournament_size)])

                # For each chromosome, add it to the mating pool based on its rank in the tournament.
                for index in range(tournament_size):

                    # Probability required is selection_probability * (1-selection_probability) ^ index
                    # e.g. top ranked fitness has probability: selection_probability
                    #   second ranked fitness has probability: selection_probability * (1-selection_probability)
                    #   third  ranked fitness has probability: selection_probability * (1-selection_probability)^2
                    # etc.
                    if random.uniform(0, 1) < ga.selection_probability * pow(1-ga.selection_probability, index):
                        ga.population.set_parent(tournament_group[index])

                        # Stop if parent ratio reached
                        if len(ga.population.get_mating_pool()) >= ga.population.size()*ga.parent_ratio:
                            break


    class Fitness:

        def roulette(ga):
            """Roulette selection works based off of how strong the fitness is of the
            chromosomes in the population. The stronger the fitness the higher the probability
            that it will be selected. Using the example of a casino roulette wheel.
            Where the chromosomes are the numbers to be selected and the board size for
            those numbers are directly proportional to the chromosome's current fitness. Where
            the ball falls is a randomly generated number between 0 and 1.
            """

            # Make sure the population is sorted by fitness
            ga.population.sort_by_best_fitness(ga)

            # Error if can't select parents
            if ga.selection_probability <= 0:
                print("Selection probability must be greater than 0 to select parents.")
                return

            # Error if not all chromosomes has positive fitness
            if (ga.get_chromosome_fitness(0) == 0 or ga.get_chromosome_fitness(-1) < 0):
                print("Error using roulette selection, all fitnesses must be positive.")
                print("Consider using stockastic roulette selection or tournament selection.")
                return

            # The sum of all the fitnessess in a population
            fitness_sum = sum(ga.get_chromosome_fitness(index) for index in range(ga.population.size()))

            # A list of ranges that represent the probability of a chromosome getting chosen
            probability = [ga.selection_probability]

            # The chance of being selected increases incrementally
            for index in range(ga.population.size()):
                probability.append(probability[-1]+ga.get_chromosome_fitness(index)/fitness_sum)

            probability = probability[1:]

            # Loops until it reaches a desired mating pool size
            while (len(ga.population.get_mating_pool()) < ga.population.size()*ga.parent_ratio):

                # Spin the roulette
                rand_number = random.random()

                # Find where the roulette landed.
                for index in range(len(probability)):
                    if (probability[index] >= rand_number):
                        ga.population.set_parent(index)
                        break


        def stochastic(ga):
            """Stochastic roulette selection works based off of how strong the fitness is of the
            chromosomes in the population. The stronger the fitness the higher the probability
            that it will be selected. Instead of dividing the fitness by the sum of all fitnesses
            and incrementally increasing the chance something is selected, the stochastic method
            just divides by the highest fitness and selects randomly."""

            # Make sure the population is sorted by fitness
            ga.population.sort_by_best_fitness(ga)

            # Error if can't select parents
            if ga.selection_probability <= 0 or ga.selection_probability >= 1:
                print("Selection probability must be between 0 and 1 to select parents.")
                return

            max_fitness = ga.get_chromosome_fitness(0)

            # Error if the highest fitness is not positive
            if max_fitness <= 0:
                print("Error using stochastic roulette selection, best fitness must be positive.")
                print("Consider using tournament selection.")
                return

            # Loops until it reaches a desired mating pool size
            while (len(ga.population.get_mating_pool()) < ga.population.size()*ga.parent_ratio):

                # Selected chromosome
                index = random.randint(0, ga.population.size()-1)

                # Probability of becoming a parent is fitness/max_fitness
                if random.uniform(ga.selection_probability, 1) < ga.get_chromosome_fitness(index)/max_fitness:
                    ga.population.set_parent(index)
