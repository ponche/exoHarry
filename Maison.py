class Maison:
    def __init__(self, name: str, couleur_principale: str) -> None:
        self._couleur_principale = couleur_principale
        self._name = name

    def __str__(self) -> str:
        return self._name

    @property
    def name(self):
        return self._name

    @property
    def couleur_principale(self):
        return self._couleur_principale

    @couleur_principale.setter
    def couleur_principale(self, valeur):
        self._couleur_principale = valeur

    