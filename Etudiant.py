from Sorcier import Sorcier

class Etudiant(Sorcier):
    def __init__(self, nom, prenom, age, maison , vie=100, point_fort = None, point_faible = None ) -> None:
        super().__init__(nom, prenom, age, vie, point_fort, point_faible, maison)

        