# EasyGA - A general solution to Genetic Algorithms

EasyGA is a python package designed to provide an easy-to-use Genetic Algorithm. The package is designed to work right out of the box, while also allowing the user to customize features as they see fit.

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
```bash
Current population:
Chromosome - 0 [8][9][5][5][1][5][7][3][10][8] / Fitness = 3
Chromosome - 1 [5][9][8][5][1][5][7][3][10][10] / Fitness = 3
Chromosome - 2 [5][9][5][5][1][6][7][3][10][8] / Fitness = 3
Chromosome - 3 [5][9][5][5][1][6][7][3][10][8] / Fitness = 3
Chromosome - 4 [5][9][5][5][1][4][7][3][10][10] / Fitness = 3
Chromosome - 5 [5][9][6][5][1][5][7][3][10][10] / Fitness = 3
Chromosome - 6 [5][9][5][5][1][6][7][3][10][8] / Fitness = 3
Chromosome - 7 [5][9][8][5][1][5][7][3][10][10] / Fitness = 3
Chromosome - 8 [4][9][5][5][1][6][7][3][10][10] / Fitness = 2
Chromosome - 9 [5][10][5][7][7][2][2][6][2][9] / Fitness = 2
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
============================================= test session starts ==============================================
platform darwin -- Python 3.8.6rc1, pytest-6.0.2, py-1.9.0, pluggy-0.13.1
rootdir: /Users/danielwilczak/github/EasyGA
collected 2 items                                                                                              

test_EasyGA.py ..                                                                                        [100%]

============================================== 2 passed in 0.04s ===============================================
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
