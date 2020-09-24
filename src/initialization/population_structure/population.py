class population:
    # population = [chromosome,chromosome,etc]
    def __init__(self, chromosomes = []):
        self.chromosomes = chromosomes
        self.fitness = None

    def get_closet_fitness(self,value):
        # Get the chomosome that has the closets fitness to the value defined
        pass

    def add_chromosome(self, chromosome, index = -1):
        if index == -1:
            index = len(self.chromosomes) - 1
        self.chromosomes.insert(index, chromosome)

    def remove_chromosome(self, index):
        del self.chromosomes[index]

    def get_all_chromosomes(self):
        return chromosomes

    def get_fitness(self):
        return self.fitness

    def set_all_chromosomes(self, chromosomes):
        self.chromosomes = chromosomes

    def set_chromosome(self, chromosomes, index):
        self.chromosome[index] = chromosome

    def set_fitness(self, fitness):
        self.fitness = fitness

    def __repr__(self):
        return f"population({self.chromosomes.__repr__()})"

    def generate_first_chromosomes(self, chromosome_count, chromosome_length, gene_lower_bound, gene_upper_bound):
        #Creating the chromosomes with Genes of random size
        for x in range(chromosome_count):
            chromosome = Chromosome(chromosome_length)
            for y in range(chromosome_length):
                chromosome.gene_set[y] = Gene(random.randint(gene_lower_bound[y], gene_upper_bound[y]))
            self.chromosome_set.append(chromosome)
