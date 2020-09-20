import random
import EasyGA

def user_gene_function():
    return random.randint(1, 100)

Population_size = 10
Chromosome_length = 10

ga = EasyGA.GA(Population_size, Chromosome_length,user_gene_function)

# Setup the GA's population,chromosomes and genes
ga.initialize()

print(ga.population.chromosomes[0].print_chromosome())
