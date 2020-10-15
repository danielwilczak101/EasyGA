import random
import EasyGA

# USE THIS COMMAND WHEN TESTING -
    # python3 -m pytest

def test_chromosome_length():
    for i in range(0,100):
        ga = EasyGA.GA()
        ga.chromosome_length = 100
        ga.evolve()

        """ Test to see if the actual chromosome length is the same as defined."""
        assert ga.population.chromosome_list[0].size() == ga.chromosome_length

def test_second():

    assert 1 + 1 == 2
