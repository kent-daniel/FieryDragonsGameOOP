import pygame
import math

TIMEREVENT = pygame.USEREVENT + 1


class TimerController:
    def __init__(self):
        self.time = 16
        self.clock = pygame.time.Clock()
        self.start_ticks = pygame.time.get_ticks()

    def get_time(self):
        time = math.floor(self.time - (pygame.time.get_ticks() - self.start_ticks) / 1000)
        if time < 1:
            self.start_ticks = pygame.time.get_ticks()
            return " " + str(0) + " "
        elif time < 10:
            time = " 0" + str(time) + ""
            return time
        else:
            return " " + str(time) + " "

    def update_time(self):
        self.start_ticks = pygame.time.get_ticks()
