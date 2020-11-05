import random
import EasyGA

# USE THIS COMMAND WHEN TESTING -
    # python3 -m pytest

# Tests can be broken down into three parts.
#   - Testing correct size
#       - Testing size while integrated with our function
#   - Testing correct value
#       - Testing integration with other functions

def test_population_size():
    """Test the population size is create correctly"""

    for i in range(1,100):
        # Create the ga to test
        ga = EasyGA.GA()
        # Set the upper limit of testing
        ga.population_size = i
        # Evolve the ga
        ga.evolve()

        # If they are not equal throw an error
        assert ga.population.size() == ga.population_size

def test_chromosome_length():
    """ Test to see if the actual chromosome length is the same as defined."""

    # Test from 0 to 100 chromosome length
    for i in range(1,100):
        # Create the ga to test
        ga = EasyGA.GA()
        # Set the upper limit of testing
        ga.chromosome_length = i
        # Evolve the ga
        ga.evolve()

        # If they are not equal throw an error
        assert ga.population.chromosome_list[0].size() == ga.chromosome_length

def test_gene_value():
    """ """
    pass

def test_initilization():
    """ """
    pass

def test_default():
    # Create the Genetic algorithm
    ga = EasyGA.GA()

    # Evolve the genetic algorithm
    ga.evolve()

    # Print your default genetic algorithm
    ga.print_generation()
    ga.print_population()


def test_attributes_gene_impl():
    # Create the Genetic algorithm
    ga = EasyGA.GA()

    # Set necessary attributes
    ga.population_size = 3
    ga.chromosome_length = 5
    ga.generation_goal =  1
    # Set gene_impl
    ga.gene_impl = lambda: random.randint(1, 10)

    # Evolve the genetic algorithm
    ga.evolve()


def test_attributes_chromosome_impl_lambdas():
    # Create the Genetic algorithm
    ga = EasyGA.GA()

    # Set necessary attributes
    ga.chromosome_length = 3
    ga.generation_goal = 1
    # Set gene_impl to None so it won't interfere
    ga.gene_impl = None
    # Set chromosome_impl
    ga.chromosome_impl = lambda: [
        random.randrange(1,100),
        random.uniform(10,5),
        random.choice(["up","down"])
        ]

    # Evolve the genetic algorithm
    ga.evolve()

def test_attributes_chromosome_impl_functions():
    # Create the Genetic algorithm
    ga = EasyGA.GA()

    # Set necessary attributes
    ga.chromosome_length = 3
    ga.generation_goal = 1

    # Create chromosome_impl user function
    def user_chromosome_function():
        chromosome_data = [
            random.randrange(1,100),
            random.uniform(10,5),
            random.choice(["up","down"])
            ]
        return chromosome_data

    # Set the chromosome_impl
    ga.chromosome_impl = user_chromosome_function

    # Evolve the genetic algorithm
    ga.evolve()

def test_while_ga_active():
    # Create the Genetic algorithm
    ga = EasyGA.GA()

    # Set necessary attributes
    ga.generation_goal = 1

    # Evolve using ga.active
    while ga.active():
        ga.evolve_generation(5)


def test_initilization_impl():
    # Create the Genetic algorithm
    ga = EasyGA.GA()

    # Set the initialization_impl
    ga.initialization_impl = EasyGA.Initialization_Methods.random_initialization

    # Evolve the genetic algorithm
    ga.evolve()

    assert (ga.initialization_impl == EasyGA.Initialization_Methods.random_initialization) and (ga != None)

def test_parent_selection_impl():
    # Create the Genetic algorithm
    ga = EasyGA.GA()

    # Set the parent_selection_impl
    ga.parent_selection_impl = EasyGA.Parent_Selection.Fitness.roulette

    # Evolve the genetic algorithm
    ga.evolve()

    assert (ga.parent_selection_impl == EasyGA.Parent_Selection.Fitness.roulette) and (ga != None)

def test_crossover_population_impl():
    # Create the Genetic algorithm
    ga = EasyGA.GA()

    # Set the crossover_population_impl
    ga.crossover_population_impl = EasyGA.Crossover_Methods.Population.sequential_selection

    # Evolve the genetic algorithm
    ga.evolve()

    assert (ga.crossover_population_impl == EasyGA.Crossover_Methods.Population.sequential_selection) and (ga != None)

def test_crossover_individual_impl():
    # Create the Genetic algorithm
    ga = EasyGA.GA()

    # Set the crossover_individual_impl
    ga.crossover_individual_impl = EasyGA.Crossover_Methods.Individual.single_point

    # Evolve the genetic algorithm
    ga.evolve()

    assert (ga.crossover_individual_impl == EasyGA.Crossover_Methods.Individual.single_point) and (ga != None)

def test_mutation_population_impl():
    # Create the Genetic algorithm
    ga = EasyGA.GA()

    # Set the mutation_population_impl
    ga.mutation_population_impl = EasyGA.Mutation_Methods.Population.random_selection

    # Evolve the genetic algorithm
    ga.evolve()

    assert (ga.mutation_population_impl == EasyGA.Mutation_Methods.Population.random_selection) and (ga != None)

def test_mutation_individual_impl():
    # Create the Genetic algorithm
    ga = EasyGA.GA()

    # Set the mutation_population_impl
    ga.mutation_individual_impl = EasyGA.Mutation_Methods.Individual.single_gene

    # Evolve the genetic algorithm
    ga.evolve()

    assert (ga.mutation_individual_impl == EasyGA.Mutation_Methods.Individual.single_gene) and (ga != None)

def test_survivor_selection_impl():
    # Create the Genetic algorithm
    ga = EasyGA.GA()

    # Set the survivor_selection_impl
    ga.survivor_selection_impl = EasyGA.Survivor_Selection.fill_in_random

    # Evolve the genetic algorithm
    ga.evolve()

    assert (ga.survivor_selection_impl == EasyGA.Survivor_Selection.fill_in_random) and (ga != None)

def test_termination_impl():
    # Create the Genetic algorithm
    ga = EasyGA.GA()

    # Set the termination_impl
    ga.termination_impl = EasyGA.Termination_Methods.fitness_and_generation_based

    # Evolve the genetic algorithm
    ga.evolve()

    assert (ga.termination_impl == EasyGA.Termination_Methods.fitness_and_generation_based) and (ga != None)
