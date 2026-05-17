from pygame import *
#mixer.init()
font.init()
import random
import os
import sys

font1 = font.Font(None, 70)
font2 = font.Font(None, 30)




def resourse_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)




bullets = sprite.Group()



lose = font1.render('YOU LOSE!!!', True, (255, 0, 0) )
win = font1.render('YOU WIN!!!', True, (255, 215, 0) )

window = display.set_mode((700, 500))
display.set_caption('Шутер')
background = transform.scale(image.load(resourse_path('galaxy.jpg')), (700, 500))

FPS = 60
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, name, width, heith, x, y, speed):
        super().__init__()
        self.name = name
        self.width = width
        self.heith = heith
        self.speed = speed
        self.image = transform.scale(image.load(resourse_path(self.name)), (self.width , self.heith))
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

monsters = sprite.Group()

for i in range(10):
    i = Enemy('ufo.png', 65, 50, random.randint(5, 630), -50, random.randint(1, 2))
    monsters.add(i)
    



missed = '0'

score = '0'


game = True
while game:

  
    if finish != True:
        window.blit(background, (0, 0))
        Heart.reset()
        Heart.move()
        for i in monsters:
            i.reset()
            i.movement()


        hits = sprite.groupcollide(monsters, bullets, True, True)
        missed = int(missed)
        if missed >= 15:
           window.blit(lose, (200, 200))
           finish = True
        missed = str(missed)

        score = int(score)
        if score >= 500:
           window.blit(win, (200, 200))
           finish = True
        score = str(score)


        missed1 = font2.render(('Пропущено: ' + missed + "/ 15"), True, (255, 255, 255) )
        score1 = font2.render(('Очки: ' + score + "/ 500"), True, (255, 255, 255) )


        window.blit(score1, (5, 5))
        window.blit(missed1, (5, 35))

        if len(monsters) < 10: 
            for i in range(10 - len(monsters)):
                i = Enemy('ufo.png', 65, 50, random.randint(5, 630), -50, random.randint(1, 2)) 
                monsters.add(i)

        key_pressed = key.get_pressed()

        for e in event.get():
            if e.type == KEYUP:
                if e.key == K_SPACE:
                    Heart.fire()
          
        for hit in hits:
            score = int(score)
            score += 1
            score = str(score)
            
                
        bullets.draw(window)
        bullets.update()  

        

    


    for e in event.get():
        if e.type == QUIT:
            game = False


    clock.tick(FPS)
    display.update()
