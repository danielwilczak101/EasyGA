class population:
    # population = [chromosome,chromosome,etc]
    def __init__(self):
        self.fitness = None
        self.chromosomes = []
        
    def add_chromosome(self,chromosome):
        self.chromosomes.append(chromosome)
