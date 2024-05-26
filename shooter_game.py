#подключение модулей
from pygame import *
from random import randint
from time import time as timer
#класс игрового обьекта
class GameSprite(sprite.Sprite):
    def __init__(self, xcor, ycor, width, height, speed, picture):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(picture),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = xcor
        self.rect.y = ycor
        self.speed = speed
    #передвежение игрока
    def hero_run(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x <850:
            self.rect.x += self.speed
    #перемещение пули
    def bullet_go(self):
        self.rect.y -= self.speed
        if self.rect.y < -10:
            self.kill()
    #перемещение врага
    def enemy_go(self):
        self.rect.y += self.speed
    #отображение обьектов
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
#создание окна
window = display.set_mode((900,600))
display.set_caption('Шутер')
background = transform.scale(image.load('galaxy.jpg'),(900,600))
#создание музыки
'''mixer.init()
mixer.music.load('space.ogg')
mixer.music.play(-1)'''
#создание обьектов
hero = GameSprite(450,500,50,50,15,'rocket.png')
enemy = GameSprite(randint(50,850),0,50,50,randint(3,5),'ufo.png')
enemy2 = GameSprite(randint(50,850),0,50,50,randint(1,7),'asteroid.png')
enemy3 = GameSprite(randint(50,850),0,50,50,randint(3,5),'ufo.png')
enemy4 = GameSprite(randint(50,850),0,50,50,randint(1,7),'asteroid.png')
enemy5 = GameSprite(randint(50,850),0,50,50,randint(1,7),'asteroid.png')
enemy6 = GameSprite(randint(50,850),0,50,50,randint(1,7),'asteroid.png')
enemy7 = GameSprite(randint(50,850),0,50,50,randint(1,7),'asteroid.png')
enemy8 = GameSprite(randint(50,850),0,50,50,randint(1,7),'asteroid.png')
enemies = [enemy,enemy2,enemy3,enemy4,enemy5,enemy6,enemy7,enemy8]
bullets = sprite.Group()
#создание переменных
lives = 15
kills = 0
seconds = 60
#команда вывода текста
font.init()
font1 = font.Font(None,50)

start = timer()
#игровой цикл
game = True
while game:
    stop = timer()
    #вывод текста
    window.blit(background, (0,0))
    lives_text = font1.render('Жизни:' + str(lives),1,(255,255,255))
    window.blit(lives_text, (10,10))
    kills_text = font1.render('Убийства:' + str(kills),1,(255,255,255))
    window.blit(kills_text, (10,60))
    seconds_text = font1.render('Осталось:' + str(seconds),1,(255,255,255))
    window.blit(seconds_text, (10,110))
    
    if stop - start > 1:
        seconds -= 1
        start = stop
    #привязка клавиш
    for ev in event.get():
        if ev.type == QUIT:
            game = False
        if ev.type == KEYDOWN:
            if ev.key == K_r:
                lives = 17
                kills = 0
                seconds = 60
                for enemy in enemies:
                    enemy.rect.y = -10
                    enemy.rect.x = randint(50,850)
                    enemy.speed = randint(5,8)
            if ev.key == K_SPACE:
                bullet = GameSprite(hero.rect.x + 20, hero.rect.y, 10,20,15,'bullet.png')
                bullets.add(bullet)
    
    for bullet in bullets:
        bullet.bullet_go()

    #победы и поражения
    if lives <= 0 or seconds == 0 and kills < 115:
        for enemy in enemies:
            enemy.speed = 0
        seconds = 60
        lose_text = font1.render('Вы проиграли',1,(255,255,255))
        window.blit(lose_text, (350,300))
        for bullet in bullets:
            bullet.kill()
        restart_text = font1.render('Нажмите R,чтобы начать заного',1,(255,255,255))
        window.blit(restart_text,(250,350))

    if kills >= 150 and lives > 0:
        for enemy in enemies:
            enemy.speed = 0
        seconds = 60
        win_text = font1.render('Вы выиграли',1,(255,255,255))
        window.blit(win_text, (350,300))
        for bullet in bullets:
            bullet.kill()
        restart_text = font1.render('Нажмите R,чтобы начать заного',1,(255,255,255))
        window.blit(restart_text,(250,350))


    if kills >= 115 and lives > 0 and seconds == 0:
        for enemy in enemies:
            enemy.speed = 0
        seconds = 60
        win_text = font1.render('Вы выиграли',1,(255,255,255))
        window.blit(win_text, (350,300))
        for bullet in bullets:
            bullet.kill()
        restart_text = font1.render('Нажмите R,чтобы начать заного',1,(255,255,255))
        window.blit(restart_text,(250,350))

    #убийства врагов
    for enemy in enemies:
        for bullet in bullets:
            if sprite.collide_rect(enemy,bullet):
                enemy.rect.y = 10
                enemy.rect.x = randint(50,860)
                bullet.kill()
                kills = kills + 1
    #отнятие жизней
    for enemy in enemies:
        if sprite.collide_rect(hero,enemy):
            lives -= 1
            enemy.rect.x = randint(50,850)
            enemy.rect.y = 10
            kills += 1

    if enemy.rect.y > 600:
        enemy.rect.y = 10
        enemy.rect.x = randint(50,850)
        enemy.speed = randint(2,5)
        lives = lives - 1
    if enemy2.rect.y > 600:
        enemy2.rect.y = 10
        enemy2.rect.x = randint(50,850)
        enemy2.speed = randint(1,6)
        lives = lives - 1
    if enemy3.rect.y > 600:
        enemy3.rect.y = 10
        enemy3.rect.x = randint(50,850)
        enemy3.speed = randint(2,5)
        lives = lives - 1
    if enemy4.rect.y > 600:
        enemy4.rect.y = 10
        enemy4.rect.x = randint(50,850)
        enemy4.speed = randint(1,6)
        lives = lives - 1
    if enemy5.rect.y > 600:
        enemy5.rect.y = 10
        enemy5.rect.x = randint(50,850)
        enemy5.speed = randint(1,6)
        lives = lives - 1
    if enemy6.rect.y > 600:
        enemy6.rect.y = 10
        enemy6.rect.x = randint(50,850)
        enemy6.speed = randint(1,6)
        lives = lives - 1
    if enemy7.rect.y > 600:
        enemy7.rect.y = 10
        enemy7.rect.x = randint(50,850)
        enemy7.speed = randint(1,6)
        lives = lives - 1
    if enemy8.rect.y > 600:
        enemy8.rect.y = 10
        enemy8.rect.x = randint(50,850)
        enemy8.speed = randint(1,6)
        lives = lives - 1
    

    hero.hero_run()
    enemy.enemy_go()
    enemy2.enemy_go()
    enemy3.enemy_go()
    enemy4.enemy_go()
    enemy5.enemy_go()
    enemy6.enemy_go()
    enemy7.enemy_go()
    enemy8.enemy_go()
    hero.reset()
    enemy.reset()
    enemy2.reset()
    enemy3.reset()
    enemy4.reset()
    enemy5.reset()
    enemy6.reset()
    enemy7.reset()
    enemy8.reset()
    bullets.draw(window)
    display.update()
    time.delay(50)