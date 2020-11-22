import EasyGA
import matplotlib.pyplot as plt

# Create the genetic algorithm
ga = EasyGA.GA()

ga.evolve()


ga.graph.highest_value_chromosome()
ga.graph.show()
