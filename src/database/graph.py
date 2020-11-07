# Graphing package
import matplotlib.pyplot as plt
# Database class
from database import database
from sqlite3 import Error

class graph:
    """Prebuilt graphing functions to make visual represention of fitness data."""

    def generation_total_fitness(ga,type_of_plot = "line",size = [6,6]):
        """Show a plot of generation by generation total fitness."""

        # Query the X data
        generations = ga.database.get_total_generations()

        # Create the generations list - [0,1,2,etc]
        X = list(range(0, generations))

        # Query for Y data
        Y = ga.database.get_generation_total_fitness()

        # Set the plot size
        plt.figure(figsize=size)

        if(type_of_plot  == "line"):
            plt.plot(X,Y)
        elif(type_of_plot == "scatter"):
            plt.scatter(X,Y)
        elif(type_of_plot == "bar"):
            plt.bar(X,Y)

        # x and y labels
        plt.xlabel('Generation')
        plt.ylabel('Generation Total Fitness')
        plt.title('Relationship Between Generations and Generation Total Fitness')

        # Show the plot
        plt.show()

    def highest_value_chromosome(ga,type_of_plot = "line",size = [6,6]):
        """Generation by Max value chromosome """

        # Query the X data
        generations = ga.database.get_total_generations()

        # Create the generations list - [0,1,2,etc]
        X = list(range(0, generations))

        # Query for Y data
        Y = ga.database.get_highest_chromosome()

        # Set the plot size
        plt.figure(figsize=size)

        if(type_of_plot  == "line"):
            plt.plot(X,Y)
        elif(type_of_plot == "scatter"):
            plt.scatter(X,Y)
        elif(type_of_plot == "bar"):
            plt.bar(X,Y)

        # x and y labels
        plt.xlabel('Generation')
        plt.ylabel('Generation Highest Fitness Chromosome')
        plt.title('Relationship Between Generations and Highest Value Chromosome')

        # Show the plot
        plt.show()


    def lowest_value_chromosome(ga,type_of_plot = "line",size = [6,6]):
        """Generation by Min value Chromosome """

        # Query the X data
        generations = ga.database.get_total_generations()

        # Create the generations list - [0,1,2,etc]
        X = list(range(0, generations))

        # Query for Y data
        Y = ga.database.get_lowest_chromosome()

        # Set the plot size
        plt.figure(figsize=size)

        if(type_of_plot  == "line"):
            plt.plot(X,Y)
        elif(type_of_plot == "scatter"):
            plt.scatter(X,Y)
        elif(type_of_plot == "bar"):
            plt.bar(X,Y)

        # x and y labels
        plt.xlabel('Generation')
        plt.ylabel('Generation Highest Fitness Chromosome')
        plt.title('Relationship Between Generations and Lowest Value Chromosome')

        # Show the plot
        plt.show()
