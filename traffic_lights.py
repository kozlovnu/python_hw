import sys
import time
import pygame

class Traffic_lights:

    __color = ''

    def green_light(self,color: str):
        WIN_WIDTH = 200
        WIN_HEIGHT = 400
        WHITE = (255, 255, 255)
        red = (255, 0, 0)
        yellow = (225, 225, 0)
        green = (0, 200, 64)
        black = (0, 0, 0)

        self.sc = pygame.display.set_mode(
            (WIN_WIDTH, WIN_HEIGHT))

        r = 40
        x = 100
        y = WIN_HEIGHT // 4
        while 1:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()

            if color == 'green':
                self.sc.fill(WHITE)
                pygame.draw.rect(self.sc, black, (25, 20, 150, 350), 8)
                pygame.draw.circle(self.sc, red, (x, y), r)
                pygame.draw.circle(self.sc, yellow, (x, y * 2), r, 8)
                pygame.draw.circle(self.sc, green, (x, y * 3), r, 8)
                pygame.display.update()
                time.sleep(3)

                self.sc.fill(WHITE)
                pygame.draw.rect(self.sc, black, (25, 20, 150, 350), 8)
                pygame.draw.circle(self.sc, red, (x, y), r)
                pygame.draw.circle(self.sc, yellow, (x, y * 2), r)
                pygame.draw.circle(self.sc, green, (x, y * 3), r, 8)
                pygame.display.update()
                time.sleep(3)

                self.sc.fill(WHITE)
                pygame.draw.rect(self.sc, black, (25, 20, 150, 350), 8)
                pygame.draw.circle(self.sc, red, (x, y), r, 8)
                pygame.draw.circle(self.sc, yellow, (x, y * 2), r, 8)
                pygame.draw.circle(self.sc, green, (x, y * 3), r)
                pygame.display.update()
                time.sleep(3)
                break
                # self.__color = 'red'
            else:
                self.sc.fill(WHITE)
                pygame.draw.rect(self.sc, black, (25, 20, 150, 350), 8)
                pygame.draw.circle(self.sc, red, (x, y), r,8)
                pygame.draw.circle(self.sc, yellow, (x, y * 2), r,8)
                pygame.draw.circle(self.sc, green, (x, y * 3), r)
                pygame.display.update()
                time.sleep(3)

                self.sc.fill(WHITE)
                pygame.draw.rect(self.sc, black, (25, 20, 150, 350), 8)
                pygame.draw.circle(self.sc, red, (x, y), r,8)
                pygame.draw.circle(self.sc, yellow, (x, y * 2), r)
                pygame.draw.circle(self.sc, green, (x, y * 3), r, 8)
                pygame.display.update()
                time.sleep(3)

                self.sc.fill(WHITE)
                pygame.draw.rect(self.sc, black, (25, 20, 150, 350), 8)
                pygame.draw.circle(self.sc, red, (x, y), r)
                pygame.draw.circle(self.sc, yellow, (x, y * 2), r,8)
                pygame.draw.circle(self.sc, green, (x, y * 3), r, 8)
                pygame.display.update()
                time.sleep(3)
                break
                # self.__color = 'green'


a = Traffic_lights()
a.green_light('red')
# a.green_light('green')
