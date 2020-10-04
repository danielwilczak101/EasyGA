# Import the data structure
from .population_structure.population import Population as create_population
from .chromosome_structure.chromosome import Chromosome as create_chromosome
from .gene_structure.gene import Gene as create_gene

class Initialization_Types:
    """Initialization examples that are used as defaults and examples"""

    def random_initialization(self, ga):
        """Takes the initialization inputs and choregraphs them to output the type of population
        with the given parameters."""
        # Create the population object
        population = create_population()

        # Fill the population with chromosomes
        for i in range(ga.population_size):
            chromosome = create_chromosome()
            #Fill the Chromosome with genes
            for j in range(ga.chromosome_length):
                # Using the chromosome_impl to set every index inside of the chromosome
                if ga.chromosome_impl != None:
                    # Each chromosome location is specified with its own function
                    chromosome.add_gene(create_gene(ga.chromosome_impl(j)))
                    # Will break if chromosome_length != len(lists) in domain
                elif ga.gene_impl != None:
                    function = ga.gene_impl[0]
                    chromosome.add_gene(create_gene(function(*ga.gene_impl[1:])))
                else:
                    #Exit because either were not specified
                    print("You did not specify any initialization constraints.")
            population.add_chromosome(chromosome)
        return population
