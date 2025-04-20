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
#class Boll():





pl = Player(20,-10)
pl2 = Player(670,-10)


FPS = 60
clock = time.Clock()
finish = True
game = True
while game:
    window.fill(color)
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