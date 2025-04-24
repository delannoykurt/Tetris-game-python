import pygame
import sys

# Initialisation
pygame.init()

# Constantes
CELL_SIZE = 30
COLS = 10
ROWS = 20
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE
FPS = 10

# Couleurs
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
GRAY = (40, 40, 40)

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris Retro")
clock = pygame.time.Clock()

# Exemple de Tetromino (forme I)
tetromino = [[4, 0], [5, 0], [6, 0], [7, 0]]  # positions x, y sur la grille

def draw_grid():
    for x in range(COLS):
        for y in range(ROWS):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)

def draw_tetromino(tetromino):
    for block in tetromino:
        x, y = block
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, CYAN, rect)

# Boucle principale
running = True
while running:
    screen.fill(BLACK)
    draw_grid()
    draw_tetromino(tetromino)

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
