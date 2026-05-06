import pygame

# Dimensioni finestra
WINDOW_WIDTH  = 600
WINDOW_HEIGHT = 600

# Griglia
GRID_ROWS    = 3
GRID_COLS    = 3
HOLE_RADIUS  = 60
GRID_MARGIN  = 60

# Colori
COLOR_BG       = (30, 30, 40)
COLOR_HOLE     = (90, 90, 100)
COLOR_HOLE_ON  = (230, 140, 40)


def hole_center(index):
    """Restituisce le coordinate (x, y) del centro del buco i-esimo."""
    # TODO: calcolare la riga e la colonna corrispondenti all'indice
    # TODO: calcolare le dimensioni di una singola cella (larghezza e altezza) escludendo i margini
    # TODO: calcolare e restituire le coordinate del centro (cx, cy) per il buco
    row = index // GRID_COLS
    col = index % GRID_COLS
    cell_width = (WINDOW_WIDTH - 2 * GRID_MARGIN) / GRID_COLS
    cell_height = (WINDOW_HEIGHT - 2 * GRID_MARGIN) / GRID_ROWS
    cx = GRID_MARGIN + col * cell_width + cell_width / 2
    cy = GRID_MARGIN + row * cell_height + cell_height / 2

    return int(cx), int(cy)


class GameView:
    # TODO: definire costruttore __init__(self, screen) che memorizzi la superficie 'screen'

    # TODO: definire un metodo 'draw(self, model)' che:
    #       - riempie lo schermo con il colore di sfondo COLOR_BG
    #       - disegna un cerchio per ogni buco usando il colore appropriato in base allo stato
    #       - aggiorna la finestra di display (pygame.display.flip())
    def __init__(self, screen):
        self.screen = screen
    
    def draw(self, model):
        self.screen.fill(COLOR_BG)
        for i, hole in enumerate(model.holes):
            cx, cy = hole_center(i)
            color = COLOR_HOLE_ON if hole.is_active else COLOR_HOLE
            pygame.draw.circle(self.screen, color, (cx, cy), HOLE_RADIUS)
        pygame.display.flip()
