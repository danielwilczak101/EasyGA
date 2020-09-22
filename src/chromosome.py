class chromosome:
    # fitness = Empty, genes = [gene,gene,gene,etc]
    def __init__(self):
        self.fitness = None
        self.genes = []

    def add_gene(self,gene):
        self.genes.append(gene)

    def get_fitness(self):
        return self.fitness

    def get_chromosome(self):
        return self.genes

    def print_chromosome(self):
        for i in range(len(self.genes)):
            # Print the gene one by one.
            if(i == len(self.genes) - 1):
                print(f"[{self.genes[i].get_value()}]")
            else:
                print(f"[{self.genes[i].get_value()}],", end = '')
