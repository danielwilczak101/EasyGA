<<<<<<< Updated upstream
class chromosome:
    
    # fitness = Empty; genes = [gene, gene, gene, etc.]
=======
class Chromosome:

>>>>>>> Stashed changes
    def __init__(self, genes = None):
        if genes is None:
            self.genes = []
        else:
            self.genes = genes
        self.fitness = None

    def add_gene(self, gene, index = -1):
        if index == -1:
            index = len(self.genes)
        self.genes.insert(index, gene)

    def remove_gene(self, index):
        del self.genes[index]

    def get_genes(self):
        return self.genes

    def get_fitness(self):
        return self.fitness

    def set_gene(self, gene, index):
        self.genes[index] = gene

    def set_genes(self, genes):
        self.genes = genes

    def set_fitness(self, fitness):
        self.fitness = fitness

    def __repr__(self):
        output_str = ''
        for gene in self.genes:
            output_str += gene.__repr__()
        return output_str
