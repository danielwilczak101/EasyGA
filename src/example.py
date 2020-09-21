import random
import EasyGA

# The user defined gene function
def user_gene_function():
    return random.randint(1, 100)

# The user defined Fitness Function
def user_fitness_function(chromosome):
    pass

# Standard user size requirements
Population_size = 10
Chromosome_length = 10

# Create the Genetic algorithm
ga = EasyGA.GA(Population_size, Chromosome_length,
                user_gene_function,user_fitness_function)
ga.initialize()

# Looking to print the first Chromosome
ga.population.chromosomes[0].print_chromosome()

# Looking to print one gene in chromosome 0
ga.population.chromosomes[0].genes[0].print_value()

# Looking to get the data of a chromosome
my_chromosome = ga.population.chromosomes[0].get_chromosome()
print(f"my_chromosome: {my_chromosome}")
# Looking to get the data of one gene in the chromosome
my_gene = ga.population.chromosomes[0].genes[0].get_value()
print(f"my_gene: {my_gene}")
