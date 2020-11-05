import random
import EasyGA

# Create the Genetic algorithm
ga = EasyGA.GA()

ga.population_size = 3
ga.generation_goal = 10
# Evolve the genetic algorithm
ga.evolve()

# Print your default genetic algorithm
ga.print_generation()
ga.print_population()
