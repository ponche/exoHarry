from Sorcier import Sorcier
from Professeur import Professeur
from Sort import Sort
from Maison import Maison
from GestionDuel import GestionDuel

def main(): 
    # déclaration des maison 
    gryffondord = Maison("Gryffondord", "rouge")
    serpentard = Maison("Serpentard", "vert")
    serdaigle = Maison("Serdaigle", "bleu")
    poufsouffle = Maison("Poufsouffle", "jaune")

    harry = Sorcier("Potter", "Harry", 18, point_fort="malefiques", point_faible="metamorphose", maison= gryffondord)
    albus = Professeur("Dumbeldore", "Albus", 99 ,)
    drago = Sorcier("Malefoy", "Drago", 16, maison= serpentard)

    abracadabra = Sort("Abracadabra", "vert", "malefiques", 200, 0)
    petrifucus_totalus = Sort("Petrifucus_totalus", "jaune", "metamorphose", 20, 0)
    
    harry.ajouter_sort(abracadabra)
    harry.ajouter_sort(petrifucus_totalus)

    albus.ajouter_sort(abracadabra)
    albus.ajouter_sort(petrifucus_totalus)

    drago.ajouter_sort(petrifucus_totalus)

    # duel 
    #GestionDuel.combat(harry, abracadabra, albus, abracadabra)
    #GestionDuel.lancer_combat(harry, albus)
    GestionDuel.lancer_combat(harry, drago)



if __name__ == "__main__": 
    main()




