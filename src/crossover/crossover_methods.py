import random

def append_to_next_population(population_method):
    """Appends the new chromosomes to the next population.
    Also modifies the input to include the mating pool.
    """

    return lambda ga:\
        ga.population.append_children(
            population_method(ga, ga.population.mating_pool)
        )


def genes_to_chromosome(individual_method):
    """Converts a collection of genes into a chromosome.
    Note: Will recreate the gene list if given gene list.
          Built-in methods do not construct gene lists
          and use yield for efficiency.
    """

    return lambda ga, parent_1, parent_2, weight:\
        ga.make_chromosome(
            individual_method(ga, parent_1, parent_2, weight)
        )


def values_to_genes(individual_method):
    """Converts a collection of values into genes.
    Returns a generator of genes to avoid storing a new list.
    """

    return lambda ga, parent_1, parent_2, weight:\
        (
            ga.make_gene(value)
            for value
            in individual_method(ga, parent_1, parent_2, weight)
        )


class Crossover_Methods:

    # Private method decorators, see above.
    _append_to_next_population = append_to_next_population
    _genes_to_chromosome       = genes_to_chromosome
    _values_to_genes           = values_to_genes


    class Population:
        """Methods for selecting chromosomes to crossover."""


        @append_to_next_population
        def sequential_selection(ga, mating_pool):
            """Select sequential pairs from the mating pool.
            Every parent is paired with the previous parent.
            The first parent is paired with the last parent.
            """

            for index in range(len(mating_pool)):    # for each parent in the mating pool
                yield ga.crossover_individual_impl(  #     apply crossover to
                    ga,                              # 
                    mating_pool[index],              #         the parent and
                    mating_pool[index-1],            #         the previous parent
                    0.5                              #         with equal weight
                )


        @append_to_next_population
        def random_selection(ga, mating_pool):
            """Select random pairs from the mating pool.
            Every parent is paired with a random parent.
            """

            for parent in mating_pool:               # for each parent in the mating pool
                yield ga.crossover_individual_impl(  #     apply crossover to
                    ga,                              # 
                    parent,                          #         the parent and
                    random.choice(mating_pool),      #         a random parent
                    0.5                              #         with equal weight
                )


    class Individual:
        """Methods for crossing parents."""


        @genes_to_chromosome
        def single_point(ga, parent_1, parent_2, weight = 0.5):
            """Cross two parents by swapping genes at one random point."""

            N = min(len(parent_1), len(parent_2))

            if weight == 0.5:
                swap_index = random.randrange(N)
            else:
                weights = [
                    weight*n + (1-weight)*(N-n)
                    for n
                    in range(N)
                ]
                swap_index = random.choices(range(N), weights)[0]

            return parent_1[:swap_index] + parent_2[swap_index:]


        @genes_to_chromosome
        def multi_point(ga, parent_1, parent_2, weight = 0.5):
            """Cross two parents by swapping genes at multiple points."""
            pass


        @genes_to_chromosome
        def uniform(ga, parent_1, parent_2, weight = 0.5):
            """Cross two parents by swapping all genes randomly."""

            for gene_pair in zip(parent_1, parent_2):
                yield random.choice(gene_pair, [weight, 1-weight])


        class Arithmetic:
            """Crossover methods for numerical genes."""

            @genes_to_chromosome
            @values_to_genes
            def random(ga, parent_1, parent_2, weight = 0.5):
                """Cross two parents by taking a random integer or float value between each of the genes."""

                values_1 = parent_1.gene_value_iter
                values_2 = parent_2.gene_value_iter

                for value_1, value_2 in zip(values_1, values_2):

                    value = weight*values_1 + (1-weight)*random.uniform(value_1, value_2)

                    if type(value_1) == type(value_2) == int:
                        value = round(value)

                    yield value


            @genes_to_chromosome
            @values_to_genes
            def average(ga, parent_1, parent_2, weight = 0.5):
                """Cross two parents by taking the average of the genes."""

                values_1 = parent_1.gene_value_iter
                values_2 = parent_2.gene_value_iter

                for value_1, value_2 in zip(values_1, values_2):

                    value = weight*value_1 + (1-weight)*value_2

                    if type(value_1) == type(value_2) == int:
                        value = round(value)

                    yield value


            @genes_to_chromosome
            @values_to_genes
            def extrapolate(ga, parent_1, parent_2, weight = 0.5):

                """Cross two parents by extrapolating towards the first parent.
                May result in gene values outside the expected domain.
                """

                values_1 = parent_1.gene_value_iter
                values_2 = parent_2.gene_value_iter

                for value_1, value_2 in zip(values_1, values_2):

                    value = (2-weight)*value_1 + (weight-1)*value_2

                    if type(value_1) == type(value_2) == int:
                        value = round(value)

                    yield value
