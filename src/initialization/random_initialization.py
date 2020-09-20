from initialization.initialization import initialization
import EasyGA as ga
import random

class random_initialization(initialization):
    def initialize(self, population_size, chromosome_length,user_defined_function):
        # Create the population object
        population = ga.population()
        # Fill the population with chromosomes
        for i in range(population_size):
            #Create the chromosome object
            chromosome = ga.chromosome()
            #Fill the Chromosome with genes
            for j in range(chromosome_length):
                # File the gene object with a value
                    # Where the user function is being implimented ---
                chromosome.add_gene(ga.gene(user_defined_function()))
                    # --------
            population.add_chromosome(chromosome)
        return population
