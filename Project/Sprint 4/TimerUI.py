from PlayerTurnController import PlayerTurnController
import pygame

class TimerUi:
    def __init__(self, player_turn_controller: PlayerTurnController):
        self._player_turn_controller = player_turn_controller
