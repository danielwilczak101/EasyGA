class population:

    def __init__(self, chromosomes = None):
        """Intiialize the population with fitness of value None, and a set of chromosomes dependant on user-passed parameter"""
        if chromosomes is None:
          self.chromosomes = []
        else:
          self.chromosomes = chromosomes
        self.fitness = None

    def get_closet_fitness(self,value):
        """Get the chomosome that has the closets fitness to the value defined"""
        pass

    def add_chromosome(self, chromosome, index = -1):
        """Adds a chromosome to the population at the input index, defaulted to the end of the chromosome set"""
        if index == -1:
            index = len(self.chromosomes)
        self.chromosomes.insert(index, chromosome)

    def remove_chromosome(self, index):
        """removes a chromosome from the indicated index"""
        del self.chromosomes[index]

    def get_all_chromosomes(self):
        """returns all chromosomes in the population"""
        return chromosomes

    def get_fitness(self):
        """returns the population's fitness"""
        return self.fitness

    def set_all_chromosomes(self, chromosomes):
        """sets the chromosome set of the population"""
        self.chromosomes = chromosomes

    def set_chromosome(self, chromosome, index):
        """sets a specific chromosome at a specific index"""
        self.chromosomes[index] = chromosome

    def set_fitness(self, fitness):
        """Sets the fitness value of the population""" 
        self.fitness = fitness

    def __repr__(self):
        """Sets the repr() output format"""
        return ''.join([chromosome.__repr__() for chromosome in self.chromosomes])

    def print_all(self):
        """Prints information about the population in the following format:"""
        """Ex .Current population"""
        """Chromosome 1 - [gene][gene][gene][.etc] /  Chromosome fitness - """
        print("Current population:")
        for index in range(len(self.chromosomes)):
            print(f'Chromosome - {index} {self.chromosomes[index]}', end = "")
            print(f' / Fitness = {self.chromosomes[index].fitness}')
