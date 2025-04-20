from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Пинг понг убили негра')
color = (0, 0, 0)
window.fill(color)

class Player():
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def blit(self):
        self.rect = Rect(self.x, 20+self.y, 20, 80)
        draw.rect(window, (0, 255, 0), self.rect)
class Boll():
    def __init__(self, x, y, mx, my):
        self.x = x
        self.y = y
        self.mx = mx
        self.my = my
        
    def blit(self):
        self.x+=self.mx
        self.y+=self.my

        self.rect = Rect(self.x, self.y, 20, 20)
        draw.rect(window, (0, 0, 255), self.rect)
    def move(self):
        
        if self.y == 0:
            self.my = 2
        elif self.y == 480:
            self.my = -2
        
        if self.x >= pl2.x and self.y >= 80+pl2.y and self.y <= 80+pl2.y:
            self.mx = -2
        elif self.x <= 10 and self.y >= 80+pl.y and self.y <= 80+pl.y:
            self.mx = 2








b = Boll(350, 250, 2, -2)
pl = Player(20,-10)
pl2 = Player(670,-10)


FPS = 60
clock = time.Clock()
finish = True
game = True
while game:
    window.fill(color)
    b.blit()
    b.move()
    pl.blit()
    pl2.blit()
    keys = key.get_pressed()
    if keys[K_s]:
        if pl.y < 400:
            pl.y += 5
    if keys[K_w]:
        if pl.y > -15:
            pl.y -= 5
    
    if keys[K_DOWN]:
        if pl2.y < 400:
            pl2.y += 5
    if keys[K_UP]:
        if pl2.y > -15:
            pl2.y -= 5

    if finish != True:
        window.blit((0, 0))

    for e in event.get():
            if e.type == QUIT:
                game = False
    clock.tick(FPS)
    display.update()