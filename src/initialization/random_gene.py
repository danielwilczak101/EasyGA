# Imported library
import random

def check_values(low,high):
    #Check to make sure its not less then zero
    assert low > 0 , "The random gene low can not be less then zero"
    # Check to make sure the high value is not
    # lower than or equal to low and not 0.
    assert high > low , "High value can not be smaller then low value"
    assert high != 0, "High value can not be zero"

def random_gene(low,high):
    # Check the values so that they follow the rules.
    check_values(low,high)
    return random.randint(1,100)
