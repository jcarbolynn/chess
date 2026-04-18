import pygame
def Board():
    print("I am the board")
    # Initialize Pygame
    pygame.init()
   
    WIDTH = 1000
    HEIGHT = 900

    screen = pygame.display.set_mode([WIDTH, HEIGHT])

    # Set up the game window
    # screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Chess")

    # Game loop
    running = True
    while running:
        for i in range(32):
            column = i % 4
            row = i // 4
            if row % 2 == 0:
                pygame.draw.rect(screen, 'light gray', [
                                600 - (column * 200), row * 100, 100, 100])
            else:
                pygame.draw.rect(screen, 'light gray', [
                                700 - (column * 200), row * 100, 100, 100])
            pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 100])
            pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5)
            pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         running = False

    # Quit Pygame
    pygame.quit()
    
    
# a-h
# 1-8