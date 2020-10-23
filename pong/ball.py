import pygame

class Ball:
    RADIUS = 10
    
    def __init__(self,x,y,display,vx=0,vy=0):
        # Basic properties
        self.x = x
        self.y = y
        self.display = display
        # Movement
        self.vx = vx
        self.vy = vy
    
    def draw(self,col):
        pygame.draw.circle(self.display, col, (self.x,self.y), self.RADIUS)
    
    def update(self,collisionRects):
    
        # Loop through all wall rects and test for collisions
        for rect in collisionRects:
            # Horizontal collision
            if rect.collidepoint((self.x + self.vx + ((1 if self.vx > 0 else -1) * self.RADIUS),self.y)):
                self.vx *= -1
            # Vertical collision
            if rect.collidepoint(self.x,(self.y + self.vy + ((1 if self.vy > 0 else -1) * self.RADIUS))):
                self.vy *= -1
        # Actually move
        self.x += self.vx
        self.y += self.vy