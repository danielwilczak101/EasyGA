# Graphing package
import matplotlib.pyplot as plt
import numpy as np


class Matplotlib_Graph:
    """Prebuilt graphing functions to make visual
    represention of fitness data."""

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
        self.legend = False

    def average_config_id(self,function):
        """Graph average line of all config_id's from data stored
        in the database."""

        # Get all the config's
        config_ids = self.database.get_all_config_id()

        stored_list = []

        # Store each list so it can be averaged later
        for config_id in config_ids:
            stored_list.append(function(config_id))

        y = np.average(stored_list, axis=0)
        x = self.database.get_each_generation_number(config_id)
        self.type_of_graph(x, y)

    def all_config_id(self,function):
        """Graph each config_id's data stored in the database
        using multiple different colored lines."""
        # Get all the config's
        config_ids = self.database.get_all_config_id()

        # Turn on the legend
        #self.legend = True

        # Get the x and y data for each config_id
        for config_id in config_ids:

            # Get x and y data
            x = self.database.get_each_generation_number(config_id)
            y = function(config_id)
            # Graph the line but dont show
            self.type_of_graph(x, y, label=f"Config_id - {config_id}")


    def generation_total_fitness(self, config_id = None):
        """Show a plot of generation by generation total fitness."""

        if config_id == "all":
            # If the user want to plot all the config_id's
            self.all_config_id(self.database.get_generation_total_fitness)
        elif config_id == "average":
            # if the user wants an average plot of all config_id's
            self.average_config_id(self.database.get_generation_total_fitness)
        else:
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

        if config_id == "all":
            # If the user want to plot all the config_id's
            self.all_config_id(self.database.get_highest_chromosome)
        elif config_id == "average":
            # if the user wants an average plot of all config_id's
            self.average_config_id(self.database.get_highest_chromosome)
        else:
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

        if config_id == "all":
            # If the user want to plot all the config_id's
            self.all_config_id(self.database.get_lowest_chromosome)
        elif config_id == "average":
            # if the user wants an average plot of all config_id's
            self.average_config_id(self.database.get_lowest_chromosome)
        else:
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

        if self.legend == True:
            plt.legend()

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
