# Graphing package
import matplotlib.pyplot as plt

class Matplotlib_Graph:
    """Prebuilt graphing functions to make visual represention of fitness data."""


    def __init__(self, database):
        self.database = database


    def make_plot(self, type_of_plot, size, X, Y):
        """Create the plot"""

        # Set the plot size
        plt.figure(figsize = size)

        if(type_of_plot  == "line"):
            plt.plot(X, Y)
        elif(type_of_plot == "scatter"):
            plt.scatter(X, Y)
        elif(type_of_plot == "bar"):
            plt.bar(X, Y)


    def generation_total_fitness(self, type_of_plot = "line", size = [6,6]):
        """Show a plot of generation by generation total fitness."""

        # Query the X data
        generations = self.database.get_total_generations()

        # Create the generations list - [0,1,2,etc]
        X = list(range(0, generations))

        # Query for Y data
        Y = self.database.get_generation_total_fitness()

        self.make_plot(type_of_plot, size, X, Y)

        # x and y labels
        plt.xlabel('Generation')
        plt.ylabel('Generation Total Fitness')
        plt.title('Relationship Between Generations and Generation Total Fitness')

        # Show the plot
        plt.show()


    def highest_value_chromosome(self, type_of_plot = "line", size = [6,6]):
        """Generation by Max value chromosome """

        # Query the X data
        generations = self.database.get_total_generations()

        # Create the generations list - [0,1,2,etc]
        X = list(range(0, generations))

        # Query for Y data
        Y = self.database.get_highest_chromosome()

        self.make_plot(type_of_plot, size, X, Y)

        # x and y labels
        plt.xlabel('Generation')
        plt.ylabel('Generation Highest Fitness Chromosome')
        plt.title('Relationship Between Generations and Highest Value Chromosome')

        # Show the plot
        plt.show()


    def lowest_value_chromosome(self, type_of_plot = "line", size = [6,6]):
        """Generation by Min value Chromosome """

        # Query the X data
        generations = self.database.get_total_generations()

        # Create the generations list - [0,1,2,etc]
        X = list(range(0, generations))

        # Query for Y data
        Y = self.database.get_lowest_chromosome()

        self.make_plot(type_of_plot, size, X, Y)

        # x and y labels
        plt.xlabel('Generation')
        plt.ylabel('Generation Highest Fitness Chromosome')
        plt.title('Relationship Between Generations and Lowest Value Chromosome')

        # Show the plot
        plt.show()
