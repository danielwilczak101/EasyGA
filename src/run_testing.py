import EasyGA
import random


# Create the Genetic algorithm
ga = EasyGA.GA()



ga.gene_impl = [random.randrange,1,100]

# Run Everything
ga.evolve()

# Print the current population
print(f"Current Generation: {ga.current_generation}")
ga.population.print_all()
