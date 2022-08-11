from __future__ import annotations
from abc import ABC, abstractmethod
import math

from Sort import Sort

class Personne(ABC): 
    def __init__(self, nom, prenom, age, vie) -> None:
        self._nom = nom
        self._prenom = prenom
        self._age = age
        self._vie = vie

    def __str__(self) -> str:
        return f"{self._prenom} {self._nom}"
       

    @property
    def nom(self):
        return self._nom

    @property
    def prenom(self):
        return self._prenom

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, valeur): 
        self._age = valeur

    @property
    def vie(self):
        return self._vie

    @vie.setter
    def vie(self, valeur):
        self._vie = valeur
        if self._vie < 0: 
            self.vie = 0

    @abstractmethod
    def recevoir_sort(self, sort_recu: Sort): 
        pass
        

    def recevoir_degats(self, degats: int):
        """recevoir les dégats et décrémente sur le nombre de point de vie 

        Args:
            degats (int): degats subits ( nombre de point de vie à lui retirer)
        
        """
        degats_subit = math.ceil(degats)
        self.vie -= degats_subit

        
        

    

    

