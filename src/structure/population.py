from copy import deepcopy

class Population:

    def __init__(self, chromosome_list = []):
        """Initialize the population with fitness of value None, and a
        set of chromosomes dependant on user-passed parameter."""

        self.chromosome_list = deepcopy(chromosome_list)
        self.fitness = None
        self.mating_pool = []
        self.next_population = []


    def update(self):
        """Sets all the population variables to what they should be at
        the end of the generation """
        self.set_chromosome_list(self.next_population)
        self.reset_mating_pool()
        self.reset_next_population()


    def remove_chromosome(self, index):
        """Removes a chromosome from the indicated index from the population"""
        del self.chromosome_list[index]


    def remove_parent(self, index):
        """Removes a parent from the indicated index from the mating pool"""
        del self.mating_pool[index]


    def remove_child(self, index):
        """Removes a child from the indicated index from the next population"""
        del self.next_population[index]


    def reset_mating_pool(self):
        """Clears the mating pool"""
        self.mating_pool = []


    def reset_next_population(self):
        """Clears the next population"""
        self.next_population = []


    def append_children(self, chromosome_list):
        """Appends a list of chromosomes to the next population"""
        self.next_population += chromosome_list


    def sort_by_best_fitness(self, ga):
        """Sorts the population by fitness"""
        self.set_chromosome_list(ga.sort_by_best_fitness(self.chromosome_list))


    def size(self):
        """Returns the size of the population"""
        return len(self.chromosome_list)


    def total_children(self):
        """Returns the size of the next population"""
        return len(self.next_population)


    def get_closet_fitness(self,value):
        """Get the chomosome that has the closets fitness to the value defined"""
        pass


    def add_chromosome(self, chromosome, index = None):
        """Adds a chromosome to the population at the input index, defaulted
         to the end of the chromosome set"""

        if index is None:
            index = self.size()
        self.chromosome_list.insert(index, chromosome)


    def add_parent(self, chromosome):
        """Adds a chromosome to the mating pool"""
        self.mating_pool.append(chromosome)


    def add_child(self, chromosome):
        """Adds a chromosome to the next population"""
        self.next_population.append(chromosome)


    def get_chromosome(self, index):
        """Returns the chromosome at the given index in the population"""
        return self.chromosome_list[index]


    def get_parent(self, index):
        """Returns the parent at the given index in the mating pool"""
        return self.mating_pool[index]


    def get_child(self, index):
        """Returns the child at the given index in the next population"""
        return self.next_population[index]


    def get_chromosome_list(self):
        """Returns all chromosomes in the population"""
        return self.chromosome_list


    def get_mating_pool(self):
        """Returns chromosomes in the mating pool"""
        return self.mating_pool


    def get_next_population(self):
        """Returns chromosomes in the next population"""
        return self.next_population


    def get_fitness(self):
        """Returns the population's fitness"""
        return self.fitness


    def set_chromosome_list(self, chromosome_list):
        """Sets the chromosome list"""
        self.chromosome_list = chromosome_list


    def set_mating_pool(self, chromosome_list):
        """Sets entire mating pool"""
        self.mating_pool = chromosome_list


    def set_chromosome(self, chromosome, index):
        """Sets the chromosome at the given index"""
        self.chromosome_list[index] = chromosome


    def set_parent(self, index):
        """Sets the indexed chromosome from the population as a parent"""
        self.add_parent(self.get_chromosome(index))


    def set_fitness(self, fitness):
        """Sets the fitness value of the population"""
        self.fitness = fitness


    def __repr__(self):
        """Returns a backend string representation of the entire population"""
        return ''.join(
                f'Chromosome - {index} {self.get_chromosome(index)} ' + 
                f'/ Fitness = {self.get_chromosome(index).get_fitness()}\n'
            for index in range(self.size())
        )
