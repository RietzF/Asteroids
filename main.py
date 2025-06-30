import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import Shot
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable) 
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        for dr in drawable:
             dr.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        
        for ast in asteroids:
             if ast.collision(player1):
                  print("Game over!")
                  sys.exit(0)
             for bullet in shots:
                if ast.collision(bullet):
                     ast.split()
                     bullet.kill()

if __name__ == "__main__":
        main()