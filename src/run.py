import EasyGA
import matplotlib.pyplot as plt

# Create the genetic algorithm
ga = EasyGA.GA()

ga.evolve()

ga.database.past_runs()


ga.graph.highest_value_chromosome(1)  # Change this so it doesn't make its own figure or show
ga.graph.show()
