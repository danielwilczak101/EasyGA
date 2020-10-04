import random
from initialization.chromosome_structure.chromosome import Chromosome as create_chromosome
from initialization.gene_structure.gene import Gene as create_gene
from initialization.population_structure.population import Population
from initialization.chromosome_structure.chromosome import Chromosome

class Selection_Types:
    """Selection is the process by which chromosomes are selected for crossover and eventually, influence the next generation of chromosomes."""
    def __init__(self):
        pass

    def tournament_selection(self, ga):
        """This example currently uses a 'with replacement' approach (chromosomes are placed back into the pool after participating)"""
        tournament_size = int(len(ga.population.get_all_chromosomes())/10) #currently hard-coded for purposes of the example.

        #selection_probability is the likelihood that a chromosome will be selected.
        #best chromosome in a tournament is given a selection probablity of selection_probability
        #2nd best is given probability of selection_probability*(1-selection_probability)
        selection_probability = 0.95
        total_selected = 0 #Total Chromosomes selected

        while (total_selected <= ga.population_size*2):
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
            for i in range(tournament_size):
                random_num = random.uniform(0,1)

                #ugly implementation but its functional
                if i == 0:
                    if random_num <= selection_probability:
                        tournament_group[i].selected = True
                        total_selected += 1
                        break
                else:
                    if random_num <= selection_probability*((1-selection_probability)**(i-1)):
                        tournament_group[i].selected = True
                        total_selected += 1
                        break


        new_population = ga.crossover_impl(ga)

        #If the crossover doesn't create enough chromosomes (ugly right now pls no judgerino, can be changed)
        #Just does single-point crossover at random indices
        while len(new_population.chromosomes) < ga.population_size:
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
                    new_chromosome = Chromosome(new_gene_set)
                    chromosome_list.append(new_chromosome)

            for i in range(len(chromosome_list)):
                new_population.add_chromosome(chromosome_list[i])
                if len(new_population.chromosomes) >= ga.population_size:
                    break
        
        new_chromosome_set = ga.mutation_impl(ga, new_population.get_all_chromosomes())
        new_population.set_all_chromosomes(new_chromosome_set)

        return new_population



    def roulette_selection(self, ga):
        """Roulette selection works based off of how strong the fitness is of the
        chromosomes in the population. The stronger the fitness the higher the probability
        that it will be selected. Using the example of a casino roulette wheel.
        Where the chromosomes are the numbers to be selected and the board size for
        those numbers are directly proportional to the chromosome's current fitness. Where
        the ball falls is a randomly generated number between 0 and 1"""
        pass
