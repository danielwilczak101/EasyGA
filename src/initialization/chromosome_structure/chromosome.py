class chromosome:
    
    def __init__(self, genes = None):
        """Initialize the chromosome based on input gene list, defaulted to an empty list"""
        if genes is None:
            self.genes = []
        else:
            self.genes = genes
        self.fitness = None

    def add_gene(self, gene, index = -1):
        """Add a gene to the chromosome at the specified index, defaulted to end of the chromosome"""
        if index == -1:
            index = len(self.genes)
        self.genes.insert(index, gene)

    def remove_gene(self, index):
        """Remove a gene from the chromosome at the specified index"""
        del self.genes[index]

    def get_genes(self):
        """Return all genes in the chromosome"""
        return self.genes

    def get_fitness(self):
        """Return the fitness of the chromosome"""
        return self.fitness

    def set_gene(self, gene, index):
        """Set a gene at a specific index"""
        self.genes[index] = gene

    def set_genes(self, genes):
        """Set the entire gene set of the chromosome"""
        self.genes = genes

    def set_fitness(self, fitness):
        """Set the fitness value of the chromosome"""
        self.fitness = fitness

    def __repr__(self):
        """Format the repr() output for the chromosome"""
        output_str = ''
        for gene in self.genes:
            output_str += gene.__repr__()
        return output_str
