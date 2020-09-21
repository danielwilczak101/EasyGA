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

# Setup the defult genetic algorithm
ga = EasyGA.GA()
# Run the defult genetic algorithm
ga.evolve()
```
### Output:
```Python
print("Output HERE")
```

## How to use EasyGA:
```python
import random
import EasyGA

# The user defined gene function
def user_gene_function():
    return random.randint(1, 100)

# The user defined Fitness Function
def user_fitness_function(chromosome):
    pass

# Standard user size requirements
Population_size = 10
Chromosome_length = 10

# Create the Genetic algorithm
ga = EasyGA.GA(Population_size, Chromosome_length,user_gene_function,user_fitness_function)
ga.initialize()
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
