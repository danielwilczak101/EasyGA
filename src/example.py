import random
import EasyGA

# The user defined gene function
def user_gene_function():
    return random.randint(1, 100)

# Standard user size requirements
Population_size = 10
Chromosome_length = 10

# Create the Genetic algorithm
ga = EasyGA.GA(Population_size, Chromosome_length,user_gene_function)
ga.initialize()

# Looking at the first chromosome in the population
ga.population.chromosomes[0].print_chromosome()
