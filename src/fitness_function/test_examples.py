class test_fitness_funciton:
    def get_fitness(self, chromosome):
        # For every gene in chromosome
        for i in range(len(chromosome.genes)):
            # If the gene has a five then add one to the fitness
            # Example -> Chromosome = [5],[2],[2],[5],[5] then fitness = 3
            if (chromosome.genes[i].get_value == 5):
                # Add to the genes fitness
                chromosome.genes[i].fitness += 1
                # Add to the chromosomes fitness
                chromosome.fitness += 1
        return chromosome.fitness
