from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Пинг понг убили негра')
color = (0, 0, 0)
window.fill(color)
font.init()
final = False

p1s = 0
p2s = 0
winer = "слева"
luser = "вправа"


f = font.Font(None, 36)


class Player():
    def __init__(self, x, y, sx = 20, sy = 80):
        self.y = y
        self.x = x
        self.sx = sx
        self.sy = sy
    def blit(self):
        self.rect = Rect(self.x, 20+self.y, self.sx, self.sy)
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
        global p1s, p2s, final
        if self.y <= 0 or self.y >= 480:
            self.my *= -1
        
        if self.x >= pl2.x - 20 and self.y >= pl2.y and self.y <= pl2.y + pl2.sy:
            self.mx *= -1
            self.mx *= 1.6
            self.my *= 1.6
        elif self.x <= pl.x + 20 and self.y >= pl.y and self.y <= pl.y + pl.sy:
            self.mx *= -1
            self.mx *= 1.6
            self.my *= 1.6

        if self.x >= pl2.x + 30:
            p1s += 1
            b.x = 350
            b.y = 250
            b.mx *= -1
            self.mx = 2
            self.my = -2
        elif self.x <= pl.x - 30:
            p2s += 1
            b.x = 350
            b.y = 250
            b.mx *= -1
            self.mx = 2
            self.my = -2
        
        if p1s == 10:
            winer = "справо"
            luser = "слева"
            final = True
        elif p2s == 10:
            winer = "слево"
            luser = "справо"
            final = True








b = Boll(350, 250, 2, -2)
pl = Player(20,-10, 20, 80)
pl2 = Player(670,-10, 20, 80)


FPS = 60
clock = time.Clock()
finish = True
game = True
while game:
    window.fill(color)
    if not final:
        b.blit()
        b.move()
        pl.blit()
        pl2.blit()
        text1 = f.render(str(p1s), True, (180, 0, 0))
        text2 = f.render(str(p2s), True, (180, 0, 0))
        window.blit(text1, (100, 50))
        window.blit(text2, (600, 50))
        keys = key.get_pressed()
    else:
        text3 = f.render("игрок " + winer + " красава, игрок " + luser + " нубский лузер!", True, (180, 0, 0))
        window.blit(text3, (50, 250))
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