from structure import Chromosome as make_chromosome
from itertools import chain

def to_chromosome(chromosome):
    """Converts the input to a chromosome if it isn't already one."""

    if isinstance(chromosome, make_chromosome):
        return chromosome
    else:
        return make_chromosome(chromosome)


class Population:

    def __init__(self, chromosome_list):
        """Initialize the population with a collection
        of chromosomes dependant on user-passed parameter."""

        self.chromosome_list = [make_chromosome(chromosome) for chromosome in chromosome_list]
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
        """Appends a list of chromosomes to the next population."""

        self.next_population += (
            to_chromosome(chromosome)
            for chromosome
            in chromosome_list
        )


    def add_chromosome(self, chromosome, index = None):
        """Adds a chromosome to the population at the input index,
        defaulted to the end of the chromosome set"""

        if index is None:
            index = len(self)
        self.chromosome_list.insert(index, to_chromosome(chromosome))


    def add_parent(self, chromosome):
        """Adds a chromosome to the mating pool"""
        self.mating_pool.append(to_chromosome(chromosome))


    def add_child(self, chromosome):
        """Adds a chromosome to the next population"""
        self.next_population.append(to_chromosome(chromosome))


    def set_parent(self, index):
        """Sets the indexed chromosome from the population as a parent"""
        self.add_parent(self[index])


    #==================================================#
    # Magic-Dunder Methods replicating list structure. #
    #==================================================#


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

        # Just one chromosome
        if isinstance(index, int):
            self.chromosome_list[index] = to_chromosome(chromosome)

        # Multiple chromosomes
        else:
            self.chromosome_list[index] = [to_chromosome(item) for item in chromosome]


    def __delitem__(self, index):
        """
        Allows the user to use
                del population[index]
        to delete a chromosome at the specified index.
        """
        del self.chromosome_list[index]


    def __len__(self):
        """
        Allows the user to use
                size = len(population)
        to get the length of the population.
        """
        return len(self.chromosome_list)


    def __contains__(self, chromosome):
        """
        Allows the user to use
                if chromosome in population
        to check if a chromosome is in the population.
        """
        return (to_chromosome(chromosome) in self.chromosome_list)


    def __eq__(self, population):
        """Returns self == population, True if all chromosomes match."""
        return self.chromosome_list == population.chromosome_list


    def __add__(self, population):
        """Returns self + population, a population made by concatenating the chromosomes."""
        return Population(chain(self, population))


    def __iadd__(self, population):
        """Implement self += population by concatenating the new chromosomes."""
        self.chromosome_list += (to_chromosome(chromosome) for chromosome in population)


    def append(self, chromosome):
        """Append chromosome to the end of the population."""
        self.chromosome_list.append(to_chromosome(chromosome))


    def clear(self):
        """Remove all chromosomes from the population."""
        self.chromosome_list = []


    def copy(self):
        """Return a copy of the population."""
        return Population(self)


    def count(self, chromosome):
        """Return number of occurrences of the chromosome in the population."""
        return self.chromosome_list.count(to_chromosome(chromosome))


    def index(self, chromosome, guess = None):
        """
        Allows the user to use
                index = population.index(chromosome)
                index = population.index(chromosome, guess)
        to find the index of a chromosome in the population.

        If no guess is given, it finds the index of the first match.
        If a guess is given, it finds index of the nearest match.
        """

        chromosome = to_chromosome(chromosome)

        # Use built-in method
        if guess is None:
            return self.chromosome_list.index(chromosome)

        # Use symmetric mod
        guess %= len(self)
        if guess >= len(self)//2:
            guess -= len(self)

        # Search outwards for the chromosome
        for i in range(len(self)//2):

            # Search to the left
            if chromosome == self[guess-i]:
                return (guess-i) % len(self)

            # Search to the right
            elif chromosome == self[guess+i]:
                return (guess+i) % len(self)

        # Chromosome not found
        raise IndexError("No such chromosome in the population found")


    def insert(self, index, chromosome):
        """Insert chromosome so that self[index] == chromsome."""
        self.chromosome_list.insert(index, to_chromosome(chromosome))


    def pop(self, index = -1):
        """Remove and return chromosome at index (default last).

        Raises IndexError if population is empty or index is out of range.
        """
        return self.chromosome_list.pop(index)


    def remove(self, chromosome):
        """Remove first occurrence of chromosome.

        Raises ValueError if the chromosome is not present.
        """
        self.chromosome_list.remove(to_chromosome(chromosome))


    def sort(self, *, key = lambda chromosome: chromosome.fitness, reverse):
        """Sorts the population."""
        self.chromosome_list.sort(
            key = key,
            reverse = reverse
        )


    def __repr__(self):
        """
        Allows the user to use
                population_string = repr(population)
                population_data   = eval(population_string)
                population        = ga.make_population(population_data)
        to get a backend representation of the population
        which can be evaluated directly as code to create
        the population.
        """
        return repr(self.chromosome_list)


    def __str__(self):
        """
        Allows the user to use
                str(population)
                print(population)
        to get a frontend representation of the population.
        """
        return ''.join(
            f'Chromosome - {index} {chromosome} / Fitness = {chromosome.fitness}\n'
            for index, chromosome
            in enumerate(self)
        )
