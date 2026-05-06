import math
import pygame

from model.game_model import GameModel
from view.game_view import GameView, hole_center, HOLE_RADIUS, WINDOW_WIDTH, WINDOW_HEIGHT


class GameController:
    # TODO: definire costruttore __init__(self) che inizializzi pygame, lo schermo, il clock, model e view

    # TODO: definire metodo 'run(self)' con il loop principale del gioco:
    #       - gestire l'evento QUIT per uscire
    #       - gestire MOUSEBUTTONDOWN per catturare il clic (invocando _handle_click)
    #       - chiamare view.draw e impostare il framerate a 60

    # TODO: definire metodo '_handle_click(self, pos)' che trova l'indice cliccato e lo inverte nel model

    # TODO: definire metodo '_hole_at(self, pos)' che:
    #       - calcola la distanza tra la posizione e i centri dei buchi
    #       - restituisce l'indice del buco se ci troviamo all'interno del suo raggio, altrimenti None
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Whack-a-mole")
        self.clock = pygame.time.Clock()
        self.model = GameModel()
        self.view = GameView(self.screen)
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._handle_click(event.pos)
            self.view.draw(self.model)
            self.clock.tick(60)
        pygame.quit()
    
    def _handle_click(self, pos):
        index = self._hole_at(pos)
        if index is not None:
            self.model.toggle_hole(index)
    
    def _hole_at(self, pos):
        for i in range(self.model.NUM_HOLES):
            cx, cy = hole_center(i)
            distance = math.sqrt((pos[0] - cx)**2 + (pos[1] - cy)**2)
            if distance <= HOLE_RADIUS:
                return i
        return None
