from __future__ import annotations
from inspect import signature
from typing import Callable, Optional, Iterable, Any, Dict
from math import sqrt, ceil
from dataclasses import dataclass, field
from functools import wraps
import random

import sqlite3
import matplotlib.pyplot as plt

from structure import Population
from structure import Chromosome
from structure import Gene

from examples import Fitness
from termination import Termination
from parent import Parent
from survivor import Survivor
from crossover import Crossover
from mutation import Mutation
from database import sql_database, matplotlib_graph


@dataclass
class Attributes:
    """
    Attributes class which stores all attributes in a dataclass.
    Contains default attributes for each attribute.
    """

    properties: Dict[str, Any] = field(default_factory=dict, init=False, repr=False, compare=False)

    run: int = 0

    chromosome_length: int = 10
    population_size: int = 10
    population: Optional[Population] = None

    target_fitness_type: str = 'max'
    update_fitness: bool = False

    parent_ratio: float = 0.1
    selection_probability: float = 0.5
    tournament_size_ratio: float = 0.1

    current_generation: int = 0
    generation_goal: int = 100
    fitness_goal: Optional[float] = None
    tolerance_goal: Optional[float] = None
    percentage_converged: float = 0.5

    chromosome_mutation_rate: float = 0.15
    gene_mutation_rate: float = 0.05

    adapt_rate: float = 0.05
    adapt_probability_rate: float = 0.05
    adapt_population_flag: bool = True

    max_selection_probability: float = 0.75
    min_selection_probability: float = 0.25
    max_chromosome_mutation_rate: float = None
    min_chromosome_mutation_rate: float = None
    max_gene_mutation_rate: float = 0.15
    min_gene_mutation_rate: float = 0.01

    fitness_function_impl: Callable[[Attributes, Chromosome], float] = Fitness.is_it_5
    make_population: Callable[[Iterable[Iterable[Any]]], Population] = Population
    make_chromosome: Callable[[Iterable[Any]], Chromosome] = Chromosome
    make_gene: Callable[[Any], Gene] = Gene

    gene_impl: Callable[[Attributes], Any] = field(default_factory=lambda: rand_1_to_10)
    chromosome_impl: Optional[[Attributes], Iterable[Any]] = field(default_factory=lambda: use_genes)
    population_impl: Optional[[Attributes], Iterable[Iterable[Any]]] = field(default_factory=lambda: use_chromosomes)

    weighted_random: Callable[[Attributes, float], float] = field(default_factory=lambda: simple_linear)
    dist: Callable[[Attributes, Chromosome, Chromosome], float] = field(default_factory=lambda: dist_fitness)

    parent_selection_impl: Callable[[Attributes], None] = Parent.Rank.tournament
    crossover_individual_impl: Callable[[Attributes], None] = Crossover.Individual.single_point
    crossover_population_impl: Callable[[Attributes], None] = Crossover.Population.sequential
    survivor_selection_impl: Callable[[Attributes], None] = Survivor.fill_in_best
    mutation_individual_impl: Callable[[Attributes], None] = Mutation.Individual.individual_genes
    mutation_population_impl: Callable[[Attributes], None] = Mutation.Population.random_avoid_best
    termination_impl: Callable[[Attributes], None] = Termination.fitness_generation_tolerance

    database: Database = sql_database.SQL_Database
    database_name: str = 'database.db'
    sql_create_data_structure: str = """
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY,
            config_id INTEGER DEFAULT NULL,
            generation INTEGER NOT NULL,
            fitness REAL,
            chromosome TEXT
        );
    """

    graph: Callable[[Database], Graph] = matplotlib_graph.Matplotlib_Graph


    #============================#
    # Built-in database methods: #
    #============================#


    def save_population(self: Attributes) -> None:
        """Saves the current population to the database."""
        self.database.insert_current_population(self)


    def save_chromosome(self: Attributes, chromosome: Chromosome) -> None:
        """
        Saves a chromosome to the database.

        Parameters
        ----------
        chromosome : Chromosome
            The chromosome to be saved.
        """
        self.database.insert_current_chromosome(self.current_generation, chromosome)


def rand_1_to_10(self: Attributes) -> int:
    """
    Default gene_impl, returning a random integer from 1 to 10.

    Returns
    -------
    rand : int
        A random integer between 1 and 10, inclusive.
    """
    return random.randint(1, 10)


def use_genes(self: Attributes) -> Iterable[Any]:
    """
    Default chromosome_impl, generates a chromosome using the gene_impl and chromosome length.

    Attributes
    ----------
    gene_impl() -> Any
        A gene implementation.
    chromosome_length : int
        The length of a chromosome.

    Returns
    -------
    chromosome : Iterable[Any]
        Generates the genes for a chromosome.
    """
    for _ in range(self.chromosome_length):
        yield self.gene_impl()


def use_chromosomes(self: Attributes) -> Iterable[Any]:
    """
    Default population_impl, generates a population using the chromosome_impl and population size.

    Attributes
    ----------
    chromosome_impl() -> Any
        A chromosome implementation.
    population_size : int
        The size of the population.

    Returns
    -------
    population : Iterable[Iterable[Any]]
        Generates the chromosomes for a population.
    """
    for _ in range(self.population_size):
        yield self.chromosome_impl()


def dist_fitness(self: Attributes, chromosome_1: Chromosome, chromosome_2: Chromosome) -> float:
    """
    Measures the distance between two chromosomes based on their fitnesses.

    Parameters
    ----------
    chromosome_1, chromosome_2 : Chromosome
        Chromosomes being compared.

    Returns
    -------
    dist : float
        The distance between the two chromosomes.
    """
    return sqrt(abs(chromosome_1.fitness - chromosome_2.fitness))


def simple_linear(self: Attributes, weight: float) -> float:
    """
    Returns a random value between 0 and 1, with increased probability
    closer towards the side with weight.

    Parameters
    ----------
    weight : float
        A float between 0 and 1 which determines the output distribution.

    Returns
    -------
    rand : float
        A random value between 0 and 1.
    """
    rand = random.random()
    if rand < weight:
        return rand * (1-weight) / weight
    else:
        return 1 - (1-rand) * weight / (1-weight)


#==================================================#
# Properties for attributes behaving like methods. #
#==================================================#


def get_method(name: str) -> Callable[[Attributes], Callable[..., Any]]:
    """
    Creates a getter method for getting a method from the Attributes class.

    Parameters
    ----------
    name : str
        The name of the method from Attributes.

    Returns
    -------
    getter(ga)(...) -> Any
        The getter property, taking in an object and returning the method.
    """
    def getter(self: Attributes) -> Callable[..., Any]:
        return self.properties[name]
    return getter


def set_method(name: str) -> Callable[[Attributes, Optional[Callable[..., Any]]], None]:
    """
    Creates a setter method for setting a method from the Attributes class.

    Parameters
    ----------
    name : str
        The name of the method from Attributes.

    Returns
    -------
    setter(ga, method)
        The setter property, taking in an object and returning nothing.
    """
    def setter(self: Attributes, method: Optional[Callable[..., Any]]) -> None:
        if method is None:
            new_method = method
        elif not callable(method):
            raise TypeError(f"{name} must be a method i.e. callable.")
        elif next(iter(signature(method).parameters), None) in ("self", "ga"):
            new_method = wraps(method)(lambda *args, **kwargs: method(self, *args, **kwargs))
        else:
            new_method = method
        self.properties[name] = new_method
    return setter


for name in (
    "fitness_function_impl",
    "parent_selection_impl",
    "crossover_individual_impl",
    "crossover_population_impl",
    "survivor_selection_impl",
    "mutation_individual_impl",
    "mutation_population_impl",
    "termination_impl",
    "dist",
    "weighted_random",
    "gene_impl",
    "chromosome_impl",
    "population_impl",
):
    setattr(Attributes, name, property(get_method(name), set_method(name)))


#============================#
# Static checking properties #
#============================#


static_checks = {
    "run": {
        "check": lambda value: isinstance(value, int) and value >= 0,
        "error": "ga.run counter must be an integer greater than or equal to 0.",
    },
    "current_generation": {
        "check": lambda value: isinstance(value, int) and value >= 0,
        "error": "ga.current_generation must be an integer greater than or equal to 0",
    },
    "chromosome_length": {
        "check": lambda value: isinstance(value, int) and value > 0,
        "error": "ga.chromosome_length must be an integer greater than and not equal to 0.",
    },
    "population_size": {
        "check": lambda value: isinstance(value, int) and value > 0,
        "error": "ga.population_size must be an integer greater than and not equal to 0.",
    },
}


def get_attr(name: str) -> Callable[[Attributes], Any]:
    """
    Creates a getter method for getting an attribute from the Attributes class.

    Parameters
    ----------
    name : str
        The name of the attribute.

    Returns
    -------
    getter(ga) -> Any
        A getter method which returns an attribute.
    """
    def getter(self: Attributes) -> Any:
        return self.properties[name]
    return getter


def set_attr(name: str, check: Callable[[Any], bool], error: str) -> Callable[[Attributes, Any], None]:
    """
    Creates a setter method for setting an attribute from the Attributes class.

    Parameters
    ----------
    name : str
        The name of the attribute.
    check(Any) -> bool
        The condition needed to be passed for the attribute to be added.
    error: str
        An error message if check(...) turns False.

    Returns
    -------
    setter(ga, Any) -> None
    Raises ValueError(error)
        A setter method which saves to an attribute.
    """
    def setter(self: Attributes, value: Any) -> Any:
        if check(value):
            self.properties[name] = value
        else:
            raise ValueError(error)
    return setter


for name in static_checks:
    setattr(
        Attributes,
        name,
        property(
            get_attr(name),
            set_attr(name, static_checks[name]["check"], static_checks[name]["error"]),
        )
    )


#==================#
# Other properties #
#==================#


def get_max_chromosome_mutation_rate(self: Attributes) -> float:
    return self._max_chromosome_mutation_rate


def set_max_chromosome_mutation_rate(self: Attributes, value: Optional[float]) -> None:

    # Default value
    if value is None:
        self._max_chromosome_mutation_rate = min(
            self.chromosome_mutation_rate * 2,
            (self.chromosome_mutation_rate + 1) / 2,
        )

    # Otherwise check value
    elif isinstance(value, (float, int)) and 0 <= value <= 1:
        self._max_chromosome_mutation_rate = value

    # Raise error
    else:
        raise ValueError("Max chromosome mutation rate must be between 0 and 1")


def get_min_chromosome_mutation_rate(self: Attributes) -> float:
    return self._min_chromosome_mutation_rate


def set_min_chromosome_mutation_rate(self: Attributes, value: Optional[float]) -> None:

    # Default value
    if value is None:
        self._min_chromosome_mutation_rate = max(
            self.chromosome_mutation_rate / 2,
            self.chromosome_mutation_rate * 2 - 1,
        )

    # Otherwise check value
    elif isinstance(value, (float, int)) and 0 <= value <= 1:
        self._min_chromosome_mutation_rate = value

    # Raise error
    else:
        raise ValueError("Min chromosome mutation rate must be between 0 and 1")


def get_database_name(self: Attributes) -> str:
    return self._database_name


def set_database_name(self: Attributes, name: str) -> None:

    # Update the database class' name
    self.database._database_name = name

    # Set the attribute for itself
    self._database_name = name


def get_graph(self: Attributes) -> Graph:
    return self._graph


def set_graph(self: Attributes, graph: Callable[[Database], Graph]) -> None:
    self._graph = graph(self.database)


def get_active(self: Attributes) -> Callable[[Attributes], None]:
    return self.termination_impl


Attributes.max_chromosome_mutation_rate = property(get_max_chromosome_mutation_rate, set_max_chromosome_mutation_rate)
Attributes.min_chromosome_mutation_rate = property(get_min_chromosome_mutation_rate, set_min_chromosome_mutation_rate)
Attributes.database_name = property(get_database_name, set_database_name)
Attributes.graph = property(get_graph, set_graph)
Attributes.active = property(get_active)
