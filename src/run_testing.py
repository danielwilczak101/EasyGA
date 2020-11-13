import EasyGA
import random
import matplotlib.pyplot as plt

# Create the Genetic algorithm
ga = EasyGA.GA()

# Create 25 chromosomes each with 10 genes and 200 generations
ga.population_size = 100
ga.chromosome_length = 10
ga.generation_goal = 150

ga.evolve()

ga.print_population()

plt.figure(figsize = [6, 6])
ga.graph.highest_value_chromosome()  # Change this so it doesn't make its own figure or show
plt.xlabel('days passed')             # override the xlabel
plt.ylabel('products sold that day')  # override the ylabel
plt.title('Efficiency over time')     # override the title
plt.show()
