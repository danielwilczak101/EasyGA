# EasyGA - A general solution to Genetic Algorithms

The projects has just started

## Installation

Run the rolling to install:

```Python
pip3 install EasyGA
```

To use the package
```python
import EasyGA
```

## Usage
```python
import random
import EasyGA

def user_gene_function():
    return random.randint(1, 100)

Population_size = 10
Chromosome_length = 10

ga = EasyGA.GA(Population_size, Chromosome_length,user_gene_function)

# Setup the GA's population,chromosomes and genes
ga.initialize()

print(ga.population.chromosomes[0].print_chromosome())

```

# Developing EasyGA
Download the repository to some folder
```
git clone https://github.com/danielwilczak101/EasyGA.git
```
Then install the repositroy using this command:
```
pip install -e .
```

# Working on developing a devel branch
To install EASY, along with the tools you need to develop and run tests, run the following in your virtual env:

```bash
$ pip install -e .[devel]
```
