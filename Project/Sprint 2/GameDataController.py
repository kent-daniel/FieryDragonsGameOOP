from PlayerDataController import IPlayerDataController, PlayerDataController
from DragonCardDataController import IDragonCardDataController, DragonCardDataController

config = {
    "player_count": "4",
    "square_animals": 'BABY_DRAGON ,BAT ,SPIDER ,SALAMANDER ,SPIDER ,BAT ,SPIDER ,SALAMANDER ,BABY_DRAGON ,BAT ,BAT ,BABY_DRAGON ,SALAMANDER ,BABY_DRAGON ,SPIDER ,BABY_DRAGON ,SALAMANDER ,BAT ,SALAMANDER ,BABY_DRAGON ,BAT ,BAT ,BABY_DRAGON ,SALAMANDER',
    "dragon_cards": '1xSALAMANDER,2xSALAMANDER,3xSALAMANDER,1xBAT,2xBAT,3xBAT,1xSPIDER,2xSPIDER,3xSPIDER,1xBABY_DRAGON,2xBABY_DRAGON,3xBABY_DRAGON,1xPIRATE,1xPIRATE,2xPIRATE,2xPIRATE'
}


class GameDataController:
    def __init__(self, config_path: str):
        # INFO: will implement reading config from file later
        self.config = config

    def _parse_config(self, config_path: str) -> None:
        # self.config = ConfigParser()
        # self.config.read(config_path)
        pass

    def create_player_data_controller(self) -> IPlayerDataController:
        return PlayerDataController(self.config['square_animals'], self.config['player_count'])

    def create_dragon_card_data_controller(self) -> IDragonCardDataController:
        return DragonCardDataController(self.config['dragon_cards'])
