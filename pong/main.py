import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Pong")

    # Define window dimensions
    WIDTH = 800
    HEIGHT = 400

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    screen.fill((0,0,0))
    # Double buffering
    pygame.display.update()

    # Setup walls
    wall_color = pygame.Color("white")
    BORDER = 15
    WALLS = (pygame.Rect((0,0), (WIDTH, BORDER)), #top
            pygame.Rect((0,0), (BORDER, HEIGHT)), #left
            pygame.Rect((0,HEIGHT-BORDER), (WIDTH, BORDER))) #bottom

    # Draw walls
    for wall in WALLS:
        pygame.draw.rect(screen,wall_color,wall)

    # Update display
    pygame.display.update()

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

# Entrypoint
if __name__ == "__main__":
    main()