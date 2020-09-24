class chromosome:
    # fitness = Empty, genes = [gene,gene,gene,etc]
    def __init__(self, genes = []):
        self.genes = genes
        self.fitness = None

    def add_gene(self, gene, index = -1):
        if index == -1:
            index = len(self.genes) - 1
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
        return f"chromosome({self.genes.__repr__()})"
