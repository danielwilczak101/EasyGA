import random
import EasyGA

# Create the Genetic algorithm
ga = EasyGA.GA()

# Makes a new gene
new_gene = ga.make_gene("HelloWorld")
# Makes a chromosome to store genes in
new_chromosome = ga.make_chromosome()
# Makes a Population to store chromosomes in
new_population = ga.make_population()

ga.initialize()

print(ga.population)

for chromosome in ga.population.chromosomes:
    print(chromosome.genes[0].__dict__)
