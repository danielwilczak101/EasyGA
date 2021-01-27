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


    def generation_total_fitness(self, config_id = None):
        """Show a plot of generation by generation total fitness."""

        # Query the X data
        generations = self.database.get_total_generations(config_id)

        # Create the generations list - [0,1,2,etc]
        self.x = list(range(generations))

        # Query for Y data
        self.y = self.database.get_generation_total_fitness(config_id)

        self.type_of_graph(self.x, self.y)
        plt.yscale(self.yscale)
        plt.xlabel('Generation')
        plt.ylabel('Generation Total Fitness')
        plt.title('Relationship Between Generations and Generation Total Fitness')


    def highest_value_chromosome(self,config_id = None):
        """Generation by Max value chromosome """

        # Query the X data
        generations = self.database.get_total_generations(config_id)

        # Create the generations list - [0,1,2,etc]
        self.x  = list(range(generations))

        # Query for Y data
        self.y = self.database.get_highest_chromosome(config_id)

        self.type_of_graph(self.x, self.y)
        plt.yscale(self.yscale)
        plt.xlabel('Generation')
        plt.ylabel('Highest Fitness')
        plt.title('Relationship Between Generations and Highest Fitness')


    def lowest_value_chromosome(self,config_id = None):
        """Generation by Min value Chromosome """

        # Query the X data
        generations = self.database.get_total_generations(config_id)

        # Create the generations list - [0,1,2,etc]
        self.x = list(range(generations))

        # Query for Y data
        self.y = self.database.get_lowest_chromosome(config_id)

        self.type_of_graph(self.x, self.y)
        plt.yscale(self.yscale)
        plt.xlabel('Generation')
        plt.ylabel('Lowest Fitness')
        plt.title('Relationship Between Generations and Lowest Fitness')


    def show(self):
        """Used to show the matplot lib graph."""
        plt.show()


    # Getter and setters
    @property
    def type_of_graph(self):
        return self._type_of_graph


    @type_of_graph.setter
    def type_of_graph(self, value_input):
        if value_input in self.type_of_graph_dict.keys():
            self._type_of_graph = self.type_of_graph_dict[value_input]
        else:
            self._type_of_graph = value_input
