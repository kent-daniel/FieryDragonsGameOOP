from typing import Tuple, Dict

import pygame.sprite
from Player import Player
from GameConstants import GameImage, GameElementStyles, CharacterImage
from Tile import Tile
from IDecodable import IDecodable
from typing import Optional

class Cave(Tile, IDecodable):

    def __init__(self,
                 id: int,
                 cave_owner: Player,
                 character: CharacterImage,
                 image: str = GameImage.CAVE.value,
                 occupant: Optional[Player] = None,
                 height: int = GameElementStyles.CAVE_SIZE.value, width: int = GameElementStyles.CAVE_SIZE.value):
        super().__init__(id, character, width, height , occupant)

        self._cave_owner = cave_owner
        self._surface: pygame.Surface = pygame.Surface((height, width), pygame.SRCALPHA)
        self._image: pygame.Surface = pygame.image.load(image).convert_alpha()
        self._image = pygame.transform.smoothscale(self._image, (width, height))
        self._character_image: pygame.Surface = pygame.image.load(character.value).convert_alpha()
        self._character_image = pygame.transform.smoothscale(self._character_image, (width*0.6, height*0.6))
        self.height = height
        self.width = width

        print(self.get_occupant())

    def get_owner(self):
        return self._cave_owner

    def get_surface(self) -> pygame.Surface:
        return self._surface

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        self.redraw_view()
        self._rect.center = location
        destination_surface.blit(self._surface, self._rect.topleft)

    def redraw_view(self) -> None:
        self._rect: pygame.Rect = self._surface.get_rect()
        self._surface.blit(self._image, self._image.get_rect(center=(self.height // 2, self.width // 2)))
        pygame.draw.circle(self._surface,
                           self._cave_owner.colour,
                           self._rect.center,
                           radius=self.height // 2,  # Radius (slightly larger than the cave)
                           width=5)
        # draw character image on top of cave image
        character_rect = self._character_image.get_rect(center=self._rect.center)
        self._surface.blit(self._character_image, character_rect.topleft)
        if self.get_occupant().id == self._cave_owner.id:
            self._draw_player()

    def is_cave(self) -> bool:
        return True

    @staticmethod
    def decode_from_json(json_data: Dict) -> 'IDecodable':
        return Cave(json_data["id"],
                    Player.decode_from_json(json_data["owner"]),
                    CharacterImage[json_data["animal"]],
                    occupant=Player.decode_from_json(json_data["occupant"]) if json_data["occupant"] else None
                    )

    def encode_to_json(self) -> Dict:
        return {
            "id": self.id,
            "owner": self.get_owner().encode_to_json(),
            "occupant": self.get_occupant().encode_to_json() if self.get_occupant() else None,
            "animal": self.character.name
        }

    def _draw_player(self) -> None:
        if self._occupant is None: return
        self._occupant.draw(self._surface, self._rect.midtop)

