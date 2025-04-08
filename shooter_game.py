#Создай собственный Шутер!

from pygame import *
from random import *

x1 = randrange(50, 650)
y1 = 400
lost = 0
score = 0
max_lost = 5
num_fire = 0
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect_x = player_x
        self.rect_y = player_y
    def reset(self):
        window.blit(self.image, (self.rect_x, self.rect_y))

class Player(GameSprite):
    def update(self):
        if keys_pressed[K_RIGHT] and self.rect_x < 650:
            self.rect_x += self.speed
        if keys_pressed[K_LEFT] and self.rect_x > 0:
            self.rect_x -= self.speed
        if keys_pressed[K_UP] and self.rect_y > 300:
            self.rect_y -= self.speed
        if keys_pressed[K_DOWN] and self.rect_y < 400:
            self.rect_y += self.speed
    def fire(self):
        w = Bullet('bullet.png',self.rect.centerx, self.rect.top, 15, 20,-15)
        w.add(bullets)

        

class Enemy(GameSprite):
    def update(self):
        self.rect_y += self.speed
        global lost
        if self.rect_y > 500:
            self.rect_x = randint(80, 620)
            self.rect_y = 0
            lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect_y += self.speed
        if self.rect_y == 0:
            self.kill()

class Asteroid(GameSprite):
    def update():
        self.rect_y += self.speed
        global lost
        if rect.y > 500:
            self.rect_x = randint(80, 620)
            self.rect_y = 0


window = display.set_mode((700, 500))
display.set_caption('Arcanoid')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
time = time.Clock()
FPS = 60
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
pdd = Player('rocket.png', x1, y1, 0.2)
game = True
finnaly = False
monsters = sprite.Group()
font.init()
font2 = font.SysFont('Arial', 36)
font1 = font.SysFont('Arial', 36)
bullets = sprite.Group()
text_proi = font1.render('Вы проиграли!', 1, (255, 255, 255))

rel_time = False

for i in range(1, 6):
    monster = Enemy('ufo.png',0,randint(80, 620), 0.1)
    monsters.add(monster)

while game:
    keys_pressed = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == K_DOWN:
            if e.key == K_SPACE:
                pdd.fire()
    
    text = font2.render('Счет: '+ str(score), 1, (255, 255, 255))
    window.blit(text, (10,20))
    text_lose = font1.render('Пропущено: '+str(lost), 1, (255, 255, 255))
    window.blit(text_lose, (10, 50))

    if not finnaly:
        window.blit(background,(0, 0))

        pdd.update()
        monsters.update()
        bullets.update()
        pdd.reset()
        monsters.draw(window)
        bullets.draw(window)

        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score += 1
            monster = Enemy('ufo.png', randint(80, 620), -40, 80, 50, randint(1, 5))
            monsters.add(monster)
        if sprite.spritecollide(pdd, monsters, False) or lost >= max_lost:
            finnaly = True
            window.blit(text_proi, (200, 200))
        
    display.update()