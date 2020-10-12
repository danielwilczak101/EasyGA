import random
from initialization.chromosome_structure.chromosome import Chromosome as create_chromosome
from initialization.gene_structure.gene import Gene as create_gene
from initialization.population_structure.population import Population
from initialization.chromosome_structure.chromosome import Chromosome

class Survivor_Selection:
    """Survivor selection determines which individuals should be brought to the next generation"""

    def fill_in_best(ga, next_population):
        """Fills in the next population with the best chromosomes from the last population until the population size is met."""
        return Population(ga.population.get_all_chromosomes()[:ga.population.size()-next_population.size()] + next_population.get_all_chromosomes())
