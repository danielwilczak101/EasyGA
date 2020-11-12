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
        # Type
        self.type_of_plot = plt.plot
        # Size
        self.size = [6,6]
        # Labels
        self.xlabel = None
        self.ylabel = None
        self.title = None
        # Scale
        self.yscale = "linear"
        # Data points
        self.x = None
        self.y = None


    def plot(self):
        """Plot all the graph attributes"""

        if self.xlabel is not None: xlabel = self.xlabel
        if self.ylabel is not None: xlabel = self.ylabel
        if self.title  is not None: xlabel = self.title

        if yscale == "log":
            # If using log then the values have to be positive numbers
            self.y  =  [abs(ele) for ele in self.y]

        # Setup data
        plt.figure(figsize = self.size)
        plt.yscale(self.yscale)
        self.type_of_plot(self.x, self.y)

        # labels
        if self.xlabel is not None: xlabel = self.xlabel
        if self.ylabel is not None: xlabel = self.ylabel
        if self.title  is not None: xlabel = self.title

        # Show the plot
        plt.show()


    def generation_total_fitness(self):
        """Show a plot of generation by generation total fitness."""

        # Query the X data
        generations = self.database.get_total_generations()

        # Create the generations list - [0,1,2,etc]
        self.x = list(range(0, generations))

        # Query for Y data
        self.y = self.database.get_generation_total_fitness()

        self.xlabel = 'Generation'
        self.ylabel = 'Generation Total Fitness'
        self.title  = 'Relationship Between Generations and Generation Total Fitness'

        self.plot()


    def highest_value_chromosome(self):
        """Generation by Max value chromosome """

        # Query the X data
        generations = self.database.get_total_generations()

        # Create the generations list - [0,1,2,etc]
        self.x  = list(range(0, generations))

        # Query for Y data
        self.y = self.database.get_highest_chromosome()

        self.xlabel = 'Generation'
        self.ylabel = 'Highest Fitness'
        self.title  = 'Relationship Between Generations and Highest Fitness'

        self.plot()

    def lowest_value_chromosome(self):
        """Generation by Min value Chromosome """

        # Query the X data
        generations = self.database.get_total_generations()

        # Create the generations list - [0,1,2,etc]
        self.x = list(range(0, generations))

        # Query for Y data
        self.y = self.database.get_lowest_chromosome()

        self.xlabel = 'Generation'
        self.ylabel = 'Lowest Fitness'
        self.title  = 'Relationship Between Generations and Lowest Fitness'

        self.plot()

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
