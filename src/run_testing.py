import EasyGA
import random


# Create the Genetic algorithm
ga = EasyGA.GA()

ga.gene_impl = [random.randrange,1,25]

# Run Everything
ga.evolve()

# Print the current population
ga.population.print_all()
