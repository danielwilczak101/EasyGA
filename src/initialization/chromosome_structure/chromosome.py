class Chromosome:
    def __init__(self, gene_list = None):
        if gene_list is None:
            self.gene_list = []
        else:
            self.gene_list = gene_list

        self.fitness = None
        # If the chromosome has been selected then the flag would switch to true
        self.selected = False

    def add_gene(self, gene, index = -1):
        """Add a gene to the chromosome at the specified index, defaulted to end of the chromosome"""
        if index == -1:
            index = len(self.gene_list)
        self.gene_list.insert(index, gene)

    def remove_gene(self, index):
        del self.gene_list[index]

    def get_genes(self):
        return self.gene_list

    def get_fitness(self):
        """Return the fitness of the chromosome"""
        return self.fitness

    def set_gene(self, gene, index):
        self.gene_list[index] = gene

    def set_genes(self, genes):
        self.gene_list = genes

    def set_fitness(self, fitness):
        """Set the fitness value of the chromosome"""
        self.fitness = fitness

    def __repr__(self):
        """Format the repr() output for the chromosome"""
        output_str = ''
        for gene in self.gene_list:
            output_str += gene.__repr__()
        return output_str
