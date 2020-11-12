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


    def generation_total_fitness(self, type_of_plot = "line", size = [6,6]):
        """Show a plot of generation by generation total fitness."""

        # Query the X data
        generations = self.database.get_total_generations()

        # Create the generations list - [0,1,2,etc]
        X = list(range(0, generations))

        # Query for Y data
        Y_list = self.database.get_generation_total_fitness()

        if(self.yscale == "log"):
            # If using log then the values have to be positive numbers
            Y  =  [abs(ele) for ele in Y_list]

        # Setup data
        plt.figure(figsize = self.size)
        plt.yscale(self.yscale)
        self.type_of_plot(X,Y_list)

        # x and y labels
        if(self.xlabel == None):
            plt.xlabel('Generation')
        if(self.ylabel == None):
            plt.ylabel('Generation Total Fitness')
        if(self.title == None):
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
        Y_list = self.database.get_highest_chromosome()

        if(self.yscale == "log"):
            # If using log then the values have to be positive numbers
            Y  =  [abs(ele) for ele in Y_list]

        # Setup data
        plt.figure(figsize = self.size)
        plt.yscale(self.yscale)
        self.type_of_plot(X,Y_list)

        # x and y labels
        if(self.xlabel == None):
            plt.xlabel('Generation')
        if(self.ylabel == None):
            plt.ylabel('Generation Total Fitness')
        if(self.title == None):
            plt.title('Relationship Between Generations and Generation Total Fitness')
        # Show the plot
        plt.show()


    def lowest_value_chromosome(self, type_of_plot = "line", size = [6,6]):
        """Generation by Min value Chromosome """

        # Query the X data
        generations = self.database.get_total_generations()

        # Create the generations list - [0,1,2,etc]
        X = list(range(0, generations))

        # Query for Y data
        Y_list = self.database.get_lowest_chromosome()

        if(self.yscale == "log"):
            # If using log then the values have to be positive numbers
            Y  =  [abs(ele) for ele in Y_list]

        # Setup data
        plt.figure(figsize = self.size)
        plt.yscale(self.yscale)
        self.type_of_plot(X,Y_list)

        # x and y labels
        if(self.xlabel == None):
            plt.xlabel('Generation')
        if(self.ylabel == None):
            plt.ylabel('Generation Total Fitness')
        if(self.title == None):
            plt.title('Relationship Between Generations and Generation Total Fitness')
        # Show the plot
        plt.show()


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
