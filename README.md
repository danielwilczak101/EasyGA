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

## Different version that is more customized:
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

### Getting your Genes and Chromosomes from the population:
```Python
# Looking to print the first Chromosome
ga.population.chromosomes[0].print_chromosome()

# Looking to print one gene in chromosome 0
ga.population.chromosomes[0].genes[0].print_value()

# Looking to get the data of a chromosome
my_chromosome = ga.population.chromosomes[0]
print(f"my_chromosome: {my_chromosome.get_chromosome()}")
print(f"my_chromosome fitness: {my_chromosome.get_fitness()}")

# Looking to get the data of one gene in the chromosome
my_gene = ga.population.chromosomes[0].genes[0]
print(f"my_gene: {my_gene.get_value()}")
print(f"my_gene fitness: {my_gene.get_fitness()}")
```

### Ouput:
```Python
[38],[40],[29],[35],[85],[96],[87],[96],[53],[44]

38

my_chromosome: [<EasyGA.gene object at 0x7fb5642d4860>,
 <EasyGA.gene object at 0x7fb5642d4898>,
  <EasyGA.gene object at 0x7fb5642d4908>,
   <EasyGA.gene object at 0x7fb5642d49e8>,
    <EasyGA.gene object at 0x7fb5642d4b00>,
     <EasyGA.gene object at 0x7fb5642d4ba8>,
      <EasyGA.gene object at 0x7fb5642d4b70>,
       <EasyGA.gene object at 0x7fb5642d4c88>,
        <EasyGA.gene object at 0x7fb5642d4cc0>,
         <EasyGA.gene object at 0x7fb5642d4cf8>]

my_chromosome fitness: None
my_gene: 38
my_gene fitness: None
```


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
