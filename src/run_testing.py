import EasyGA
import random

# Create the Genetic algorithm
ga = EasyGA.GA()

ga.generation_goal = 200
ga.population_size = 50

ga.evolve()

ga.print_population()

ga.graph_scatter()
