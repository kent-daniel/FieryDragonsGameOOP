class DragonCard:
    def __init__(self, animals):
        self.animals = animals
        self.is_pirate = any(animal == "Pirate" for animal in animals)