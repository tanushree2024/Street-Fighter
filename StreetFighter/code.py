import pygame
import random

width = 1200
height = 600
screen = pygame.display.set_mode((width,height))

black = 0,0,0
white = 255,255,255
red = 255,0,0
color_1 = 100,105,150

class Spritesheet():

    def __init__(self, file_name):
        pygame.sprite.Sprite.__init__(self)
        self.spriteSheet = file_name

    def getImage(self, x, y, width, height):

        image = pygame.Surface((width, height))
        image.blit(self.spriteSheet, (0,0), (x, y, width, height))
        image.set_colorkey(black)

        return image

class Player(pygame.sprite.Sprite):
    standingFrames = []
    kickFrames = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        spritesheet = Spritesheet(ken)
        self.image = spritesheet.getImage(48,246,109,240)
        self.standingFrames.append(self.image)
        self.image = spritesheet.getImage(265,241,109,247)
        self.standingFrames.append(self.image)
        self.image = spritesheet.getImage(481,245,109,243)
        self.standingFrames.append(self.image)
        self.image = spritesheet.getImage(687,246,109,242)
        self.standingFrames.append(self.image)

        self.image = spritesheet.getImage(250, 1451, 118, 250)
        self.kickFrames.append(self.image)
        self.image = spritesheet.getImage(428, 1457, 208, 248)
        self.kickFrames.append(self.image)
        self.image = spritesheet.getImage(676, 1461, 120, 244)
        self.kickFrames.append(self.image)

        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = height - 300
        self.pos = 0

        self.stand = True
        self.kick = False

    def update(self):
        self.pos += 2

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_SPACE]:
            self.kick = True
            self.stand = False
        else:
            self.kick = False
            self.stand = True

        if self.stand:
            frame = self.pos // 30 % len(self.standingFrames)
            self.image = self.standingFrames[frame]
        elif self.kick:
            frame = self.pos // 30 % len(self.kickFrames)
            self.image = self.kickFrames[frame]

background = pygame.image.load("img/background.png")
ken = pygame.image.load("img/ken_.png")

all_sprites = pygame.sprite.Group()
player_1 = Player()
player_2 = Player()
all_sprites.add(player_1)
# all_sprites.add(player_2)

FPS = 100
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.blit(background, (0,0))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.update()
    clock.tick(FPS)