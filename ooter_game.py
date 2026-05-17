from pygame import *
#mixer.init()
font.init()
import random

font1 = font.Font(None, 70)
font2 = font.Font(None, 30)


missed = '0'

score = '0'


bullets = sprite.Group()



lose = font1.render('YOU LOSE!!!', True, (255, 0, 0) )
win = font1.render('YOU WIN!!!', True, (255, 215, 0) )

window = display.set_mode((700, 500))
display.set_caption('Шутер')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))

FPS = 60
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, name, width, heith, x, y, speed):
        super().__init__()
        self.name = name
        self.width = width
        self.heith = heith
        self.speed = speed
        self.image = transform.scale(image.load(self.name), (self.width , self.heith))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def __init__(self, name, width, heith, x, y, speed):
        super().__init__(name, width, heith, x, y, speed)
        self.sprite_center_x = self.rect.centerx
        self.sprite_top = self.rect.top
    def move(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key_pressed[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', 10, 20, self.rect.centerx, self.rect.top, 15)
        bullets.add(bullet)


class Bullet(GameSprite):
    def __init__(self, name, width, heith, x, y, speed):
        super().__init__(name, width, heith, x, y, speed)
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
        
        
                



class Enemy(GameSprite):
    def __init__(self, name, width, heith, x, y, speed):
        super().__init__(name, width, heith, x, y, speed)
        
    def movement(self):
            self.rect.y += self.speed
            if self.rect.y >= 630:
                global missed
                missed = int(missed)
                missed += 1
                missed = str(missed)
                self.rect.y = -50

finish = False

Heart = Player('rocket.png', 50, 70, 16, 425, 6)

monsters = []

for i in range(5):
    i = Enemy('ufo.png', 65, 50, random.randint(5, 630), -50, random.randint(1, 2))
    monsters.append(i)
    






game = True
while game:

  
    if finish != True:
        window.blit(background, (0, 0))
        Heart.reset()
        Heart.move()
        for i in monsters:
            i.reset()
            i.movement()


     
        missed1 = font2.render(('Пропущено: ' + missed), True, (255, 255, 255) )
        score1 = font2.render(('Очки: ' + score), True, (255, 255, 255) )


        window.blit(score1, (5, 5))
        window.blit(missed1, (5, 35))

        if len(monsters) < 5:
            for i in range(5 - len(monsters)):
                i = Enemy('ufo.png', 65, 50, random.randint(5, 630), -50, random.randint(1, 2))
                monsters.append(i)

        key_pressed = key.get_pressed()

        for event in pygame.event.get():
            if eveny.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    Heart.fire()


          
                
        bullets.draw(window)
        bullets.update()   


    


    for e in event.get():
        if e.type == QUIT:
            game = False


    clock.tick(FPS)
    display.update()
