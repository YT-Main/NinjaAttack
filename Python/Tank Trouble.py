import pygame
import random
from os import path

img_path = path.join(path.dirname(__file__), "img")

WIDTH = 850
HEIGHT = 850
FPS = 60
global Score_1, Score_2
Score_1 = 0
Score_2 = 0

player_y = HEIGHT - 10
player_x = WIDTH / 2

player_2_x = WIDTH / 2
player_2_y = HEIGHT - 840

# Define colour
WHITE = (255, 222, 173)
Black = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = ( 0, 0, 255)
#Initialize pygame and create window

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NinjaAttack")
clock = pygame.time.Clock()


#player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        global player_y, player_x
        pygame.sprite.Sprite.__init__(self)
        self.image = player_1_img
        transColor = player_1_img.get_at((0,0))
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()
        self.rect.centerx = player_x
        self.rect.bottom = player_y
        self.speedy = 0
        self.speedx = 0
    def update(self):
        self.speedy = 0
        self.speedx = 0
        if self.rect.top <= HEIGHT/2:
            self.rect.y = HEIGHT - 10
            self.rect.x = WIDTH/2
        if self.rect.top >= 850:
            self.rect.y = HEIGHT - 10
            self.rect.x = WIDTH/2
        if self.rect.centerx <= 0:
            self.rect.y = HEIGHT - 10
            self.rect.x = WIDTH/2
        if self.rect.centerx >= 850:
            self.rect.y = HEIGHT - 10
            self.rect.x = WIDTH/2
        hit_b = pygame.sprite.spritecollide(player, bullets_2, False)
        if hit_b:
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
            print("hi")
        Key = pygame.key.get_pressed()
        if Key[pygame.K_w]:
            self.speedy = -5
            print("Confirmed_UP")
        if Key[pygame.K_x]:
            self.image = player_1_img_ATT
            transColor = player_1_img_ATT.get_at((0,0))
            self.image.set_colorkey(transColor)
        else:
            self.image = player_1_img
            transColor = player_1_img.get_at((0,0))
            self.image.set_colorkey(transColor)
        if Key[pygame.K_s]:
            print("Confirmed_DOWN")
            self.speedy = 5
        if Key[pygame.K_a]:
            print("Confirmed_LEFT")
            self.speedx = -5
            self.image = Left_img
            transColor = Left_img.get_at((0,0))
            self.image.set_colorkey(transColor)
#            self.image = pygame.transform.rotate(self.image, 5)
#            self.rect = pygame.transform.rotate(self.rect, 5)
        if Key[pygame.K_d]:
            print("Confirmed_RIGHT")
            self.speedx = 5
            self.image = Right_img
            transColor = Right_img.get_at((0,0))
            self.image.set_colorkey(transColor)
        self.rect.y += self.speedy
        self.rect.x += self.speedx

    def shoot(self):
        bullet = Bullets(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
#player 2
class Player_2(pygame.sprite.Sprite):
    def __init__(self):
        global player_2_x, player_2_y
        pygame.sprite.Sprite.__init__(self)
        self.image = player_2_img
        transColor = player_2_img.get_at((0,0))
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()
        self.rect.centerx = player_2_x
        self.rect.top = player_2_y
        self.speedy = 0
        self.speedx = 0
    def update(self):
        self.speedy = 0
        self.speedx = 0
        if self.rect.top <= 0:
            self.rect.y = HEIGHT - 790
            self.rect.x = WIDTH/2
        if self.rect.centerx <= 0:
            self.rect.y = HEIGHT - 790
            self.rect.x = WIDTH/2
        if self.rect.centerx >= 850:
            self.rect.y = HEIGHT - 790
            self.rect.x = WIDTH/2
        if self.rect.bottom >= HEIGHT/2:
            self.rect.y = HEIGHT - 790
            self.rect.x = WIDTH/2
        hit_a = pygame.sprite.spritecollide(player_2, bullets, False)
        if hit_a:
            self.rect.centerx = WIDTH / 2
            self.rect.top = HEIGHT - 840
            print("HI")
        Key = pygame.key.get_pressed()
        if Key[pygame.K_UP]:
            self.speedy = -5
            print("Confirmed_UP")
        if Key[pygame.K_SPACE]:
            self.image = player_2_img_ATT
            transColor = player_2_img_ATT.get_at((0,0))
            self.image.set_colorkey(transColor)
        else:
            self.image = player_2_img
            transColor = player_2_img.get_at((0,0))
            self.image.set_colorkey(transColor)
        if Key[pygame.K_DOWN]:
            print("Confirmed_DOWN")
            self.speedy = 5
        if Key[pygame.K_LEFT]:
            print("Confirmed_LEFT")
            self.speedx = -5
            self.image = Left_img
            transColor = Left_img.get_at((0,0))
            self.image.set_colorkey(transColor)
#            self.image = pygame.transform.rotate(self.image, 5)
#            self.rect = pygame.transform.rotate(self.rect, 5)
        if Key[pygame.K_RIGHT]:
            print("Confirmed_RIGHT")
            self.speedx = + 5
            self.image = Right_img
            transColor = Right_img.get_at((0,0))
            self.image.set_colorkey(transColor)
        self.rect.y += self.speedy
        self.rect.x += self.speedx

    def shoot_2(self):
        print("shot")
        bullet_2 = Bullets_2(self.rect.centerx, self.rect.bottom)
        all_sprites.add(bullet_2)
        bullets_2.add(bullet_2)


#Bullets:
class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_2_img
        transColor = bullet_2_img.get_at((0,0))
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -15
    def update(self,):
        global Score_2
        global player_2_x, player_2_y
        self.rect.y += self.speedy
        #kill if it moves off screen
        if self.rect.bottom < 0:
            self.kill()
        #Blocking with barrels
        Block = pygame.sprite.spritecollide(obsticle, bullets, False)
        if Block:
            self.kill()
        Block = pygame.sprite.spritecollide(obsticle_2,  bullets, False)
        if Block:
            self.kill()
        Block = pygame.sprite.spritecollide(obsticle_3, bullets, False)
        if Block:
            self.kill()
        Block = pygame.sprite.spritecollide(obsticle_4, bullets, False)
        if Block:
            self.kill()
        Block = pygame.sprite.spritecollide(obsticle_5, bullets, False)
        if Block:
            self.kill()
        hit = pygame.sprite.spritecollide(player_2, bullets, False)
        if hit:
            player_2_x = WIDTH/2
            player_2_y = HEIGHT - 840
            Score_2 += 1
            self.kill()




#Bullets_2
class Bullets_2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        transColor = bullet_img.get_at((0,0))
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x
        self.speedy = + 15
    def update(self,):
        global Score_1
        global player_y, player_x
        self.rect.y += self.speedy
        #kiff if it moves off screen
        if self.rect.bottom < 0:
            self.kill()
        Block = pygame.sprite.spritecollide(obsticle, bullets_2, False)
        if Block:
            self.kill()
        Block = pygame.sprite.spritecollide(obsticle_2, bullets_2, False)
        if Block:
            self.kill()
        Block = pygame.sprite.spritecollide(obsticle_3, bullets_2, False)
        if Block:
            self.kill()
        Block = pygame.sprite.spritecollide(obsticle_4, bullets_2, False)
        if Block:
            self.kill()
        Block = pygame.sprite.spritecollide(obsticle_5, bullets_2, False)
        if Block:
            self.kill()
        hit = pygame.sprite.spritecollide(player, bullets_2, False)
        if hit:
            Score_1 += 1
            print (Score_2)
            player_y = HEIGHT - 10
            player_x = WIDTH/2
            self.kill()

#Text
font_name = pygame.font.match_font('arial')
def point_1(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)
def point_2(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)
def gameover(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)
def gameover_2(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)
#Obsticles
class Obsticles(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = obsticle_img
        transColor = obsticle_img.get_at((0,0))
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/4
        self.rect.bottom = HEIGHT/ 4
class Obsticles_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = obsticle_img
        transColor = obsticle_img.get_at((0,0))
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()
        self.rect.centerx = ( 3 * WIDTH)/ 4
        self.rect.bottom = HEIGHT/ 4
class Obsticles_3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = obsticle_img
        transColor = obsticle_img.get_at((0,0))
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/ 4
        self.rect.bottom = (3 * HEIGHT)/ 4

class Obsticles_4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = obsticle_img
        transColor = obsticle_img.get_at((0,0))
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()
        self.rect.centerx = (3 * WIDTH)/ 4
        self.rect.bottom = (3 * HEIGHT)/ 4
class Obsticles_5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = obsticle_img
        transColor = obsticle_img.get_at((0,0))
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/ 2
        self.rect.bottom = HEIGHT/ 2

#loading all graphics
background = pygame.image.load(path.join("img", "Background.png")).convert()
background_rect = background.get_rect()
player_2_img = pygame.image.load(path.join("img", "Still_NINJA_2.png")).convert()
player_1_img = pygame.image.load(path.join("img", "Still_NINJA.png")).convert()
bullet_img = pygame.image.load(path.join("img", "Kunai.png")).convert()
bullet_2_img = pygame.image.load(path.join("img", "Kunai_2.png")).convert()
player_1_img_ATT = pygame.image.load(path.join("img", "Throwing_NINJA.png")).convert()
player_2_img_ATT = pygame.image.load(path.join("img", "Attack_NINJA_2.png")).convert()
obsticle_img = pygame.image.load(path.join("img", "Obsticle.png")).convert()
Right_img = pygame.image.load(path.join("img", "Right_NINJA.png")).convert()
Left_img = pygame.image.load(path.join("img", "Left_NINJA.png")).convert()
#All sprites stuffs
obsticle = Obsticles()
obsticle_2 = Obsticles_2()
obsticle_3 = Obsticles_3()
obsticle_4 = Obsticles_4()
obsticle_5 = Obsticles_5()

bullets = pygame.sprite.Group()
bullets_2 = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(obsticle_2)
all_sprites.add(obsticle_3)
all_sprites.add(obsticle_4)
all_sprites.add(obsticle_5)

all_sprites.add(obsticle)
player = Player()
player_2 = Player_2()
all_sprites.add(player)
all_sprites.add(player_2)
#Game Loop
running = True
while running:

    #kepp running at right speed
    clock.tick(FPS)
    #Process input (events)
    for event in pygame.event.get():
        #Check for window closing

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                player.shoot()
            if event.key == pygame.K_SPACE:
                player_2.shoot_2()
                print("confirmx")
    #Update
    all_sprites.update()
    #chech to see if the bullets hit anything
    hits = pygame.sprite.spritecollide(player_2, bullets, False)
    #Draw/ render
    screen.fill(WHITE)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    point_1(screen, str(Score_1), 30, WIDTH - 790, HEIGHT/2 - 40)

    point_2(screen, str(Score_2), 30, WIDTH - 790, HEIGHT/2 + 10)
    if Score_1 > 10:
        gameover(screen, str("Player 1 Wins"), 70, WIDTH/2 , HEIGHT/2)

    if Score_2 > 10:
        gameover_2(screen, str("Player 2 Wins"), 70, WIDTH/2 , HEIGHT/2)
    #*After* Drawing flip the screen
    pygame.display.flip()


pygame.quit()
