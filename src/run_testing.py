import EasyGA
import random
# Create the Genetic algorithm
ga = EasyGA.GA()

ga.chromosome_length = 3

# If the user wants to use a domain
ga.gene_impl = [random.randrange,1,10]


# Run Everyhting
ga.evolve()

# Print the current population
ga.population.print_all()
