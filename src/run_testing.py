import EasyGA
import random


# Create the Genetic algorithm
ga = EasyGA.GA()

#def random_parent_selection(population):
    #while ()

ga.gene_impl = [random.randrange,1,100]

# Run Everything
ga.evolve()

# Print the current population
ga.population.print_all()
