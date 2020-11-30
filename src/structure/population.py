from copy import deepcopy

class Population:

    def __init__(self, chromosome_list):
        """Initialize the population with fitness of value None, and a
        set of chromosomes dependant on user-passed parameter."""

        self.chromosome_list = [deepcopy(chromosome) for chromosome in chromosome_list]
        self.fitness = None
        self.mating_pool = []
        self.next_population = []


    def update(self):
        """Sets all the population variables to what they should be at
        the end of the generation """
        self.chromosome_list = self.next_population
        self.reset_mating_pool()
        self.reset_next_population()


    def reset_mating_pool(self):
        """Clears the mating pool"""
        self.mating_pool = []


    def reset_next_population(self):
        """Clears the next population"""
        self.next_population = []


    def remove_chromosome(self, index):
        """Removes and returns a chromosome from the indicated index from the population"""
        return self.chromosome_list.pop(index)


    def remove_parent(self, index):
        """Removes and returns a parent from the indicated index from the mating pool"""
        return self.mating_pool.pop(index)


    def remove_child(self, index):
        """Removes and returns a child from the indicated index from the next population"""
        return self.next_population.pop(index)


    def append_children(self, chromosome_list):
        """Appends a list of chromosomes to the next population.
        Appends to the front so that chromosomes with fitness
        values already will stay sorted.
        """

        if not isinstance(chromosome_list, list):
            chromosome_list = list(chromosome_list)
        self.next_population = chromosome_list + self.next_population


    def sort_by_best_fitness(self, ga):
        """Sorts the population by fitness"""
        ga.sort_by_best_fitness(self.chromosome_list, in_place = True)


    def add_chromosome(self, chromosome, index = None):
        """Adds a chromosome to the population at the input index,
        defaulted to the end of the chromosome set"""

        if index is None:
            index = len(self)
        self.chromosome_list.insert(index, chromosome)


    def add_parent(self, chromosome):
        """Adds a chromosome to the mating pool"""
        self.mating_pool.append(chromosome)


    def add_child(self, chromosome):
        """Adds a chromosome to the next population"""
        self.next_population.append(chromosome)


    def set_parent(self, index):
        """Sets the indexed chromosome from the population as a parent"""
        self.add_parent(self[index])


    def __iter__(self):
        """
        Allows the user to use

                iter(population)
                list(population) == population.chromosome_list
                tuple(population)
                for chromosome in population

        to loop through the population.
        """
        return iter(self.chromosome_list)


    def __getitem__(self, index):
        """
        Allows the user to use
                chromosome = population[index]
        to get the indexed chromosome.
        """
        return self.chromosome_list[index]


    def __setitem__(self, index, chromosome):
        """
        Allows the user to use
                population[index] = chromosome
        to set the indexed chromosome.
        """
        self.chromosome_list[index] = chromosome


    def __len__(self):
        """
        Allows the user to use
                size = len(population)
        to get the length of the population.
        """
        return len(self.chromosome_list)


    def __contains__(self, searched_chromosome):
        """
        Allows the user to use
                if chromosome in population
        to check if a chromosome is in the population.
        """
        return (searched_chromosome in self.chromosome_list)


    def index_of(self, searched_chromosome):
        """
        Allows the user to use
                index = population.index_of(chromosome)
        to find the index of a chromosome in the population.
        Be sure to check if the population contains the chromosome
        first, or to catch an exception if the chromosome is not
        in the population.
        """
        return self.chromosome_list.index(searched_chromosome)


    def __repr__(self):
        """
        Allows the user to use
                repr(population)
                str(population)
                print(population)
        to get a backend representation of the population.
        """
        return ''.join(
            f'Chromosome - {index} {chromosome} / Fitness = {chromosome.fitness}\n'
            for index, chromosome
            in enumerate(self)
        )
