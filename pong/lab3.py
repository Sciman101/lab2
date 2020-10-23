import pygame
from paddle import Paddle
from ball import Ball
import random

def main():
    pygame.init()
    pygame.display.set_caption("Pong")

    # Define window dimensions
    WIDTH = 800
    HEIGHT = 400
    
    FPS = 60
    
    COLOR_FG = pygame.Color('white')
    COLOR_BG = pygame.Color('black')
    # Setup walls
    BORDER = 15
    WALLS = (pygame.Rect((0,0), (WIDTH, BORDER)), #top
            pygame.Rect((0,0), (BORDER, HEIGHT)), #left
            pygame.Rect((0,HEIGHT-BORDER), (WIDTH, BORDER))) #bottom
    # Ball constants
    BALL_SPD = 3

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    screen.fill((0,0,0))
    # Double buffering
    pygame.display.update()

    # Draw walls
    for wall in WALLS:
        pygame.draw.rect(screen,COLOR_FG,wall)
    
    # Initialize ball
    #TODO Random +- 45 degree ball speed
    ball = Ball(WIDTH - Ball.RADIUS,HEIGHT // 2,screen,vx=-BALL_SPD,vy=random.choice((-BALL_SPD,BALL_SPD)))
    ball.draw(COLOR_FG)

    # Update display
    pygame.display.update()

    # define a variable to control the main loop
    running = True

    # Define game clock
    clock = pygame.time.Clock()

    # main loop
    while running:
    
        # Update ball
        ball.draw(COLOR_BG)
        ball.update(WALLS)
        ball.draw(COLOR_FG)
        
        pygame.display.update()
    
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        
        clock.tick(FPS)

# Entrypoint
if __name__ == "__main__":
    main()