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
        self.type_of_plot = plt.plot
        self.size = [6,6]
        self.xlabel = None
        self.ylabel = None
        self.title = None
        self.yscale = "linear"


    def plt_setup(self, X, Y, yscale, xlabel, ylabel, title, type_of_plot, size):
        """Setup for plt"""

        if self.xlabel is not None: xlabel = self.xlabel
        if self.ylabel is not None: xlabel = self.ylabel
        if self.title  is not None: xlabel = self.title

        if yscale == "log":
            # If using log then the values have to be positive numbers
            Y  =  [abs(ele) for ele in Y]

        # Setup data
        plt.figure(figsize = size)
        plt.yscale(self.yscale)
        type_of_plot(X, Y)

        # labels
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)

        # Show the plot
        plt.show()


    def generation_total_fitness(self):
        """Show a plot of generation by generation total fitness."""

        # Query the X data
        generations = self.database.get_total_generations()

        # Create the generations list - [0,1,2,etc]
        X = list(range(0, generations))

        # Query for Y data
        Y = self.database.get_generation_total_fitness()

        self.plt_setup(X, Y, self.yscale, 'Generation', 'Generation Total Fitness', 'Relationship Between Generations and Generation Total Fitness', self.type_of_plot, self.size)


    def highest_value_chromosome(self):
        """Generation by Max value chromosome """

        # Query the X data
        generations = self.database.get_total_generations()

        # Create the generations list - [0,1,2,etc]
        X = list(range(0, generations))

        # Query for Y data
        Y = self.database.get_highest_chromosome()

        self.plt_setup(X, Y, self.yscale, 'Generation', 'Highest Fitness', 'Relationship Between Generations and Highest Fitness', self.type_of_plot, self.size)


    def lowest_value_chromosome(self):
        """Generation by Min value Chromosome """

        # Query the X data
        generations = self.database.get_total_generations()

        # Create the generations list - [0,1,2,etc]
        X = list(range(0, generations))

        print(X)

        # Query for Y data
        Y = self.database.get_lowest_chromosome()

        self.plt_setup(X, Y, self.yscale, 'Generation', 'Lowest Fitness', 'Relationship Between Generations and Lowest Fitness', self.type_of_plot, self.size)


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
