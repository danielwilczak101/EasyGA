import random

from attributes import attributes


class GA(attributes):

    # Inhert all the ga attributes from the attributes class.
    def __init__(self):             
       super(GA, self).__init__()


    def evolve_generation(self, number_of_generations = 1, consider_termination = True):
        """Evolves the ga the specified number of generations."""

        while(number_of_generations > 0               # Evolve the specified number of generations
              and (not consider_termination           #     and if consider_termination flag is set
                   or self.termination_impl(self))):  #         then also check if termination conditions reached

            # If its the first generation then initialize the population
            if self.current_generation == 0:
                self.initialize_population()
                self.set_all_fitness()
                self.population.sort_by_best_fitness(self)

            # Otherwise evolve the population
            else:
                self.set_all_fitness()
                self.population.sort_by_best_fitness(self)
                self.parent_selection_impl(self)
                self.crossover_population_impl(self)
                self.survivor_selection_impl(self)
                self.mutation_population_impl(self)
                self.population.update()

            number_of_generations -= 1
            self.current_generation += 1


    def evolve(self):
        """Runs the ga until the termination point has been satisfied."""
        while(self.active()):
            self.evolve_generation()


    def active(self):
        """Returns if the ga should terminate based on the termination implimented."""
        return self.termination_impl(self)


    def initialize_population(self):
        """Initialize the population using
        the initialization implimentation
        that is currently set.
        """
        self.population = self.initialization_impl(self)


    def set_all_fitness(self):
        """Will get and set the fitness of each chromosome in the population.
        If update_fitness is set then all fitness values are updated.
        Otherwise only fitness values set to None (i.e. uninitialized
        fitness values) are updated.
        """

        # Check each chromosome
        for chromosome in self.population.get_chromosome_list():

            # Update fitness if needed or asked by the user
            if(chromosome.get_fitness() is None or self.update_fitness):
                chromosome.set_fitness(self.fitness_function_impl(chromosome))


    def sort_by_best_fitness(self, chromosome_set):
        """Sorts the array by fitness.
        1st element has highest fitness.
        2nd element has second highest fitness.
        etc.
        """

        return sorted(chromosome_set,                                    # list to be sorted
                     key = lambda chromosome: chromosome.get_fitness(),  # by fitness
                     reverse = True)                                     # from highest to lowest fitness
