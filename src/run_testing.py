import EasyGA
import random

# Create the Genetic algorithm
ga = EasyGA.GA()

def user_defined_gene():
    return random.choice(["left","right","up","down"])

ga.gene_function_impl = user_defined_gene

# Creating population
ga.initialize()

# Print the current population
ga.population.print_all()
