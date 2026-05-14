import pygame
import sys
import random
import time
from pygame.locals import *
pygame.init()

FPS = 60
clock = pygame.time.Clock()

black = pygame.Color(0, 0, 0)         
white = pygame.Color(255, 255, 255)   
grey = pygame.Color(128, 128, 128)   
red = pygame.Color(255, 0, 0)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SPEED = 5
SCORE = 0
COINS = 0

font = pygame.font.SysFont("Verdana", 80)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, white)
coin_font = font_small.render("Coins:", True, white)
points_font = font_small.render("Points:", True, white)
power_up = font.render("POWER UP", True, red)

background = pygame.image.load("clouds.jpg")
background = pygame.transform.scale_by(background, 3)


DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(white)


class bad_objects(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []
        bomb_image = pygame.image.load("bomb_cropped.png")
        bomb_image = pygame.transform.scale_by(bomb_image, .5)
        cheese_image = pygame.image.load("cheese_cropped.png")
        cheese_image = pygame.transform.scale_by(cheese_image, .5)
        self.images.append(bomb_image)
        self.images.append(cheese_image)
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(0,800),0)
 
    def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 820):
            self.rect.top = 0
            self.rect.center = (random.randint(0, 800), 0)
 
class good_objects(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.images = []
        for i in range(1,7):
             image = pygame.image.load(f"candy{i}_cropped.png")
             image = pygame.transform.scale_by(image, .5)
             self.images.append(image)
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(0,800),0) 
 
    def move(self):
        self.rect.move_ip(0,SPEED)
        if self.rect.top > 820:
            self.rect.top = 0
            self.rect.center = (random.randint(0, 800), 0)

class coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("coin_cropped.png")
        self.image = pygame.transform.scale_by(self.image, .5)
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(0,800),0) 
    def move(self):
        self.rect.move_ip(0,SPEED)
        if self.rect.top > 820:
            self.rect.top = 0
            self.rect.center = (random.randint(0, 800), 0)


class jar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("jar_cropped.png")
        # self.image = pygame.transform.scale_by(self.image, .5)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 680)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.rect.left > -200:
                  self.rect.move_ip(-10, 0)
        if pressed_keys[K_RIGHT] and self.rect.right < 1000:        
                  self.rect.move_ip(10, 0)
def cover():
            DISPLAYSURF.blit(background, (0,0))
            DISPLAYSURF.blit(coin_font, (10,10))
            DISPLAYSURF.blit(points_font, (10,30))
            scores = font_small.render(str(SCORE), True, white)
            DISPLAYSURF.blit(scores, (80,30))
            coin = font_small.render(str(COINS), True, white)
            DISPLAYSURF.blit(coin, (75,10))


         
J1 = jar()
B1 = bad_objects()
G1 = good_objects()
C1 = coins()
N1 = True

 
bads = pygame.sprite.Group()
bads.add(B1)
goods = pygame.sprite.Group()
goods.add(G1)
money = pygame.sprite.Group()
money.add(C1)
nothing = pygame.sprite.Group()


all_sprites = pygame.sprite.Group()
all_sprites.add(B1)
all_sprites.add(G1)
all_sprites.add(J1)
all_sprites.add(C1)


INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2000)

while True:
    DISPLAYSURF.blit(background, (0,0))
    DISPLAYSURF.blit(coin_font, (10,10))
    DISPLAYSURF.blit(points_font, (10,30))
    scores = font_small.render(str(SCORE), True, white)
    DISPLAYSURF.blit(scores, (80,30))
    coin = font_small.render(str(COINS), True, white)
    DISPLAYSURF.blit(coin, (75,10))
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5
           
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    if pygame.sprite.spritecollideany(J1, bads):
        DISPLAYSURF.fill(black)
        print(SCORE)
        DISPLAYSURF.blit(game_over, (225,250))
        DISPLAYSURF.blit(scores, (385, 320))
        pygame.display.update()
        for sprite in all_sprites:
                sprite.kill() 
        time.sleep(4)
        pygame.quit()
        sys.exit()        
    if pygame.sprite.spritecollideany(J1, goods):
        SCORE += 1
        G1.image = random.choice(G1.images)
        G1.rect.top = 0
        G1.rect.center = (random.randint(0,800),0)
    if pygame.sprite.spritecollideany(J1, money):
        COINS += 1
        C1.rect.top = 0
        C1.rect.center = (random.randint(0,800),0)
        if COINS == 5:
            DISPLAYSURF.blit(power_up, (200,250))
    pygame.display.update()
    clock.tick(FPS)

    pygame.display.update()




# if pygame.sprite.spritecollideany(J1, bads):

# make a class of enemies and a class of candy and a class of coins

# create the movement for the candy jar
    
# randomly pick things falling from both classes

# keep score

