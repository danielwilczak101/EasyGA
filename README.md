![](https://raw.githubusercontent.com/danielwilczak101/EasyGA/media/images/easyGA_logo.png)

# EasyGA - Genetic Algorithms made Easy

EasyGA is a python package designed to provide an easy-to-use Genetic Algorithm. The package is designed to work right out of the box, while also allowing the user to customize features as they see fit.

### Check out our [wiki](https://github.com/danielwilczak101/EasyGA/wiki) for more information.

## Installation:

Run the rolling to install:

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



# How Testing works

### Getting started with testing

```bash
pip3 install pytest
```

### Navigate to your EasyGA folder and run:
```bash
python3 -m pytest
```

#### Output
```bash
============================================= test session starts =========================
platform darwin -- Python 3.8.6rc1, pytest-6.0.2, py-1.9.0, pluggy-0.13.1
rootdir: /Users/github/EasyGA
collected 2 items                                                      

test_EasyGA.py ..                                                                    [100%]

============================================== 2 passed in 0.04s ==========================
```




This is only an example and we will create hundreds of tests so this list will become bigger and bigger.


## Developing EasyGA:
### If you know how to use Github and git ignore this section.

### Getting started with development
To work together we plan on using github and the git framework. This is made easy with the Atom software.

Download Atom for whatever OS you have.
https://atom.io/

Use the github tab to pull the github repository. Its self explanitory.

Use the <b>run_testing.py</b> file inside the src folder to run your code and test while we build the package.

## Upload to PyPi

1. Change version number to whatever plus 1
2. Rename "src" folder to "EasyGA"
3. Run these two commands
```
python setup.py bdist_wheel sdist // Build the package for publishing
twine upload dist/* // Upload package to PyPI
```

The second command requires a username and password.

## Other options

Download the repository to some folder - If you never used git. Look up a youtube tutorial. It will all make sense.
```
git clone https://github.com/danielwilczak101/EasyGA.git
```
Or download as a zip file.
```
https://github.com/danielwilczak101/EasyGA/archive/master.zip
```
Use the run_testing.py file inside the src folder to run your code and test while we build the package.
