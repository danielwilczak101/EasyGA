# EasyGA - A general solution to Genetic Algorithms

The project has just started

## Installation:

Run the rolling to install:

```Python
pip3 install EasyGA
```

To use the package:
```python
import EasyGA
```

## All you need to get started:
```python
import random
import EasyGA

# The user defined gene function
def user_gene_function():
    return random.randint(1, 100)

# The user defined Fitness Function
def user_fitness_function():
    pass

# Standard user size requirements
Population_size = 10
Chromosome_length = 10

# Create the Genetic algorithm
ga = EasyGA.GA(Population_size, Chromosome_length,user_gene_function)
ga.initialize()
```

# Getting your Genes and Chromosomes from the population:
```Python
# Looking to print the first Chromosome
ga.population.chromosomes[0].print_chromosome()

# Looking to print one gene in chromosome 0
ga.population.chromosomes[0].genes[0].print_value()

# Looking to get the data of a chromosome
my_chromosome = ga.population.chromosomes[0].get_chromosome()
print(f"my_chromosome: {my_chromosome}")
# Looking to get the data of one gene in the chromosome
my_gene = ga.population.chromosomes[0].genes[0].get_value()
print(f"my_gene: {my_gene}")
```

# Ouput:
```Python
[99],[30],[59],[77],[68],[57],[14],[92],[85],[27]

99

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

my_gene: 99

```


# Developing EasyGA:
Download the repository to some folder - If you never used git. Look up a youtube tutorial. It will all make sense.
```
git clone https://github.com/danielwilczak101/EasyGA.git
```
Then install the repositroy using this command:
```
pip install -e .
```

# Working on developing a devel branch:
To install EASY, along with the tools you need to develop and run tests, run the following in your virtual env:

```bash
$ pip install -e .[devel]
```
