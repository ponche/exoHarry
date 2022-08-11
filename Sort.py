class Sort:
    def __init__(self, nom: str, couleur_sort: str, categorie: str, degats: int, vie: int = 0) -> None:
        self._nom = nom
        self._couleur_sort = couleur_sort
        self._categorie = categorie
        self._degats = degats
        self._vie = vie

    def __str__(self) -> str:
        return self._nom

    @property
    def nom(self):
        return self._nom

    @property
    def couleur_sort(self):
        return self._couleur_sort

    @property
    def categorie(self):
        return self._categorie

    @property
    def degats(self):
        return self._degats

    @property
    def vie(self): 
        return self._vie

    

    

    

    