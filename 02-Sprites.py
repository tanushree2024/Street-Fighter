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
        self.rect.x = width/2 - 25
        self.rect.y = height - 100
        self.moveX = 0

    def update(self):
        self.rect.x += self.moveX

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            self.moveX = 4
        elif keypressed[pygame.K_LEFT]:
            self.moveX = -4
        else:
            self.moveX = 0

    def triggerBullet(self):
        bullet = Bullet(self.rect.x + 20, self.rect.top)
        all_sprites.add(bullet)
        bulletGroup.add(bullet)

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,width - 50)
        self.rect.y = random.randint(-height,0)
        self.moveY = random.randint(0,3)

    def update(self):
        self.rect.y += self.moveY

        if self.rect.top > height:
            self.rect.y = random.randint(-height, 0)
            self.rect.x = random.randint(0, width - 50)

class Bullet(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((4,10))
        # self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.color = 255,0,0
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.moveY = -10

    def update(self):
        self.rect.y += self.moveY

        if self.rect.top < 0:
            self.kill()


def playerHealth(barWidth):
    pygame.draw.rect(screen,black,[10,10,barWidth,15])

all_sprites = pygame.sprite.Group()
player_1 = Player()
playerGroup = pygame.sprite.Group()
all_sprites.add(player_1)

enemyGroup = pygame.sprite.Group()
for i in range(20):
    enemy = Enemy()
    enemyGroup.add(enemy)
    all_sprites.add(enemy)

bulletGroup = pygame.sprite.Group()

FPS = 100
clock = pygame.time.Clock()

health = 200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_1.triggerBullet()

    screen.fill(white)
    # screen.blit(player.img, (player.rect.x, player.rect.y))
    all_sprites.draw(screen)
    all_sprites.update()
    playerHealth(health)

    collision = pygame.sprite.spritecollide(player_1,enemyGroup,True)
    if collision:
        health -= 50

    hit = pygame.sprite.groupcollide(enemyGroup,bulletGroup,True,True)
    if hit:
        # print("Hit")
        pass

    pygame.display.update()
    clock.tick(FPS)