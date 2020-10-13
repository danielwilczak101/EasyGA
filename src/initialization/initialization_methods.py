# Import the data structure
from .population_structure.population import Population as create_population
from .chromosome_structure.chromosome import Chromosome as create_chromosome
from .gene_structure.gene import Gene as create_gene

class Initialization_Methods:
    """Initialization examples that are used as defaults and examples"""

    def random_initialization(ga):
        """Takes the initialization inputs and returns a population with the given parameters."""

        # Using the chromosome_impl to set every index inside of the chromosome
        if ga.chromosome_impl != None:
            return create_population([
                       create_chromosome([
                           create_gene(ga.chromosome_impl(j))
                       for j in range(ga.chromosome_length)])
                   for i in range(ga.population_size)])

        # Using the gene_impl to set every gene to be the same
        elif ga.gene_impl != None:
            function = ga.gene_impl[0]
            return create_population([
                       create_chromosome([
                           create_gene(function(*ga.gene_impl[1:]))
                       for j in range(ga.chromosome_length)])
                   for i in range(ga.population_size)])

        # Exit because no gene creation method specified
        else:
            print("You did not specify any initialization constraints.")
            return None
