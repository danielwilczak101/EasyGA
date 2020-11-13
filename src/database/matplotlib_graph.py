# Graphing package
import matplotlib.pyplot as plt

class Matplotlib_Graph:
    """Prebuilt graphing functions to make visual represention of fitness data."""

    type_of_plot_dict = {
            'line'    : plt.plot,
            'scatter' : plt.scatter,
            'bar'     : plt.bar
        }

    def __init__(self, database):
        self.database = database
        self.type_of_plot = 'line'


    def generation_total_fitness(self):
        """Show a plot of generation by generation total fitness."""

        # Query the X data
        generations = self.database.get_total_generations()

        # Create the generations list - [0,1,2,etc]
        X = list(range(0, generations))

        # Query for Y data
        Y = self.database.get_generation_total_fitness()

        self.type_of_plot(X, Y)
        plt.xlabel('Generation')
        plt.ylabel('Generation Total Fitness')
        plt.title('Relationship Between Generations and Generation Total Fitness')


    def highest_value_chromosome(self):
        """Generation by Max value chromosome """

        # Query the X data
        generations = self.database.get_total_generations()

        # Create the generations list - [0,1,2,etc]
        X  = list(range(0, generations))

        # Query for Y data
        Y = self.database.get_highest_chromosome()

        self.type_of_plot(X, Y)
        plt.xlabel('Generation')
        plt.ylabel('Highest Fitness')
        plt.title('Relationship Between Generations and Highest Fitness')


    def lowest_value_chromosome(self):
        """Generation by Min value Chromosome """

        # Query the X data
        generations = self.database.get_total_generations()

        # Create the generations list - [0,1,2,etc]
        X = list(range(0, generations))

        # Query for Y data
        Y = self.database.get_lowest_chromosome()

        self.type_of_plot(X, Y)
        plt.xlabel('Generation')
        plt.ylabel('Lowest Fitness')
        plt.title('Relationship Between Generations and Lowest Fitness')


    # Getter and setters
    @property
    def type_of_plot(self):
        return self._type_of_plot


    @type_of_plot.setter
    def type_of_plot(self, _type_of_plot):
        if _type_of_plot in self.type_of_plot_dict.keys():
            self._type_of_plot = self.type_of_plot_dict[_type_of_plot]
        else:
            self._type_of_plot = _type_of_plot
