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
                tournament_size = int(len(ga.population.get_all_chromosomes())/10) #currently hard-coded for purposes of the example.
                if tournament_size < 3:
                    tournament_size = int(len(ga.population.get_all_chromosomes())/3)
                parent_ratio = 0.25

                #selection_probability is the likelihood that a chromosome will be selected.
                #best chromosome in a tournament is given a selection probablity of selection_probability
                #2nd best is given probability of selection_probability*(1-selection_probability)
                #3rd best is given probability of selection_probability*(1-selection_probability)**2
                selection_probability = 0.95
                total_selected = 0 #Total Chromosomes selected

                while (total_selected < parent_ratio*ga.population_size):
                    #create & gather tournament group
                    tournament_group = []

                    for i in range(tournament_size):
                        tournament_group.append(random.choice(ga.population.get_all_chromosomes()))
                    
                    #Sort the tournament contenders based on their fitness
                    #currently hard-coded to only consider higher fitness = better; can be changed once this impl is agreed on
                    #also currently uses bubble sort because its easy
                    tournament_group_temp = tournament_group
                    not_sorted_check = 0
                    while (not_sorted_check != len(tournament_group_temp)):
                        not_sorted_check = 0
                        for i in range(len(tournament_group_temp)):
                            if ((i + 1 < len(tournament_group_temp)) and (tournament_group_temp[i + 1].fitness > tournament_group_temp[i].fitness)):
                                temp = tournament_group[i]
                                tournament_group_temp[i] = tournament_group[i + 1]
                                tournament_group_temp[i + 1] = temp
                            else:
                                not_sorted_check += 1

                    tournament_group = tournament_group_temp

                    #After sorting by fitness, randomly select a chromosome based on selection_probability
                    selected_chromosome_tournament_index = 0
                    for i in range(tournament_size):
                        random_num = random.uniform(0,1)

                        #ugly implementation but its functional
                        if i == 0:
                            if random_num <= selection_probability:
                                tournament_group[i].selected = True
                                total_selected += 1
                                selected_chromosome_tournament_index = i
                                break
                        else:
                            if random_num <= selection_probability*((1-selection_probability)**(i-1)):
                                tournament_group[i].selected = True
                                total_selected += 1
                                selected_chromosome_tournament_index = i
                                break

    class Survivor_Selection:
        def repeated_crossover(self, ga, next_population): #Might be cheating? I don't know honestly - RG
            while len(next_population.get_all_chromosomes()) < ga.population_size:
                crossover_pool = []
                for i in range(ga.population_size):
                    if ga.population.get_all_chromosomes()[i].selected:
                        crossover_pool.append(ga.population.get_all_chromosomes()[i])

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

            #Bubble sorting by highest fitness
            temp_population = ga.population
            not_sorted_check = 0
            while (not_sorted_check != len(temp_population.get_all_chromosomes())):
                not_sorted_check = 0
                for i in range(len(temp_population.get_all_chromosomes())):
                    if ((i + 1 < len(temp_population.get_all_chromosomes())) and (temp_population.get_all_chromosomes()[i + 1].fitness > temp_population.get_all_chromosomes()[i].fitness)):
                        temp = temp_population.get_all_chromosomes()[i]
                        temp_population.get_all_chromosomes()[i] = ga.population.get_all_chromosomes()[i + 1]
                        temp_population.get_all_chromosomes()[i + 1] = temp
                    else:
                        not_sorted_check += 1

            iterator = 0
            while len(next_population.get_all_chromosomes()) < ga.population_size:
                next_population.add_chromosome(temp_population.get_all_chromosomes()[iterator])
                iterator += 1
            return next_population

    def roulette_selection(self, ga):
        """Roulette selection works based off of how strong the fitness is of the
        chromosomes in the population. The stronger the fitness the higher the probability
        that it will be selected. Using the example of a casino roulette wheel.
        Where the chromosomes are the numbers to be selected and the board size for
        those numbers are directly proportional to the chromosome's current fitness. Where
        the ball falls is a randomly generated number between 0 and 1"""
        pass
