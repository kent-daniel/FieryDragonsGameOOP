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
from Win import Win


class Game:
    def __init__(self, data_controller: GameDataController,
                 screen: pygame.surface.Surface):
        """
        :param data_controller:
        :param screen:

        initilising object fields
        """
        self.winner = None
        self.screen_width, self.screen_height = pygame.display.get_desktop_sizes()[0]
        self._data_controller = data_controller
        self._screen = screen
        self._is_running: bool = True
        self.initialise_game()
        self.render_game()

    def render_game(self):
        """
        rendering the components of the game
        :return: the components on a GUI
        """
        self._draw_dragon_cards()
        self._draw_board()
        self._draw_notification_tab()
        if self.winner is not None:
            self.win = Win(self.winner)
            self.win.render_win(self._screen, self._screen.get_rect().topleft)

    def _draw_board(self):
        """
        draws the board onto the screen
        :return: None
        """
        self._board.draw(self._screen, self._screen.get_rect().center)

    def _draw_dragon_cards(self):
        """
        places the dragon cards on the the screen (GUI)
        :return: None

        """
        self._dragon_cards.draw(self._screen, self._screen.get_rect().center)

    def _draw_notification_tab(self):
        """
        Draws notificatin Tab onto the screen
        :return: None
        """
        self._notification_tab.draw(self._screen,
                                    self._screen.get_rect().topleft)

    @property
    def is_running(self):
        """
        check if still running
        :return: Boolean
        """
        return self._is_running

    def end_game(self):
        """
        end's the game by changing running to false
        :return: None
        """
        self._is_running = False

    def handle_events(self):
        """
        handles different events within the game
        :return: None
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                card = self._dragon_cards.get_clicked_card(
                    pygame.mouse.get_pos())
                if card:
                    self._handle_chosen_card(card)
            if self._check_winner():
                self.winner = self._player_turn_controller.get_current_player()

    def _handle_chosen_card(self, card: DragonCard):
        """
        :param card:
        :return:
        processes the movements of the player based on the dragon card they pick
        """
        current_player = self._player_turn_controller.get_current_player()
        self._player_move_controller.process_movement(current_player,card)

    def _check_winner(self):
        """
        check if the player has reached their initial cave
        :return: True if the player has reached their cave otherwise False
        """
        current_player = self._player_turn_controller.get_current_player()
        if current_player.steps_to_win == 0:
            return True

    def initialise_game(self):
        """
        initilises the different graphical components, managers and controllers of the game
        :return: None
        """
        self._setup_data()
        self._setup_views()
        self._movement_manager: IMovementEventManager = MovementEventManager()
        self._player_turn_controller: IPlayerTurnController = PlayerTurnController(
            self._player_data_controller)
        self._player_move_controller: IPlayerMoveController = PlayerMoveController(
            self._movement_manager,
            self._player_data_controller)
        self._movement_manager.add_listener(self._board)
        self._movement_manager.add_listener(self._dragon_cards)
        self._movement_manager.add_listener(self._player_turn_controller)

    def _setup_views(self) -> None:
        """
            seting up the graphical components of the game
        :return:
        """
        self._board = Board(int(self._screen.get_width() * 0.7),
                            self._screen.get_height(),
                            self._player_data_controller)
        self._dragon_cards = DragonCardsGroup(
            self._dragon_cards_data_controller)
        self._notification_tab = NotificationTabUI()

    def _setup_data(self) -> None:
        """
        Setting up the data controllers for player and dragon card
        :return: None
        """
        self._player_data_controller: IPlayerDataController = self._data_controller.create_player_data_controller()
        self._dragon_cards_data_controller: IDragonCardDataController = self._data_controller.create_dragon_card_data_controller()

    def quit(self) -> None:
        """
        used to quit the game, by quiting pygame
        :return: None
        """
        self.end_game()
        pygame.quit()
