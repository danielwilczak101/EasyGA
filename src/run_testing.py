import EasyGA
import matplotlib.pyplot as plt

# Create the genetic algorithm
ga = EasyGA.GA()

# Create 25 chromosomes each with 10 genes and 200 generations
ga.population_size = 100
ga.chromosome_length = 10
ga.generation_goal = 150

# Evolve the genetic algorithm
ga.evolve()
# Print generation and population
ga.print_generation()
ga.print_population()

# Plot the data from the genetic algorithm
plt.figure(figsize = [6, 6])
ga.graph.highest_value_chromosome()  # Change this so it doesn't make its own figure or show
plt.xlabel('My datas generations')             # override the xlabel
plt.ylabel('How well the fitness is')  # override the ylabel
plt.title('My GA fitness x generations')     # override the title
plt.show()
