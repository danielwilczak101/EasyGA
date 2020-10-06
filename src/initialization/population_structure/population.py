class Population:

    # fitness = Empty; population = [chromosome, chromosome, etc.]
    def __init__(self, chromosomes = None):
        if chromosomes is None:
          self.chromosome_list = []
        else:
          self.chromosome_list = chromosomes
        self.fitness = None
        self.mating_pool = []

    def get_closet_fitness(self,value):
        # Get the chomosome that has the closets fitness to the value defined
        pass

    def add_chromosome(self, chromosome, index = -1):
        if index == -1:
            index = len(self.chromosome_list)
        self.chromosome_list.insert(index, chromosome)

    def remove_chromosome(self, index):
        del self.chromosome_list[index]

    def get_all_chromosomes(self):
        """returns all chromosomes in the population"""
        return self.chromosome_list

    def get_fitness(self):
        return self.fitness

    def set_all_chromosomes(self, chromosomes):
        self.chromosome_list = chromosomes

    def set_chromosome(self, chromosome, index = -1):
        if index == -1:
            index = len(self.chromosomes)-1
        self.chromosome_list[index] = chromosome

    def set_fitness(self, fitness):
        self.fitness = fitness

    def __repr__(self):
        for index in range(len(self.chromosomes)):
            return f'{self.chromosome_list[index]}'

    def print_all(self):
        # Ex .Current population
        #     Chromosome 1 - [gene][gene][gene][.etc] /  Chromosome fitness - #
        print("Current population:")
        for index in range(len(self.chromosome_list)):
            print(f'Chromosome - {index} {self.chromosome_list[index]}', end = "")
            print(f' / Fitness = {self.chromosome_list[index].fitness}')