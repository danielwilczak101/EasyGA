import random
import EasyGA

# Create the Genetic algorithm
ga = EasyGA.GA()

# Start the population
ga.initialize()

for chromosome in ga.population.chromosomes:
    print(chromosome.genes[0].__dict__)
