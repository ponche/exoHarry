from __future__ import annotations

from Sorcier import Sorcier
from Sort import Sort

class GestionDuel:

    @staticmethod
    def lancer_attaques(sorcier1: Sorcier, sorcier2: Sorcier):
        """duel de sorcier, fait affronter 2 sorcier avec le sort choisir pour un coup

        Args:
            sorcier1 (Sorcier): sorcier 1 pour duel
            sorcier2 (Sorcier): soricer 2 pour duel
        """
        sorcier1.lancer_sort(sorcier2)
        sorcier2.lancer_sort(sorcier1)

    @staticmethod
    def lancer_combat(sorcier1: Sorcier, sorcier2: Sorcier):
        """crée un duel avec lancer de 1 seul sort tirer alétoirement dans la liste sort des dualiste

        Args:
            sorcier1 (Sorcier): dualiste 1
            sorcier2 (Sorcier): dualiste 2
        """
        
        while(sorcier1.vie > 0 and sorcier2.vie > 0):
            GestionDuel.lancer_attaques(sorcier1, sorcier2)

        # vérification du vainqueur
        if (sorcier1.vie <= 0 and sorcier2.vie <= 0):
            #match null 
            print(f"match null, les 2 dualiste sont KO")
        elif (sorcier1.vie <= 0):
            #dualiste 2 gagne 
            print(f"{sorcier2} de la maison {sorcier2.maison} remporte le duel")
        else : 
            #dualiste 1 gagne 
            print(f"{sorcier1} de la maison {sorcier1.maison} remporte le duel")

        
        

   
   


        




        

        

        

        



