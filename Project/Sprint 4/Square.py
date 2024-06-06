from typing import Tuple, Optional, Dict
import pygame
from GameConstants import CharacterImage, GameElementStyles, GameStyles
from Cave import Cave
from Tile import Tile
from IDecodable import IDecodable
from Player import Player


class Square(Tile, IDecodable):

    def __init__(self, id: int, character: CharacterImage,
                 width: int = GameElementStyles.SQUARE_LENGTH.value,
                 height: int = GameElementStyles.SQUARE_LENGTH.value,
                 cave: Optional[Cave] = None,
                 occupant: Optional[Player] = None) -> None:
        super().__init__(id, character, width, height, occupant)
        self._cave: Optional[Cave] = cave
        self._rect = None
        self._image: pygame.Surface = pygame.image.load(self._character.value).convert_alpha()
        self._image = pygame.transform.smoothscale(self._image, (self.width * 0.8, self.height * 0.8))
        self._square_surface: pygame.Surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self._combined_surface: pygame.Surface = self._square_surface
        self.redraw_view()

    def redraw_view(self) -> None:
        self._rect: pygame.Rect = self._combined_surface.get_rect()
        self._draw_square()
        if self._cave:
            self._draw_cave()
        if self._occupant:
            self._draw_player()

    def is_cave(self) -> bool:
        return False

    @property
    def cave(self) -> Optional[Cave]:
        return self._cave

    def _draw_square(self) -> None:
        square_colour = self._occupant.colour if self._occupant is not None else GameStyles.COLOR_BROWN_LIGHT.value
        pygame.draw.rect(self._square_surface,
                         square_colour,
                         self._square_surface.get_rect(),
                         border_radius=GameStyles.BORDER_RADIUS_MEDIUM.value
                         )

        self._square_surface.blit(self._image, self._image.get_rect(
            center=(self._square_surface.get_width() // 2, self._square_surface.get_height() // 2)))
        self._combined_surface.blit(self._square_surface, self._rect.topleft)

    def _draw_cave(self) -> None:
        if self._cave is None: return
        self._cave.draw(self._combined_surface,
                        (self._rect.centerx, self._rect.centery + GameElementStyles.CAVE_OFFSET.value))

    def _draw_player(self) -> None:
        if self._occupant is None: return
        self._occupant.draw(self._combined_surface, self._rect.midtop)

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        self._rect.topleft = location
        destination_surface.blit(self._combined_surface, self._rect.topleft)

    def get_surface(self) -> pygame.Surface:
        return self._combined_surface

    def set_cave(self, cave: Cave) -> None:
        self._combined_surface = pygame.Surface(
            (self.width, self.height + self._cave.get_surface().get_rect().height), pygame.SRCALPHA)
        self._cave = cave

    @staticmethod
    def decode_from_json(json_data: Dict) -> 'IDecodable':
        return Square(json_data["id"],
                      CharacterImage[json_data["animal"]],
                      occupant=Player.decode_from_json(json_data["occupant"]) if json_data["occupant"] else None ,
                      cave=Cave.decode_from_json(json_data["cave"]) if json_data["cave"] else None
                      )

    def encode_to_json(self) -> Dict:
        return {
            "id": self.id,
            "occupant": self.get_occupant().encode_to_json() if self.get_occupant() else None,
            "animal": self.character.name,
            "cave": self.cave.encode_to_json() if self.cave else None
        }
