# EasyGA - A general solution to Genetic Algorithms

The projects has just started

## Installation

Run the rolling to install:

```Python
pip3 install EasyGA
```

To use the package
```python
import EasyGA as ga
```

## Usage

```python
import EasyGA as ga

chromosome = ga.chromosome()

# Fill the chromosome with genes with Gene Number i'th number 
for i in range(10):
    gene_value = f"Gene Number {i}"
    new_gene = ga.gene("gene_value")
    chromosome.add_gene(new_gene)

# Chromosome has 10 genes in it
print(len(chromosome.genes))

# Get the first genes value
print(chromosome.genes[0].get_value())

```

# Developing EasyGA

To install EASY, along with the tools you need to develop and run tests, run the following in your virtual env:

```bash
$ pip install -e .[dev]
```