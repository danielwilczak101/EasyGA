<<<<<<< Updated upstream
# Import all the data prebuilt modules
from initialization.population_structure.population import population as create_population
from initialization.chromosome_structure.chromosome import chromosome as create_chromosome
from initialization.gene_structure.gene import gene as create_gene

# Import functions for defaults
from initialization.gene_function.gene_random import random_gene
# Import functionality defaults
from initialization.random_initialization import random_initialization


class GA:
    def __init__(self):
        # Default variables
        self.population = None
        self.generations = 3
        self.chromosome_length = 4
        self.population_size = 5
        self.mutation_rate = 0.03
        # Defualt EastGA implimentation structure
        self.gene_function_impl = random_gene
        self.gene_input = []
        self.gene_input_type = []

        while len(self.gene_input_type) != self.chromosome_length:
            self.gene_input_type.append(None)
            
        # Set the GA Configuration
        self.initialization_impl = random_initialization
        #self.mutation_impl = PerGeneMutation(Mutation_rate)
        #self.selection_impl = TournamentSelection()
        #self.crossover_impl = FastSinglePointCrossover()
        #self.termination_impl = GenerationTermination(Total_generations)
        #self.evaluation_impl = TestEvaluation()


    def initialize(self, gene_input):
        self.gene_input = gene_input

        #It's possible user may just enter "domain", "float-range", etc. for gene_input_type rather than referring to a specific gene
        #In that case, create an array with the same length as the chromosome where each element is just the user's input
        if isinstance(self.gene_input_type, str):
            gene_input_type_temp = self.gene_input_type
            self.gene_input_type = []
            while len(self.gene_input_type) != self.chromosome_length:
                self.gene_input_type.append(gene_input_type_temp)


        #There are two types of gene_input we should expect from the user - "general" or index-dependent
        #For example, if a user just enters [1,100], it should be assumed that this is a range/domain that should apply to all genes in the chromosome...
        #...rather than assuming that it means gene 1 should be 1 and gene 2 should be 100.
        #The check for this is done by checking if any of the values in the user's gene input are lists.
        #If lists are included, then values like the ones given above will be converted (i.e. [1, 100, ["up", "left"]] becomes [[1,1], [100,100], ["up", "left"]]) and apply to specific genes
        #Else if no lists are included, the gene input will apply to each gene (i.e. for chromosomes with length 3, [1,100] becomes [[1,100],[1,100],[1,100]])
        general_gene_input = True
        for n in range(len(self.gene_input)):
            if isinstance(self.gene_input[n], list):
                general_gene_input = False
                break

        #Converting user's input into standardized format - list of lists where each sublist is the range/domain for a specific gene
        if general_gene_input == False:
            for x in range(len(self.gene_input)):
                if isinstance(self.gene_input[x], list) == False:
                    self.gene_input[x] = [self.gene_input[x], self.gene_input[x]]
        else:
            gene_input_temp = self.gene_input
            self.gene_input = []
            for y in range(self.chromosome_length):
                self.gene_input.append(gene_input_temp)

        #Setting up the gene_input_type defaults in the standard format
        #values including strings are always domain
        #values including floats but no strings is a float-range
        #values included neither strings or floats is a normal range
        for x in range(len(self.gene_input_type)):
            try:
                if (self.gene_input[x]):
                    pass
            except IndexError:
                self.gene_input.append(None)

            if self.gene_input_type[x] == None and self.gene_input[x] != None: #If it hasn't been hard-set by the user
                for y in range(len(self.gene_input[x])):
                    if isinstance(self.gene_input[x][y], str):
                        self.gene_input_type[x] = "domain"
                        break
                    elif isinstance(self.gene_input[x][y], float):
                        self.gene_input_type[x] = "float-range"
                    elif y == (len(self.gene_input[x]) -1 and self.gene_input_type[x] != "float-range"):
                        self.gene_input_type[x] = "range"

        # Create the first population
        self.population = self.initialization_impl(
        self.chromosome_length,
        self.population_size,
        self.gene_function_impl,
        self.gene_input,
        self.gene_input_type)


    def evolve():
        # If you just want to evolve through all generations
        pass

    def evolve_generation(self, number_of_generations):
        # If you want to evolve through a number of generations
        # and be able to pause and output data based on that generation run.
        pass
=======
import random
# Import all the data structure prebuilt modules
from initialization import Population as create_population
from initialization import Chromosome as create_chromosome
from initialization import Gene as create_gene
# Import example classes
from fitness_function import Fitness_Examples
from initialization import Initialization_Types
from termination_point import Termination_Types
from selection import Selection_Types
from crossover import Crossover_Types
from mutation import Mutation_Types

class GA:
    def __init__(self):
        """Initialize the GA."""
        # Initilization variables
        self.chromosome_length = 10
        self.population_size = 100
        self.chromosome_impl = None
        self.gene_impl = None
        self.population = None
        # Termination varibles
        self.current_generation = 0
        self.current_fitness = 0
        self.generation_goal = 35
        self.fitness_goal = 3
        # Mutation variables
        self.mutation_rate = 0.075

        # Rerun already computed fitness
        self.update_fitness = True

        # Defualt EastGA implimentation structure
        self.initialization_impl = Initialization_Types().random_initialization
        self.fitness_function_impl = Fitness_Examples().is_it_5
        self.mutation_impl = Mutation_Types().random_mutation
        self.selection_impl = Selection_Types().tournament_selection
        self.crossover_impl = Crossover_Types().single_point_crossover
        self.termination_impl = Termination_Types().generation_based

    def initialize_population(self):
        """Initialize the population using the initialization
         implimentation that is currently set"""
        self.population = self.initialization_impl(self)
        
    def set_all_fitness(self,chromosome_set):
        """Will get and set the fitness of each chromosome in the population.
        If update_fitness is set then all fitness values are updated.
        Otherwise only fitness values set to None (i.e. uninitialized
        fitness values) are updated."""
        # Get each chromosome in the population

        for chromosome in chromosome_set:
            if(chromosome.fitness == None or self.update_fitness == True):
                # Set the chromosomes fitness using the fitness function
                chromosome.set_fitness(self.fitness_function_impl(chromosome))

    def evolve(self):
        """Runs the ga until the termination point has been satisfied."""
        # While the termination point hasnt been reached keep running
        while(self.active()):
            self.evolve_generation()

    def evolve_generation(self, number_of_generations = 1, consider_termination = True):
        """Evolves the ga the specified number of generations."""
        while(number_of_generations > 0 and (consider_termination == False or self.termination_impl(self))):
            # If its the first generation then initialize the population
            if self.current_generation == 0:
                self.initialize_population()
                self.set_all_fitness(self.population.chromosomes)
            
            next_population = self.selection_impl(self)
            self.population = next_population
            self.set_all_fitness(self.population.chromosomes)

            number_of_generations -= 1
            self.current_generation += 1
>>>>>>> Stashed changes

    def active(self):
        """Returns if the ga should terminate base on the termination implimented"""
        return self.termination_impl(self)

    def make_gene(self,value):
        return create_gene(value)

    def make_chromosome(self):
        return create_chromosome()

    def make_population(self):
        return create_population()
