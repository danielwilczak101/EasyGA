import matplotlib.pyplot as plt

import EasyGA

for _ in range(2):
    # Create a new genetic algorithm each.
    ga = EasyGA.GA()
    ga.evolve()
    ga.print_population()

# Graph the average of the two runs
plt.subplot(1, 2, 1)
ga.graph.highest_value_chromosome("average")

plt.subplot(1, 2, 1)
ga.graph.highest_value_chromosome("all")

ga.graph.show()
