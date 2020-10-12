import random
from initialization.chromosome_structure.chromosome import Chromosome as create_chromosome
from initialization.gene_structure.gene import Gene as create_gene
from initialization.population_structure.population import Population
from initialization.chromosome_structure.chromosome import Chromosome

class Parent_Selection:
    class Tournament:
        def with_replacement(ga):
            """
            Will make tournaments of size tournament_size and choose the winner (best fitness) from the tournament and use it as a parent for the next generation
            The total number of parents selected is determined by parent_ratio, an attribute to the GA object.
            """
            
            tournament_size = int(ga.population.size()*ga.tournament_size_ratio)
            if tournament_size < 5:
                tournament_size = 5
            # Probability used for determining if a chromosome should enter the mating pool.
            selection_probability = ga.selection_probability
            
            # Repeat tournaments until the mating pool is large enough.
            while (len(ga.population.mating_pool) < ga.population.size()*ga.parent_ratio):
                # Generate a random tournament group and sort by fitness.
                tournament_group = ga.sort_by_best_fitness([random.choice(ga.population.get_all_chromosomes()) for n in range(tournament_size)])
                
                # For each chromosome, add it to the mating pool based on its rank in the tournament.
                for index in range(tournament_size):
                    # Probability required is selection_probability * (1-selection_probability) ^ (tournament_size-index+1)
                    # e.g. top ranked fitness has probability: selection_probability
                    #   second ranked fitness has probability: selection_probability * (1-selection_probability)
                    #   third  ranked fitness has probability: selection_probability * (1-selection_probability)^2
                    # etc.
                    if random.uniform(0, 1) < selection_probability * pow(1-selection_probability, index):
                        ga.population.mating_pool.append(tournament_group[index])

    class Roulette:
        def roulette_selection(ga):
            """Roulette selection works based off of how strong the fitness is of the
            chromosomes in the population. The stronger the fitness the higher the probability
            that it will be selected. Using the example of a casino roulette wheel.
            Where the chromosomes are the numbers to be selected and the board size for
            those numbers are directly proportional to the chromosome's current fitness. Where
            the ball falls is a randomly generated number between 0 and 1"""
            total_fitness = sum(ga.population.chromosome_list[i].get_fitness() for i in range(ga.population.size()))
            rel_fitnesses = []
    
            for chromosome in ga.population.chromosome_list:
                if (total_fitness != 0):
                    rel_fitnesses.append(float(chromosome.fitness)/total_fitness)
            
            probability = [sum(rel_fitnesses[:i+1]) for i in range(len(rel_fitnesses))]
    
            while (len(ga.population.mating_pool) < ga.population.size()*ga.parent_ratio):
                rand_number = random.random()
    
                # Loop through the list of probabilities
                for i in range(len(probability)):
                    # If the probability is greater than the random_number, then select that chromosome
                    if (probability[i] >= rand_number):
                        ga.population.mating_pool.append(ga.population.chromosome_list[i])
                        # print (f'Selected chromosome : {i}')
                        break