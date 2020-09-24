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

# Creating population
ga.initialize()

ga.population.print_all()
print("")
print(ga.population.chromosomes[0].__repr__())
