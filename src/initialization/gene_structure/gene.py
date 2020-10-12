def check_gene(value):
    #Check to make sure the gene is not empty
    assert value != "" , "Gene can not be empty"
    return value


class Gene:

    def __init__(self, value):
        """Initialize a gene with fitness of value None and the input value"""
        self.fitness = None
        self.value = check_gene(value)


    def get_fitness(self):
        """Return fitness of the gene"""
        return self.fitness


    def get_value(self):
        """Return value of the gene"""
        return self.value


    def set_fitness(self, fitness):
        """Set fitness of the gene"""
        self.fitness = fitness


    def set_value(self, value):
        """Set value of the gene"""
        self.value = value


    def __repr__(self):
        """Format the repr() output value"""
        return f'[{self.value}]'
