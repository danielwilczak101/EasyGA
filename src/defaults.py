
# Defult packages for GA functionality
from create_gene.random_gene import random_gene
from initialization.random_initialization import random_initialization



class defaults:
# Defult values so that the user doesnt have to explicidly
# state every feature of the genetic algorithm.
    def __init__(self):


    def gene_function(self):
        return random_gene(1,10)

    def fitness_function(self):
        pass

    def initialize_function(self):
        return random_initialization(population,chromosome,gene,
        chromosome_length,population_size,gene_function)

    def selection_function(self):
        return tournament_selection()

    def crossover_function(self):
        return fast_single_point_crossover()

    def mutations_function(self):
        return per_gene_mutation()

    def termination_point_function(self,amount):
        # The default termination point is based on how
        # many generations the user wants to run.
        return generation_termination(amount)

    def get_highest_fitness(self):
        # Get the highest fitness of the current generation
        pass

    def get_lowest_fitness(self):
        # Get the lowest fitness of the current generation
        pass
