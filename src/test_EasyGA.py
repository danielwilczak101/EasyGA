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
    pass

def test_chromosome_length():
    """ Test to see if the actual chromosome length is the same as defined."""

    # Test from 0 to 100 chromosome length
    for i in range(0,100):
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

def test_second():

    assert 1 + 1 == 2
