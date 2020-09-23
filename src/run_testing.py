import random
import EasyGA

# Create the Genetic algorithm
ga = EasyGA.GA()

# Start the population
ga.initialize()

new_gene = ga.make_gene("Hello")
print(new_gene.get_value())
print(new_gene.get_fitness())

for chromosome in ga.population.chromosomes:
    print(chromosome.genes[0].__dict__)
