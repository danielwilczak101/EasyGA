![](https://raw.githubusercontent.com/danielwilczak101/EasyGA/media/images/easyGA_logo.png)

# EasyGA - Genetic Algorithms made Easy

EasyGA is a python package designed to provide an easy-to-use Genetic Algorithm. The package is designed to work right out of the box, while also allowing the user to customize features as they see fit. 

## Check out our [wiki](https://github.com/danielwilczak101/EasyGA/wiki) for more information.

## Installation:

Run python's pip3 to install:

```Python
pip3 install EasyGA
```

## Getting started with EasyGA:
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

## Issues
We would love to know if your having any issues. Please start a new issue on the [Issues Page](https://github.com/danielwilczak101/EasyGA/issues).


## Local System Approach

Download the repository to some folder on your computer.

```
https://github.com/danielwilczak101/EasyGA/archive/master.zip
```
Use the run.py file inside the EasyGA folder to run your code. This is a local version of the package. 
