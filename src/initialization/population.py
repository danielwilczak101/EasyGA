class population:
    # population = [chromosome,chromosome,etc]
    def __init__(self):
        self.chromosomes = []
        self.fitness = None

    def add_chromosome(self,chromosome):
        self.chromosomes.append(chromosome)
