import pygame
import random

width = 1000
height = 500
screen = pygame.display.set_mode((width,height))

black = 0,0,0
white = 255,255,255
red = 255,0,0
color_1 = 100,105,150

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        # self.center = (width/2, height/2)
        self.moveX = random.randint(0, 4)
        self.moveY = random.randint(0, 4)

    def update(self):
        self.rect.x += self.moveX
        self.rect.y += self.moveY

        if self.rect.right > width:
            self.moveX = random.randint(-4, -1)
        elif self.rect.bottom > height:
            self.moveY = random.randint(-4, -1)
        elif self.rect.left < 0:
            self.moveX = random.randint(0, 4)
        elif self.rect.top < 0:
            self.moveY = random.randint(0, 4)

all_sprites = pygame.sprite.Group()
player_1 = Player()
player_2 = Player()
all_sprites.add(player_1)
# all_sprites.add(player_2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    # screen.blit(player.img, (player.rect.x, player.rect.y))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.update()