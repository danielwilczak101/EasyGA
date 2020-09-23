def check_gene(value):
    #Check to make sure the gene is not empty
    assert value != "" , "Gene can not be empty"
    return value

class gene:
    # fitness = Empty, value = Define by gene function
    def __init__(self, value):
        self.fitness = None
        self.value = check_gene(value)

    def set_fitness(self,fitness):
        self.fitness = fitness

    def get_fitness(self):
        return self.fitness

    def get_value(self):
        return self.value

    def print_value(self):
        print(self.value)

    def print_fitness(self):
        print(self.fitness)
