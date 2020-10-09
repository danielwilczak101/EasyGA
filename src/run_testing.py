import EasyGA
import random

# Create the Genetic algorithm
ga = EasyGA.GA()

ga.population_size = 15
ga.chromosome_length = 10
ga.generation_goal =  100
ga.gene_impl = [random.randint,1,10]

ga.evolve()

ga.population.print_all()