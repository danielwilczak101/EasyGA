import random

class Mutation_Methods:
    
    def __init__(self):
        pass

    def random_mutation(ga, chromosome_set = None):
        
        if chromosome_set == None:
            chromosome_set = ga.population.get_all_chromosomes()

        chromosome_mutate_num = int(len(chromosome_set)*ga.mutation_rate)
        temp_population = ga.initialization_impl(ga)

        while chromosome_mutate_num > 0:
            chromosome_set[random.randint(0,ga.population_size-1)] = temp_population.get_all_chromosomes()[chromosome_mutate_num]
            chromosome_mutate_num -= 1
        
        return chromosome_set
    
    def per_gene_mutation(ga, chromosome_set = None, gene_mutate_count = 1):
        
        gene_mutate_count_static = int(gene_mutate_count)

        if chromosome_set == None:
            chromosome_set = ga.population.get_all_chromosomes()

        for i in range(len(chromosome_set)):
            random_num = random.uniform(0,1)

            if (random_num <= ga.mutation_rate):
                while gene_mutate_count > 0:
                    dummy_population = ga.initialization_impl(ga) #Really inefficient, but works for now
                    random_index = random.randint(0, ga.chromosome_length-1)
                    chromosome_set[i].get_genes()[random_index] = dummy_population.get_all_chromosomes()[random.randint(0,ga.population_size-1)].get_genes()[random_index]
                    gene_mutate_count -= 1
            gene_mutate_count = int(gene_mutate_count_static)

        return chromosome_set

        
