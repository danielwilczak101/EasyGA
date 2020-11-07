# Graphing package
import matplotlib.pyplot as plt
# Database class
from database import database
from sqlite3 import Error

class graph:
    """ """

    def scatter(ga):
        """Show a scatter plot of the database information."""

        # Query the X data
        generations = ga.database.query_one_item("SELECT COUNT(DISTINCT generation) FROM data;")

        # Create the generations array
        X = list(range(0, generations))

        #Query the Y data
        Y_data = ga.database.query_all("SELECT SUM(fitness) FROM data GROUP BY generation;")

        # Format the Y data so we can use it to plot
        Y = [i[0] for i in Y_data]

        # Set the plot size
        plt.figure(figsize=[5, 5])

        plt.scatter(X,Y)
        # x and y labels
        plt.xlabel('Generation')
        plt.ylabel('Generation Total Fitness')
        plt.title('Relationship Between Generations and Generation Total Fitness')

        # Show the plot
        plt.show()


    def line(ga):
        pass
