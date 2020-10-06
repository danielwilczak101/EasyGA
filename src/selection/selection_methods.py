import random
from initialization.chromosome_structure.chromosome import Chromosome as create_chromosome
from initialization.gene_structure.gene import Gene as create_gene
from initialization.population_structure.population import Population
from initialization.chromosome_structure.chromosome import Chromosome

class Selection_Methods:
    """Selection is the process by which chromosomes are selected for crossover and eventually, influence the next generation of chromosomes."""
    def __init__(self):
        pass

    class Parent_Selection:
        class Tournament:
            def with_replacement(self, ga):
                tournament_size = int(len(ga.population.get_all_chromosomes())*ga.parent_ratio/10)
                if tournament_size < 3:
                    tournament_size = int(len(ga.population.get_all_chromosomes())*ga.parent_ratio/3)
                
                # Probability used for determining if a chromosome should enter the mating pool.
                selection_probability = 0.95
                
                # Repeat tournaments until the mating pool is large enough.
                while (len(ga.population.mating_pool) < len(ga.population.get_all_chromosomes())*ga.parent_ratio):
                    
                    # Generate a random tournament group and sort by fitness.
                    tournament_group = ga.sort_by_best_fitness([random.choice(ga.population.get_all_chromosomes()) for n in range(tournament_size)])
                    
                    # For each chromosome, add it to the mating pool based on its rank in the tournament.
                    for index in range(tournament_size):
                        # Probability required is selection_probability * (1-selection_probability) ^ (tournament_size-index+1)
                        # e.g. top ranked fitness has probability: selection_probability
                        #   second ranked fitness has probability: selection_probability * (1-selection_probability)
                        #   third  ranked fitness has probability: selection_probability * (1-selection_probability)^2
                        # etc.
                        if random.uniform(0, 1) < selection_probability * pow(1-selection_probability, index+1):
                            ga.population.mating_pool.append(tournament_group[index])

        class Roulette:
            def roulette_selection(self, ga):
                """Roulette selection works based off of how strong the fitness is of the
                chromosomes in the population. The stronger the fitness the higher the probability
                that it will be selected. Using the example of a casino roulette wheel.
                Where the chromosomes are the numbers to be selected and the board size for
                those numbers are directly proportional to the chromosome's current fitness. Where
                the ball falls is a randomly generated number between 0 and 1"""
                total_fitness = sum(ga.population.chromosome_list[i].get_fitness() for i in range(len(ga.population.chromosome_list)))
                rel_fitnesses = []
        
                for chromosome in ga.population.chromosome_list:
                    if (total_fitness != 0):
                        rel_fitnesses.append(float(chromosome.fitness)/total_fitness)
                
                probability = [sum(rel_fitnesses[:i+1]) for i in range(len(rel_fitnesses))]
        
                while (len(ga.population.mating_pool) < len(ga.population.get_all_chromosomes())*ga.parent_ratio):
                    rand_number = random.random()
        
                    # Loop through the list of probabilities
                    for i in range(len(probability)):
                        # If the probability is greater than the random_number, then select that chromosome
                        if (probability[i] >= rand_number):
                            ga.population.mating_pool.append(ga.population.chromosome_list[i])
                            # print (f'Selected chromosome : {i}')
                            break

    class Survivor_Selection:
        def repeated_crossover(self, ga, next_population): #Might be cheating? I don't know honestly - RG
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
    
        def remove_two_worst(self, ga, next_population):
            iterator = 0
            while len(next_population.get_all_chromosomes()) < ga.population_size:
                next_population.add_chromosome(ga.population.get_all_chromosomes()[iterator])
                iterator += 1
            return next_population
