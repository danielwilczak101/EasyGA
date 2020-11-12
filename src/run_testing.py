import EasyGA
import random

# Create the Genetic algorithm
ga = EasyGA.GA()

# Create 25 chromosomes each with 10 genes and 200 generations
ga.population_size = 100
ga.chromosome_length = 10
ga.generation_goal = 1000

ga.evolve()

ga.print_population()

ga.graph.highest_value_chromosome()
