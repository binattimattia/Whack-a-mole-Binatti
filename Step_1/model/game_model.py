class Hole:
    """Un singolo buco della griglia."""
    # TODO: definire un costruttore che inizializzi lo stato (is_active) a False
    # TODO: definire un metodo 'toggle' per invertire lo stato (is_active)
    def __init__(self):
        self.is_active = False
    
    def toggle(self):
        self.is_active = not self.is_active

class GameModel:
    """Stato complessivo del gioco."""
    NUM_HOLES = 9

    # TODO: definire un costruttore che inizializzi una lista di 'NUM_HOLES' buchi
    # TODO: definire un metodo 'toggle_hole(index)' per invocare il toggle del buco corrispondente (con validazione)
    def __init__(self):
        self.holes = [Hole() for _ in range(self.NUM_HOLES)]
    
    def toggle_hole(self, index):
        if 0 <= index < self.NUM_HOLES:
            self.holes[index].toggle()
