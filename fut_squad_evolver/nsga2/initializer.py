"""
This module provides an Initializer class that generates genotypes.
"""
from fut_squad_evolver.nsga2.individual import Individual


class Initializer:

    def __init__(self, n_individuals):
        self.n_individuals = n_individuals

    def _initialize(self):
        """
        Initializes a single genotype, needs to be overriden by the child class.
        """
        pass

    def _initialize_individual(self):
        return Individual(self._initialize())

    def initialize(self):
        """
        Initializes a list of individuals with length self.n_individuals.
        """
        population = {}
        for _ in range(self.n_individuals):
            indiviual = self._initialize_individual()
            population[indiviual.individual_id] = indiviual
        return population
