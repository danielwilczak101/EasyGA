# Defult packages for GA functionality
from initialization.random_initialization import random_initialization


class GA:
    def __init__(self):
        # Default variables
        self.population_size = defaults.generations
        self.chromosome_length = defaults.chromosome_length
        self.generations = defaults.generations
        # Defualt ga implimentation structure
        self.create_gene = defaults.default_gene_function()
        self.initialization = defaults.default_initialize()
        self.mutation = defaults.default_mutations_function()
        self.selection = defaults.default_selection_function()
        self.crossover = defaults.default_crossover_function()
        self.termination = defaults.default_termination_function(self.generations)
        self.fitness_function = defaults.default_fitness_function()

    def initialize(self):
        # Create the initial population
        self.population = self.initialization.initialize(self.population_size,
                                                                self.chromosome_length,
                                                                 self.user_gene_function)

    def evolve(self):
        # Evolve will run all the functions
        initialize()
