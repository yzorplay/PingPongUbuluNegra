from pygame import *
import math
import random
window = display.set_mode((700, 500))
display.set_caption('Пинг понг убили негра')
color = (0, 0, 0)
window.fill(color)
font.init()
final = False

p1s = 10
p2s = 10
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
            sound_generator.play_sound(222, 0.1)
        
        if self.x >= pl2.x - 20 and self.y >= pl2.y and self.y <= pl2.y + pl2.sy and self.x <= pl2.x:
            self.mx *= -1
            self.mx *= 1.6
            self.my *= 1.6
            sound_generator.play_sound(333, 0.1)
        elif self.x <= pl.x + 20 and self.y >= pl.y and self.y <= pl.y + pl.sy and self.x >= pl.x:
            self.mx *= -1
            self.mx *= 1.6
            self.my *= 1.6
            sound_generator.play_sound(444, 0.1)

        if self.x >= pl2.x + 80:
            p1s -= 1
            b.x = 350
            b.y = 250
            #b.mx *= -1
            self.mx = random.randint(-4, 4)
            self.my = random.randint(-4, 4)
            if self.mx == 0 or self.mx == -1 or self.mx == 1:
                self.mx = random.randint(-4, 4)
                self.my = random.randint(-4, 4)
            sound_generator.play_sound(80, 0.1, sound_generator.play_sound, (80, 0.1))
        elif self.x <= pl.x - 80:
            p2s -= 1
            b.x = 350
            b.y = 250
            #b.mx *= -1
            self.mx = random.randint(-4, 4)
            self.my = random.randint(-4, 4)
            if self.mx == 0 or self.mx == -1 or self.mx == 1:
                self.mx = random.randint(-4, 4)
                self.my = random.randint(-4, 4)
            sound_generator.play_sound(80, 0.1, sound_generator.play_sound, (80, 0.1))
        
        if p1s == 0:
            winer = "справо"
            luser = "слева"
            final = True
        elif p2s == 0:
            winer = "слево"
            luser = "справо"
            final = True



class PixelSoundGenerator:
    def __init__(self, sample_rate=44100, volume=0.2, num_channels=8):
        self.sample_rate = sample_rate
        self.volume = volume
        mixer.init(frequency=self.sample_rate, size=-16, channels=1)  # Инициализируем mixer
        mixer.set_num_channels(num_channels)  # Устанавливаем количество каналов
        self.channels = [mixer.Channel(i) for i in range(num_channels)]
        self.channel_callbacks = {} # Словарь для хранения коллбэков для каждого канала

    def generate_pixel_sound(self, frequency, duration):
        num_samples = int(self.sample_rate * duration)
        wave_data = []
        for i in range(num_samples):
            # Прямоугольная волна: 1, если sin(x) > 0, и -1, если sin(x) < 0
            sample = self.volume if math.sin(2 * math.pi * frequency * i / self.sample_rate) > 0 else -self.volume
            # Ограничиваем значения от -1 до 1
            sample = max(-1, min(1, sample))
            # Преобразуем значения от -1 до 1 в целые числа в диапазоне -32768 до 32767
            sample_value = int(sample * 32767)
            wave_data.append(sample_value)

        # Преобразуем в формат, понятный 
        sound_array = mixer.Sound(buffer=b''.join([sample.to_bytes(2, byteorder='little', signed=True) for sample in wave_data]))
        return sound_array

    def play_sound(self, frequency, duration, callback=None, callback_args=()):
        sound = self.generate_pixel_sound(frequency, duration)
        channel = self.find_available_channel()

        if channel:
            channel.play(sound)
            self.channel_callbacks[channel] = (callback, callback_args) # Сохраняем коллбэк для этого канала
            return channel
        else:
            print("Все каналы заняты!")
            return None

    def find_available_channel(self):
        for channel in self.channels:
            if not channel.get_busy():
                return channel
        return None

    def check_finished_channels(self):
        for channel, (callback, callback_args) in list(self.channel_callbacks.items()):
            if not channel.get_busy():  # Если канал свободен (звук закончился)
                if callback:
                    callback(*callback_args)  # Вызываем коллбэк
                del self.channel_callbacks[channel]  # Удаляем коллбэк из словаря

    def cleanup(self):
        mixer.quit()  # Выключаем mixer, когда он больше не нужен


sound_generator = PixelSoundGenerator() # Создаем экземпляр класса






b = Boll(350, 250, 2, -2)
pl = Player(60,-10, 20, 80)
pl2 = Player(620,-10, 20, 80)


FPS = 60
clock = time.Clock()
finish = True
game = True
while game:
    sound_generator.check_finished_channels()
    window.fill(color)
    if not final:
        b.blit()
        b.move()
        pl.blit()
        pl2.blit()
        #text1 = f.render(str(p1s), True, (180, 0, 0))
        #text2 = f.render(str(p2s), True, (180, 0, 0))
        #window.blit(text1, (100, 50))
        #window.blit(text2, (600, 50))

        for i in range(p2s):
            rectanos = Rect(5, 480 - i * 20, 50, 10)
            draw.rect(window, (255, 0, 0), rectanos)
        for i in range(p1s):
            rectanos = Rect(645, 480 - i * 20, 50, 10)
            draw.rect(window, (255, 0, 0), rectanos)


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