# EasyGA - A general solution to Genetic Algorithms

Project description

## Installation:

Run the rolling to install:

```Python
pip3 install EasyGA
```

## Getting started with EasyGA:
```Python
import EasyGA

# Setup the default genetic algorithm
ga = EasyGA.GA()
# Run the default genetic algorithm
ga.evolve()
```

### Output:
```python
Put the out here
```

## Customized:
```python
import random
import EasyGA

# Setup the default genetic algorithm
ga = EasyGA.GA()

# User set sizes
ga.population_size = 10
ga.chromosome_length = 10
ga.generations = 10

# The user defined gene function
def user_gene_function():
    pass

# The user defined Fitness function that gives the chromosome some kind of fitness
def user_fitness_function(chromosome):
    pass

# The user defined initialization function
def user_initialization_function():
    pass

# User sets the gene function
ga.gene = user_gene_function
# Set the fitness functions
ga.fitness =  user_fitness_function
# Changing the initialization function.
ga.initialization = user_initialization_function
# Run the customized genetic algorithm
ga.eveolve()
```

### Output:
```python
Put the out here
```

# How Testing works

### Getting started with testing

```bash
pip3 install pytest
```

### Navigate to your EasyGA folder and run:
```bash
pytest
```

#### Output
```bash
============================== 1 passed in 0.02s ===============================
danielwilczak@Daniels-MacBook-Pro EasyGA % pytest
============================= test session starts ==============================
platform darwin -- Python 3.8.6rc1, pytest-6.0.2, py-1.9.0, pluggy-0.13.1
rootdir: /Users/danielwilczak/github/EasyGA
collected 1 item                                                               

src/gene/test_gene.py .                                                  [100%]

============================== 1 passed in 0.03s ===============================  

```

This is only example and we will create hundreds of tests so this list will become bigger and bigger.


## Developing EasyGA:
### If you know how to use Github and git ignore this section.

### Getting started with development
To work together we plan on using github and the git framework. This is made easy with the Atom software.

Download Atom for whatever OS you have.
https://atom.io/

Use the github tab to pull the github repository. Its self explanitory.

Use the example.py file inside the src folder to run your code and test while we build the package.

## Other options

Download the repository to some folder - If you never used git. Look up a youtube tutorial. It will all make sense.
```
git clone https://github.com/danielwilczak101/EasyGA.git
```
Or download as a zip file.
```
https://github.com/danielwilczak101/EasyGA/archive/master.zip
```
Use the example.py file inside the src folder to run your code and test while we build the package.
