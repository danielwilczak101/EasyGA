![](https://raw.githubusercontent.com/danielwilczak101/EasyGA/media/images/easyGA_logo.png)

# EasyGA - Genetic Algorithms made Easy

EasyGA is a python package designed to provide an easy-to-use Genetic Algorithm. The package is designed to work right out of the box, while also allowing the user to customize features as they see fit. 

## Check out our [Wiki](https://github.com/danielwilczak101/EasyGA/wiki) or [Youtube](https://www.youtube.com/watch?v=jbuDKwIiYBw) for more information.

## Installation:

Run python's pip3 to install:

```Python
pip3 install EasyGA
```

## Getting started with EasyGA(Basic Example):
```Python
import EasyGA

# Create the Genetic algorithm
ga = EasyGA.GA()

# Evolve the whole genetic algorithm until termination has been reached
ga.evolve()

# Print out the current generation and the population
ga.print_generation()
ga.print_population()
```

### Output:
```bash
Current Generation      : 15
Current population:
Chromosome - 0 [7][4][4][5][3][5][5][8][3][7] / Fitness = 3
Chromosome - 1 [7][4][4][5][3][5][5][8][3][7] / Fitness = 3
Chromosome - 2 [7][4][4][5][3][5][5][8][3][7] / Fitness = 3
Chromosome - 3 [7][4][4][5][3][5][5][8][3][7] / Fitness = 3
Chromosome - 4 [7][2][4][5][3][5][5][8][3][7] / Fitness = 3
Chromosome - 5 [7][2][4][5][3][5][5][8][3][7] / Fitness = 3
Chromosome - 6 [5][8][8][6][10][10][5][7][2][7] / Fitness = 2
Chromosome - 7 [5][8][8][6][10][10][5][7][2][7] / Fitness = 2
Chromosome - 8 [5][8][8][6][10][10][5][7][2][7] / Fitness = 2
Chromosome - 9 [7][2][8][10][3][5][5][8][1][7] / Fitness = 2
```

## Getting started with EasyGA (Password Cracker Example):
```Python
import EasyGA
import random

ga = EasyGA.GA()

word = input("Please enter a word: \n")

# Basic Attributes
ga.chromosome_length = len(word)
ga.fitness_goal = len(word)

# Size Attributes
ga.population_size = 50
ga.generation_goal = 10000

# User definded fitness
def password_fitness(chromosome):

    return sum(1 for gene, letter
        in zip(chromosome, word)
        if gene.value == letter
    )

ga.fitness_function_impl = password_fitness

# What the genes will look like.
ga.gene_impl = lambda: random.choice(["A","a","B","b","C","c","D","d","E","e",
                                      "F","f","G","g","H","h","I","i","J","j",
                                      "K","k","L","l","M","m","N","n","O","o",
                                      "P","p","Q","q","R","r","S","s","T","t",
                                      "U","u","V","v","W","w","X","x","Y","y",
                                      "Z","z"," "])

# Evolve the gentic algorithm
ga.evolve()

# Print out the current generation and the population
ga.print_generation()
ga.print_population()

# Show graph of progress
ga.graph.highest_value_chromosome()
ga.graph.show()
```

## Ouput:
```
Please enter a word: 
EasyGA
Current Generation 	: 44
Chromosome - 0 [E][a][s][y][G][A] / Fitness = 6
Chromosome - 1 [E][a][s][Y][G][A] / Fitness = 5
Chromosome - 2 [E][a][s][O][G][A] / Fitness = 5
Chromosome - 3 [E][a][s][Y][G][A] / Fitness = 5
Chromosome - 4 [E][a][s][c][G][A] / Fitness = 5
Chromosome - 5 [E][a][s][c][G][A] / Fitness = 5
Chromosome - 6 [E][a][s][y][Z][A] / Fitness = 5
Chromosome - 7 [E][a][s][Y][G][A] / Fitness = 5
Chromosome - 8 [E][a][s][y][Z][A] / Fitness = 5
Chromosome - 9 [E][a][s][Y][G][A] / Fitness = 5
```

![]()
<img width="500px" src="https://raw.githubusercontent.com/danielwilczak101/EasyGA/media/images/password_cracker_results.png" />

## Issues
We would love to know if your having any issues. Please start a new issue on the [Issues Page](https://github.com/danielwilczak101/EasyGA/issues).


## Local System Approach

Download the repository to some folder on your computer.

```
https://github.com/danielwilczak101/EasyGA/archive/master.zip
```
Use the run.py file inside the EasyGA folder to run your code. This is a local version of the package. 

## Check out our [wiki](https://github.com/danielwilczak101/EasyGA/wiki) for more information.
