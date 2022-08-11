from __future__ import annotations

from Personne import Personne
from Sort import Sort
import math
import random

class Sorcier(Personne):
    def __init__(self, nom, prenom, age, vie = 100, point_fort = None, point_faible = None , maison = None ) -> None:
        super().__init__(nom, prenom, age, vie)
        self._point_fort = point_fort
        self._point_faible = point_faible
        self._maison = maison
        self._list_sort = []

    @property
    def point_fort(self):
        return self._point_fort


    @property
    def point_faible(self):
        return self._point_faible


    @property
    def maison(self):
        return self._maison


    def ajouter_sort(self, nouveau_sort: Sort):
        """ajouter un nouveau sort au sorcier 

        Args:
            nouveau_sort (Sort): le nouveau sort 

        
        """
        if type(nouveau_sort) is not Sort:
            raise TypeError("sort doit etre de Type Sort")

        self._list_sort.append(nouveau_sort)
        

    def recevoir_sort(self, sort_recu: Sort): 
        """recevoir un sort 

        Args:
            sort_recu (Sort): le sort recu ( dégats ou soin)

        Returns:
            self: return self
        """
        coef_degats = 1
        if sort_recu.categorie == self.point_faible:
            coef_degats = 2

        if sort_recu.categorie == self.point_fort:
            coef_degats = 0.5

        degats_subit = coef_degats * sort_recu.degats
        self.recevoir_degats(degats_subit)
        print(f"{self.nom} à subit {degats_subit} point de degats avec le sort {sort_recu.nom} il lui reste {self.vie} point de vie")

        return self

    def tomber(self, taux_fail: int = 10) -> bool:
        """à 10% de chanche d'envoyer True

        Returns:
            bool: True, si il tombe, sinon False
        """
        aleatoire = random.randrange(0, 100)
        if aleatoire <= taux_fail: 
            #Le sorcier tombe comme une merde
            return True
        return False

    def selectioner_sort_aleatoire(self):
        """choisir un sort aléatoire dans liste du sorcier 

        Returns:
            Sort: retourne le sort tirer aléatoirement
        """
        nombre_sort = len(self._list_sort)
        index_sort_aleatoire = random.randint(0, nombre_sort - 1)
        return self._list_sort[index_sort_aleatoire]

    def lancer_sort(self , cible: Sorcier):
        """lance un sort aléatoire

        Args:
            cible (Sorcier): cible du sort
        """
        sort = self.selectioner_sort_aleatoire()

        if self.tomber():
            print(f"{self} a échouer son sort {sort.nom} sur {cible}")
        else:
            print(f"{self} lance le sort {sort.nom} sur {cible}")
            cible.recevoir_sort(sort)

   