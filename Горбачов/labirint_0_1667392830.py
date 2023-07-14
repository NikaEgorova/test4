from pygame import *
 

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
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)

        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    def update(self): 
        if player1.rect.x <= win_width-80 and player1.x_speed > 0 or player1.rect.x >= 0 and player1.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left) 
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        if player1.rect.y <= win_height-80 and player1.y_speed > 0 or player1.rect.y >= 0 and player1.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, 15)
        bullets.add(bullet)

class Enemy(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, start_x1, start_x2):

        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
        self.start_x1=start_x1
        self.start_x2=start_x2


    def update(self):
        if self.rect.x <= self.start_x1: 
            self.side = "right"
        if self.rect.x >= self.start_x2:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    #рух ворога
    def update(self):
        self.rect.x += self.speed
        # зникає, якщо дійде до краю екрана
        if self.rect.x > win_width+10:
            self.kill()

win_width = 1280
win_height = 720
display.set_caption("Лабіринт")
window = display.set_mode((win_width, win_height))
back = transform.scale(image.load('background.jpg'), (1280, 720))

barriers = sprite.Group()
bullets = sprite.Group()
monsters = sprite.Group()

w1 = GameSprite('platform2.png',0,0,30,720)
w2 = GameSprite('platform2.png', 150, 520, 250, 30)
w3 = GameSprite('platform2.png',150,550,30,200)
w4 = GameSprite('platform2.png',1250,0,30,720)
w5 = GameSprite('platform2.png',370,520,30,100)
w6 = GameSprite('platform2.png', 30, 380, 500, 30)
w7 = GameSprite('platform2.png', 500, 380, 30, 240)
w8 = GameSprite('platform2.png', 650, 280, 30, 340)
w9 = GameSprite('platform2.png', 650, 590, 200, 30)
w10 = GameSprite('platform2.png', 820, 590, 30, 150)
w11 = GameSprite('platform2.png', 140, 250, 250, 30)
w12 = GameSprite('platform2.png', 140, 110, 30, 140)
w13 = GameSprite('platform2.png', 510, 250, 345, 30)
w14 = GameSprite('platform2.png', 270, 110, 750, 30)
w15 = GameSprite('platform2.png', 650, -30, 30, 140)
w16 = GameSprite('platform2.png', 30, 110, 110, 30)
w17 = GameSprite('platform2.png', 1000, 110, 30, 150)
w18 = GameSprite('platform2.png', 850, 380, 180, 30)
w19 = GameSprite('platform2.png', 820, 380, 30, 100)
w20 = GameSprite('platform2.png', 820, 450, 430, 30)


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
barriers.add(w15)
barriers.add(w16)
barriers.add(w17)
barriers.add(w18)
barriers.add(w19)
barriers.add(w20)

player1 = Player('hero.png', 35, win_height - 100, 80, 80, 0, 0)
monster1 = Enemy('enemy.png', 160, 180, 60, 60, 2, 180, 950)
monster2 = Enemy('enemy.png', 250, 650, 60, 60, 2, 190, 760)
monster3 = Enemy('enemy.png', 770, 290, 60, 60, 2, 700, 1200)
monster4 = Enemy('enemy.png', 1000, 530, 60, 60, 4, 680, 1200)
monster5 = Enemy('enemy.png', 250, 650, 60, 60, 2, 190, 760)
final_sprite = GameSprite('final.png', win_width - 115, win_height - 75, 80, 80)


monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)
monsters.add(monster5)

finish = False
run = True
while run:
 
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                player1.x_speed = -3
            elif e.key == K_RIGHT:
                player1.x_speed = 3
            elif e.key == K_UP:
                player1.y_speed = -3
            elif e.key == K_DOWN:
                player1.y_speed = 3
            elif e.key == K_SPACE:
                player1.fire()
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                player1.x_speed = 0
            elif e.key == K_RIGHT:
                player1.x_speed = 0
            elif e.key == K_UP:
                player1.y_speed = 0
            elif e.key == K_DOWN:
                player1.y_speed = 0
    if not finish:
        window.blit(back,(0,0))
        barriers.draw(window)
    
        final_sprite.reset()
        player1.reset()
        bullets.update()
        player1.update()
        bullets.draw(window)
        barriers.draw(window)

        sprite.groupcollide(monsters, bullets, True, True)
        monsters.update()
        monsters.draw(window)
        sprite.groupcollide(bullets, barriers, True, False)
        if sprite.spritecollide(player1, monsters, False):
            finish = True
            img = image.load('dead.png')
            d = img.get_width() // img.get_height()
            window.fill((0, 0, 0))
            window.blit(transform.scale(img, (win_height * d, win_height)), (250, 10))

        if sprite.collide_rect(player1, final_sprite):
            finish = True
            img = image.load('end.jpg')
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
    
        time.delay(5)
        display.update()