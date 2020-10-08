import random
from initialization.chromosome_structure.chromosome import Chromosome as create_chromosome
from initialization.gene_structure.gene import Gene as create_gene
from initialization.population_structure.population import Population
from initialization.chromosome_structure.chromosome import Chromosome

class Survivor_Selection:
        def repeated_crossover(ga, next_population): #Might be cheating? I don't know honestly - RG
            while len(next_population.get_all_chromosomes()) < ga.population_size:
                crossover_pool = ga.population.mating_pool

                split_point = random.randint(0,ga.chromosome_length)    
                chromosome_list = []
                for i in range(len(crossover_pool)):
                    if i + 1 < len(crossover_pool):
                        new_gene_set = []
                        parent_one = crossover_pool[i].get_genes()
                        parent_two = crossover_pool[i+1].get_genes()
                        new_gene_set.extend(parent_one[0:split_point])
                        new_gene_set.extend(parent_two[split_point:])
                        new_chromosome = create_chromosome(new_gene_set)
                        chromosome_list.append(new_chromosome)
                        
                
                for i in range(len(chromosome_list)):
                    next_population.add_chromosome(chromosome_list[i])
                    if len(next_population.get_all_chromosomes()) >= ga.population_size:
                        break
            return next_population
    
        def remove_two_worst(ga, next_population):
            iterator = 0
            while len(next_population.get_all_chromosomes()) < ga.population_size:
                next_population.add_chromosome(ga.population.get_all_chromosomes()[iterator])
                iterator += 1
            return next_population