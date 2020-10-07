import random
from initialization.chromosome_structure.chromosome import Chromosome
from initialization.population_structure.population import Population

class Crossover_Methods:
    """ Crossover explination goes here.

    Points - Defined as sections between the chromosomes genetic makeup
    """
    def __init__(self):
        pass
    
    def single_point_crossover(ga):
        """Single  point crossover is when a "point" is selected and the genetic
        make up of the two parent chromosomes are "Crossed" or better known as swapped"""

        crossover_pool = ga.population.mating_pool
        
        new_population = Population()
        for i in range(len(crossover_pool)):
            if i + 1 < len(crossover_pool):
                new_gene_set = []
                parent_one = crossover_pool[i].get_genes()
                parent_two = crossover_pool[i+1].get_genes()
                #halfway_point = int(ga.chromosome_length/2)
                split_point = random.randint(0,ga.chromosome_length)    
                new_gene_set.extend(parent_one[0:split_point])
                new_gene_set.extend(parent_two[split_point:])
                new_chromosome = Chromosome(new_gene_set)
                new_population.add_chromosome(new_chromosome)

        return new_population
    
    def multi_point_crossover(ga, number_of_points = 2):
        """Multi point crossover is when a specific number (More then one) of
        "points" are created to merge the genetic makup of the chromosomes."""
        pass
