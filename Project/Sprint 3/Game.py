import pygame
from Board import Board
from Player import Player
from GameDataController import GameDataController
from DragonCardsGroup import DragonCardsGroup
from DragonCard import DragonCard
from PlayerMoveController import IPlayerMoveController, PlayerMoveController
from MovementEventManager import IMovementEventManager, MovementEventManager
from PlayerTurnController import IPlayerTurnController, PlayerTurnController
from GameDataController import IPlayerDataController, IDragonCardDataController
from Movement import Movement
from NotificationTabUI import NotificationTabUI


class Game:
    def __init__(self, data_controller: GameDataController, screen: pygame.surface.Surface):
        self._data_controller = data_controller
        self._screen = screen
        self._is_running: bool = True
        self.initialise_game()
        self.render_game()

    def render_game(self):
        self._draw_dragon_cards()
        self._draw_board()
        self._draw_notification_tab()

    def _draw_board(self):
        self._board.draw(self._screen, self._screen.get_rect().center)

    def _draw_dragon_cards(self):
        self._dragon_cards.draw(self._screen, self._screen.get_rect().center)

    def _draw_notification_tab(self):
        self._notification_tab.draw(self._screen , self._screen.get_rect().topleft)

    @property
    def is_running(self):
        return self._is_running

    def end_game(self):
        self._is_running = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                card = self._dragon_cards.get_clicked_card(pygame.mouse.get_pos())
                if card:
                    self._handle_chosen_card(card)

    def _handle_chosen_card(self, card: DragonCard):
        current_player = self._player_turn_controller.get_current_player()
        current_player_location = self._player_move_controller.get_player_location(current_player)
        final_movement = self._player_move_controller.process_movement(current_player_location,
                                                                       current_player,
                                                                       card.action(current_player_location))

    def _check_winner(self, current_player: Player, movement: Movement):
        pass

    def initialise_game(self):
        self._setup_data()
        self._setup_views()
        self._movement_manager: IMovementEventManager = MovementEventManager()
        self._player_turn_controller: IPlayerTurnController = PlayerTurnController(self._player_data_controller)
        self._player_move_controller: IPlayerMoveController = PlayerMoveController(self._movement_manager,
                                                                                   self._player_data_controller)
        self._movement_manager.add_listener(self._board)
        self._movement_manager.add_listener(self._dragon_cards)
        self._movement_manager.add_listener(self._player_turn_controller)

    def _setup_views(self) -> None:
        self._board = Board(int(self._screen.get_width() * 0.7), self._screen.get_height(),
                            self._player_data_controller)
        self._dragon_cards = DragonCardsGroup(self._dragon_cards_data_controller)
        self._notification_tab = NotificationTabUI()

    def _setup_data(self) -> None:
        self._player_data_controller: IPlayerDataController = self._data_controller.create_player_data_controller()
        self._dragon_cards_data_controller: IDragonCardDataController = self._data_controller.create_dragon_card_data_controller()

    def quit(self) -> None:
        self.end_game()
        pygame.quit()
