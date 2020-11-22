from copy import deepcopy

class Gene:

    def __init__(self, value):
        """Initialize a gene with fitness of value None and the input value"""
        self.value = deepcopy(value)
        self.fitness = None


    def __repr__(self):
        """
        Allows the user to use
                repr(gene)
        to get a backend representation of the gene.
        """
        return str(self.value)


    def __str__(self):
        """
        Allows the user to use
                str(gene)
                print(gene)
        to get a frontend representation of the gene.
        """
        return f'[{str(self.value)}]'
