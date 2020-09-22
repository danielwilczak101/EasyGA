# Defult packages for GA functionality
from initialization.random_initialization import random_initialization

import random
from defaults import defaults
import gene

class GA:
    def __init__(self):
        # Default variables
         self.gene = defaults.default_gene_function()
    #     self.population_size = defaults.generations
    #     self.chromosome_length = defaults.chromosome_length
    #     self.generations = defaults.generations
    #     # Defualt ga implimentation structure

    #     self.initialization = defaults.default_initialize()
    #     self.mutation = defaults.default_mutations_function()
    #     self.selection = defaults.default_selection_function()
    #     self.crossover = defaults.default_crossover_function()
    #     self.termination = defaults.default_termination_function(self.generations)
    #     self.fitness_function = defaults.default_fitness_function()
    #
    # def initialize(self):
    #     # Create the initial population
    #     self.population = self.initialization.initialize(self.population_size,
    #                                                             self.chromosome_length,
    #                                                              self.user_gene_function)
    #
    # def evolve(self):
    #     # Evolve will run all the functions
    #     initialize()

    def evolve():
        # If you just want to evolve through all generations
        pass

    def evolve_generation(self, number_of_generations):
        # If you want to evolve through a number of generations
        # and be able to pause and output data based on that generation run.
        pass

    # What about if you want to see how each
