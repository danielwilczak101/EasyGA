import random
import EasyGA

# Create the Genetic algorithm
ga = EasyGA.GA()

ga.chromosome_length = 100

ga.evolve()

print(f"Current Generation: {ga.current_generation}")
ga.population.print_all()
