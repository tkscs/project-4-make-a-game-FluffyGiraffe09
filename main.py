import pygame
import sys
import random, time
from pygame.locals import *
pygame.init()

FPS = 60
clock = pygame.time.Clock()

black = pygame.Color(0, 0, 0)         # Black
white = pygame.Color(255, 255, 255)   # White
grey = pygame.Color(128, 128, 128)   # Grey
red = pygame.Color(255, 0, 0)       # Red


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)

background = pygame.image.load("Untitled design.png")
background = pygame.transform.scale_by(background, .4)


DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(white)
pygame.display.set_caption("Game")




class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.image = pygame.transform.scale_by(self.image, .5)
        self.rect = self.image.get_bounding_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 
 
    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.image = pygame.transform.scale_by(self.image, .5)
        self.rect = self.image.get_bounding_rect()
        self.rect.center = (160, 520)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if pressed_keys[K_LEFT] and self.rect.left > -200:
                  self.rect.move_ip(-10, 0)
        if pressed_keys[K_RIGHT] and self.rect.right < 800:        
                  self.rect.move_ip(10, 0)
  
         
P1 = Player()
E1 = Enemy()
 
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2000)



while True:
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, black)
    DISPLAYSURF.blit(scores, (10,10))
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 1
           
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        DISPLAYSURF.fill(red)
        print(SCORE)
        DISPLAYSURF.blit(game_over, (130,250))
        DISPLAYSURF.blit(scores, (300, 280))
        pygame.display.update()
        for entity in all_sprites:
                entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()        

         
    pygame.display.update()
    clock.tick(FPS)

    pygame.display.update()

