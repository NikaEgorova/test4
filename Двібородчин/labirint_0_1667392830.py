from pygame import *

win_width = 1050
win_height = 700
display.set_caption("Лабіринт")
window = display.set_mode((win_width, win_height))
back = transform.scale(image.load('back.jpg'),(win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
        self.coins = None
        self.collected_coins = 0

    def update(self):
        if player.rect.x <= win_width - 80 and player.x_speed > 0 or player.rect.x >= 0 and player.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for platforms in platforms_touched:
                self.rect.right = min(self.rect.right, platforms.rect.left)
        elif self.x_speed < 0:
            for platforms in platforms_touched:
                self.rect.left = max(self.rect.left, platforms.rect.right)

        if player.rect.y <= win_height - 80 and player.y_speed > 0 or player.rect.y >= 0 and player.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for platforms in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, platforms.rect.top)
        elif self.y_speed < 0:
            for platforms in platforms_touched:
                self.rect.top = max(self.rect.top, platforms.rect.bottom)
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.right - 25, self.rect.centery - 16, 15, 20, 10)
        bullets.add(bullet)
    def fire2(self):
        bullet = Bullet('bullet.png', self.rect.left - 25, self.rect.centery - 16, 15, 20, -10)
        bullets.add(bullet)

class Enemy(GameSprite):
    side = 'left'
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self,player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def update(self):
        if self.rect.x <= 500:
            self.side = 'right'
        if self.rect.x >= win_width - 250:
            self.side = 'left'

        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Викликаємо конструктор GameSprite
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

    # рух ворога
    def update(self):
        self.rect.x += self.speed
        # зникає, якщо виходить за межі екрану
        if self.rect.x > win_width + 10:
            self.kill()

class Enemy1(GameSprite):
    side = 'left'

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def update(self):
        if self.rect.x <= 200:
            self.side = 'right'
        if self.rect.x >= win_width - 500:
            self.side = 'left'

        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy2(GameSprite):
    side = 'left'

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def update(self):
        if self.rect.x <= 80:
            self.side = 'right'
        if self.rect.x >= win_width - 510:
            self.side = 'left'

        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy3(GameSprite):
    side = 'up'

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def update(self):
        if self.rect.y <= 270:
            self.side = 'down'
        if self.rect.y >= 580:
            self.side = 'up'

        if self.side == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed            

class Enemy4(GameSprite):
    side = 'up'

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def update(self):
        if self.rect.y <= 170:
            self.side = 'down'
        if self.rect.y >= 420:
            self.side = 'up'
        
        if self.side == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed  

font.init()
font1 = font.SysFont('arial', 25)
coins_amount_1 = 0
kills_number = 0

class Coin(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)

#Створюємо групу для стін
barriers = sprite.Group()
bullets = sprite.Group()
#Створюємо стіни картинки
w1 = GameSprite('wall1.png', 400, 100, 400, 75)
w2 = GameSprite('wall2.png', 750, 0, 75, 550)
w3 = GameSprite('wall3.png', 200, 360, 450, 65)
w4 = GameSprite('wall4.png', 400, 365, 75, 375)
w5 = GameSprite('wall5.png', 0, 100, 250, 75)
w6 = GameSprite('wall6.png', 815, 100, 235, 75)
w7 = GameSprite('wall7.png', 0, 680, 1050, 20)
w8 = GameSprite('wall8.png', 0, 0, 1050, 20)
w9 = GameSprite('wall9.png', 0, 0, 15, 700)
w10 = GameSprite('wall10.png', 1035, 0, 15, 700)
w11 = GameSprite('wall11.png', 620, 500, 200, 60)
w12 = GameSprite('wall11.png', 210, 530, 140, 50)
w13 = GameSprite('wall4.png', 85, 260, 40, 340)
w14 = GameSprite('wall1.png', 85, 250, 520, 40)

#додаємо стіни до групи
barriers.add(w1)
barriers.add(w2) 
barriers.add(w3)
barriers.add(w4) 
barriers.add(w5)
barriers.add(w6) 
barriers.add(w7) 
barriers.add(w8) 
barriers.add(w9) 
barriers.add(w10) 
barriers.add(w11)
barriers.add(w12)
barriers.add(w13)
barriers.add(w14)

#створюємо спрайти
monsters = sprite.Group()

player = Player('skeleton.png', 35, win_height - 95, 70, 70, 0, 0)
monster = Enemy('vampire2.png', win_width - 300, 570, 80, 90, 4)
final_sprite = GameSprite('treasure.png', win_width - 220,win_height - 350, 120, 120)
monstr = Enemy1('vampire.png', 600, 290, 65, 70, 4)
monstryk = Enemy2('vampire2.png', 550, 25, 70, 70, 4)
b_w1 = Enemy1('wall13.png', 200, 400, 50, 160, 0)
b_w2 = Enemy1('wall14.png', 600, 20, 50, 100, 0)
mmonster = Enemy3('vampire.png', 890, 250, 80, 75, 4)
mmonsterr = Enemy4('vampire.png', 660, 230, 70, 70, 3)

monsters.add(monster)
monsters.add(monstr)
monsters.add(monstryk)
monsters.add(b_w1)
monsters.add(b_w2)
monsters.add(mmonster)
monsters.add(mmonsterr)

coin1 = Coin('coin.png', 310, 460, 40, 40)
coin2 = Coin('coin.png', 680, 50, 40, 40)
coin3 = Coin('coin.png', 50, 50, 40, 40)
coin4 = Coin('coin.png', 520, 460, 40, 40)
coin5 = Coin('coin.png', 910, 200, 40, 40)
coin6 = Coin('coin.png', 910, 585, 40, 40)

coins = sprite.Group()
coins.add(coin1)
coins.add(coin2)
coins.add(coin3)
coins.add(coin4)
coins.add(coin5)
coins.add(coin6)

mixer.init()
mixer.music.load('game.mp3')
mixer.music.play()

win = False
run = True
while run:
    time.delay(17)
    window.blit(back,(0,0))

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_w:
                player.y_speed = -5
            elif e.key == K_s:
                player.y_speed = 5
            elif e.key == K_a:
                player.x_speed = -5
            elif e.key == K_d:
                player.x_speed = 5
            elif e.key == K_RIGHT:
                player.fire()
            elif e.key == K_LEFT:
                player.fire2()
        elif e.type == KEYUP:
            if e.key == K_w:
                player.y_speed = 0
            elif e.key == K_s:
                player.y_speed = 0
            elif e.key == K_a:
                player.x_speed = 0
            elif e.key == K_d:
                player.x_speed = 0
    if not win:
        bullets.draw(window)
        monsters.draw(window)
        bullets.update()
        player.reset()
        player.update()
        barriers.draw(window)
        coins.draw(window)

        if sprite.groupcollide(monsters, bullets, True, True):
            kills_number += 1
        monsters.update()
        monsters.draw(window)
        sprite.groupcollide(bullets, barriers, True, False)

        if sprite.spritecollide(player, coins, True):
            coins_amount_1 += 1
        coin = font1.render(f'Зібрано монет : {coins_amount_1}', True, (241, 231, 70))
        window.blit(coin, (830, 35))
        kills = font1.render(f'Вбито ворогів : {kills_number}', True, (165, 0, 0))
        window.blit(kills, (830, 60))

        if sprite.spritecollide(player, monsters, False):
            win = True
            img = image.load('lose.jpg')
            window.blit(transform.scale(img, (win_width, win_height)), (0,0))

        if coins_amount_1 == 6 and len(monsters)==0:
            final_sprite.reset()

            if sprite.collide_rect(player, final_sprite):
                win = True
                img = image.load('win.jpg')
                window.blit(transform.scale(img, (win_width, win_height)), (0,0))

        display.update()