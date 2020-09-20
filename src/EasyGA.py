def check_gene(value):
    assert value != "" , "Gene can not be empty"
    return value


## Your main structure
class gene:
    # Defults
        # fitness = double , value = Anything
    def __init__(self, value):
        self.fitness = None
        self.value = check_gene(value)

    def get_fitness(self):
        return self.fitness

    def set_fitness(self,fitness):
        self.fitness = fitness

    def get_value(self):
        return self.value

    # Should the gene creation of the genes veriation be
    # included in the gene class or should the use just
    # assign value to the gene and we move on?

class chromosome:
    # Defults
        # fitness = double, genes = [gene,gene,gene,etc]
    def __init__(self):
        self.fitness = None
        self.genes = []

    def get_fitness(self):
        return self.score

    def add_gene(self,gene):
        self.genes.append(gene)

class population:
    # chromosomes = [chromosome,chromosome,etc]
    def __init__(self, chromosome):
        self.chromosomes = []

class ga:
    pass
