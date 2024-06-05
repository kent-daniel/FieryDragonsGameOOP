import pygame

TIMEREVENT = pygame.USEREVENT + 1


class TimerController:
    def __init__(self):
        self.time = 15000
        self.clock = pygame.time.Clock
        self.clock.tick()

    # def run_timer(self):
    #     pygame.time.set_timer(TIMEREVENT, 1000)

    def get_time(self):
        if self.clock.get_time() < self.time:
            return (self.time - self.clock.get_time()) / 1000
        else:

            self.clock.tick()
            return 0
