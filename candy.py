import pygame
import sys
import random
import time
from pygame.locals import *
pygame.init()

power_start = 0
power_end = 5000
power_word_start = 0
power_word_end = 1000
word = False
thing= False
FPS = 60
clock = pygame.time.Clock()
new_jar = False
power = False
shoot = False
ba = False

balls = 0

black = pygame.Color(0, 0, 0)         
white = pygame.Color(255, 255, 255)   
grey = pygame.Color(128, 128, 128)   
red = pygame.Color(255, 0, 0)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SPEED = 5
SPEED2 = -5
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
    pygame.display.update()
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
            self.image = random.choice(self.images)
            self.rect.top = 0
            self.rect.center = (random.randint(0, 800), 0)
 
class good_objects(pygame.sprite.Sprite):
    pygame.display.update()
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
    pygame.display.update()
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
    pygame.display.update()
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("jar_cropped.png")
        self.rect = self.image.get_rect()
        self.rect.center = (400, 700)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.rect.left > 0:
                  self.rect.move_ip(-10, 0)
        if pressed_keys[K_RIGHT] and self.rect.right < 800:        
                  self.rect.move_ip(10, 0)
class shielded_jar(pygame.sprite.Sprite):
    pygame.display.update()
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("shielded_jar_cropped.png")
        self.rect = self.image.get_rect()
        self.rect.center = (400, 700)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.rect.left > 0:
                  self.rect.move_ip(-10, 0)
        if pressed_keys[K_RIGHT] and self.rect.right < 800:        
                  self.rect.move_ip(10, 0)

class shield(pygame.sprite.Sprite):
    pygame.display.update()
    def __init__(self):
         super().__init__()
         self.image = pygame.image.load("shield_cropped.png")
         self.image = pygame.transform.scale_by(self.image, .5)
         self.rect = self.image.get_rect()
         self.rect.center=(random.randint(0,800),0)
    def move(self):
        self.rect.move_ip(0,SPEED)
        if self.rect.top > 820:
            self.rect.top = 0
            self.rect.center = (random.randint(0, 800), 0)
class balls(pygame.sprite.Sprite):
    pygame.display.update()
    def __init__(self):
        super().__init__()
        self.images = []
        ball1_image = pygame.image.load("ball1_cropped.png")
        ball1_image = pygame.transform.scale_by(ball1_image, .5)
        ball2_image = pygame.image.load("ball2_cropped.png")
        ball2_image = pygame.transform.scale_by(ball2_image, .5)
        self.images.append(ball1_image)
        self.images.append(ball2_image)
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(0,800),0)

        self.shooting = False

    def shoot(self, x, y):
        self.rect.center = (x, y)
        self.shooting = True

    def move(self):
        if power == False:
            self.rect.move_ip(0,SPEED)
            if self.rect.top > 820:
                self.rect.top = 0
                self.rect.center = (random.randint(0, 800), 0)
        elif self.shooting:
            self.rect.move_ip(0, -10)
        else:
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_LEFT] and self.rect.left > 0:
                    self.rect.move_ip(-10, 0)
            if pressed_keys[K_RIGHT] and self.rect.right < 800:        
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
S1 = shield()
J2 = shielded_jar()
P1 = balls()

ball = pygame.sprite.Group()
ball.add(P1)
bads = pygame.sprite.Group()
bads.add(B1)
goods = pygame.sprite.Group()
goods.add(G1)
money = pygame.sprite.Group()
money.add(C1)
nothing = pygame.sprite.Group()
shields = pygame.sprite.Group()
shields.add(S1)


all_sprites = pygame.sprite.Group()
all_sprites.add(B1)
all_sprites.add(G1)
all_sprites.add(J1)
all_sprites.add(C1)


INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2000)
pygame.display.update()

while True:
    pygame.display.update()
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
    
    if new_jar == False and pygame.sprite.spritecollideany(J1, bads):
        DISPLAYSURF.fill(black)
        print(SCORE)
        DISPLAYSURF.blit(game_over, (175,250))
        DISPLAYSURF.blit(scores, (380, 350))
        pygame.display.update()
        for sprite in all_sprites:
                sprite.kill() 
        time.sleep(4)
        pygame.quit()
        sys.exit()
    if new_jar == True:
        if pygame.sprite.spritecollideany(J2, bads):
            B1.rect.top = 0
            J2.kill()
            all_sprites.add(J1)
            J1.rect.center = J2.rect.center
            new_jar = False
    candy_collide = pygame.sprite.spritecollideany(J1, goods)
    if candy_collide:
        SCORE += 1
        candy_collide.image = random.choice(candy_collide.images)
        candy_collide.rect.top = 0
        candy_collide.rect.center = (random.randint(0,800),0)
    if new_jar == True:
        candy_collide = pygame.sprite.spritecollideany(J2, goods)
        if candy_collide:
            SCORE += 1
            candy_collide.image = random.choice(candy_collide.images)
            candy_collide.rect.top = 0
            candy_collide.rect.center = (random.randint(0,800),0)

    if pygame.sprite.spritecollideany(J1, money):
        COINS += 1
        C1.rect.top = 0
        C1.rect.center = (random.randint(0,800),0)
        if COINS == 5 and thing == False:
                thing = True
                # word = True
                power_start = pygame.time.get_ticks()
                # power_word_start = pygame.time.get_ticks()
                DISPLAYSURF.blit(power_up, (200,250))
                for i in range(4):
                    power_candy = good_objects()
                    goods.add(power_candy)
                    all_sprites.add(power_candy)
    if new_jar == True:
        if pygame.sprite.spritecollideany(J2, money):
            COINS += 1
            C1.rect.top = 0
            C1.rect.center = (random.randint(0,800),0)
            if COINS == 5 and thing == False:
                    thing = True
                    # word = True
                    power_start = pygame.time.get_ticks()
                    # power_word_start = pygame.time.get_ticks()
                    DISPLAYSURF.blit(power_up, (200,250))
                    for i in range(4):
                        power_candy = good_objects()
                        goods.add(power_candy)
                        all_sprites.add(power_candy)
    if COINS >= 13:
         ba = True
         for thing in ball:
            DISPLAYSURF.blit(thing.image, thing.rect)
            thing.move()
    if new_jar == False:
        if pygame.sprite.spritecollideany(J1, ball):
            P1.rect.centerx = J1.rect.centerx
            P1.rect.bottom = J1.rect.top
            power = True
    if new_jar == True:
        if pygame.sprite.spritecollideany(J2, ball):
            P1.rect.centerx = J2.rect.centerx
            P1.rect.bottom = J2.rect.top
            power = True
    if power == True:
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE] and not P1.shooting:
            if new_jar == False:
                P1.shoot(J1.rect.centerx, J1.rect.centery)
            else:
                P1.shoot(J2.rect.centerx, J2.rect.centery) 
    if pygame.sprite.spritecollideany(P1, bads) and ba == True:
        P1.kill()
        B1.kill()
        B1 = bad_objects()
        bads = pygame.sprite.Group()
        bads.add(B1)
        all_sprites.add(B1)
        ba = False

    # if word == True:
    #      power_word_length = pygame.time.get_ticks()
    #      if power_word_length - power_word_start > power_word_end:
    #           word=False
    if thing == True:
        power_length = pygame.time.get_ticks()
        if power_length - power_start > power_end:
            thing = False
            for candy in goods.sprites()[1:]:
                candy.kill()
    if COINS >= 10: 
        for thing in shields:
            DISPLAYSURF.blit(thing.image, thing.rect)
            thing.move()
    if pygame.sprite.spritecollideany(J1, shields):
         J1.kill()
         S1.kill()
         all_sprites.add(J2)
         J2.rect.center = J1.rect.center
         new_jar = True

                            
    pygame.display.update()
    clock.tick(FPS)

    pygame.display.update()


