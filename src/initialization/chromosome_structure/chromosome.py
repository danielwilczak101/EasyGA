class Chromosome:

    def __init__(self, genes = None):
        if genes is None:
            self.gene_list = []
        else:
            self.gene_list = genes
        self.fitness = None

    def add_gene(self, gene, index = -1):
        if index == -1:
            index = len(self.gene_list)
        self.gene_list.insert(index, gene)

    def remove_gene(self, index):
        del self.gene_list[index]

    def get_genes(self):
        return self.gene_list

    def get_fitness(self):
        return self.fitness

    def set_gene(self, gene, index):
        self.gene_list[index] = gene

    def set_genes(self, genes):
        self.gene_list = genes

    def set_fitness(self, fitness):
        self.fitness = fitness

    def __repr__(self):
        output_str = ''
        for gene in self.gene_list:
            output_str += gene.__repr__()
        return output_str
