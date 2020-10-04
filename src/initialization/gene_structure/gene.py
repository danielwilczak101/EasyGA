def check_gene(value):
    #Check to make sure the gene is not empty
    assert value != "" , "Gene can not be empty"
    return value

class Gene:

    def __init__(self, value):
        self.fitness = None
        self.value = check_gene(value)

    def get_fitness(self):
        return self.fitness

    def get_value(self):
        return self.value

    def set_fitness(self, fitness):
        self.fitness = fitness

    def set_value(self, value):
        """Set value of the gene"""
        self.value = value

    def __repr__(self):
        return f'[{self.value}]'
