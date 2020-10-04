import random

class Mutation_Types:
    
    def __init__(self):
        pass

    def random_mutation(self, ga, chromosome_set = None):
        
        if chromosome_set == None:
            chromosome_set = ga.population

        chromosome_mutate_num = int(len(chromosome_set)*ga.mutation_rate)
        temp_population = ga.initialization_impl(ga)

        while chromosome_mutate_num > 0:
            chromosome_set[random.randint(0,ga.population_size-1)] = temp_population.get_all_chromosomes()[chromosome_mutate_num]
            chromosome_mutate_num -= 1
        
        return chromosome_set
        
