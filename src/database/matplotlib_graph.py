# Graphing package
import matplotlib.pyplot as plt

class Matplotlib_Graph:
    """Prebuilt graphing functions to make visual represention of fitness data."""

    # Common graphing functions
    type_of_graph_dict = {
            'line'    : plt.plot,
            'scatter' : plt.scatter,
            'bar'     : plt.bar
        }

    def __init__(self, database):
        self.database = database
        self.type_of_graph = 'line'
        self.x = None
        self.y = None
        self.yscale = "linear"


    def generation_total_fitness(self):
        """Show a plot of generation by generation total fitness."""

        # Query the X data
        generations = self.database.get_total_generations()

        # Create the generations list - [0,1,2,etc]
        self.x = list(range(0, generations))

        # Query for Y data
        self.y = self.database.get_generation_total_fitness()

        if self.yscale == "log":
            # If using log then the values have to be positive numbers
            self.y  =  [abs(ele) for ele in self.y]

        self.type_of_graph(self.x, self.y)
        plt.xlabel('Generation')
        plt.ylabel('Generation Total Fitness')
        plt.title('Relationship Between Generations and Generation Total Fitness')


    def highest_value_chromosome(self):
        """Generation by Max value chromosome """

        # Query the X data
        generations = self.database.get_total_generations()

        # Create the generations list - [0,1,2,etc]
        self.x  = list(range(0, generations))

        # Query for Y data
        self.y = self.database.get_highest_chromosome()

        if self.yscale == "log":
            # If using log then the values have to be positive numbers
            self.y  =  [abs(ele) for ele in self.y]

        self.type_of_graph(self.x, self.y)
        plt.xlabel('Generation')
        plt.ylabel('Highest Fitness')
        plt.title('Relationship Between Generations and Highest Fitness')


    def lowest_value_chromosome(self):
        """Generation by Min value Chromosome """

        # Query the X data
        generations = self.database.get_total_generations()

        # Create the generations list - [0,1,2,etc]
        self.x = list(range(0, generations))

        # Query for Y data
        self.y = self.database.get_lowest_chromosome()

        if self.yscale == "log":
            # If using log then the values have to be positive numbers
            self.y  =  [abs(ele) for ele in self.y]

        self.type_of_graph(self.x, self.y)
        plt.xlabel('Generation')
        plt.ylabel('Lowest Fitness')
        plt.title('Relationship Between Generations and Lowest Fitness')


    # Getter and setters
    @property
    def type_of_graph(self):
        return self._type_of_graph


    @type_of_graph.setter
    def type_of_graph(self, value_input):
        if value_input in self.type_of_graph_dict.keys():
            self._type_of_graph = self.type_of_graph_dict[value_input]
        else:
            self._type_of_plot = value_input
