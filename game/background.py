# game/background.py — fundo com scroll infinito.

import pygame

from constants import SCREEN_W


class Background:
    """Fundo com scroll infinito — offset avança e reseta via módulo."""

    def __init__(self, image: pygame.Surface, tile_w: int):
        self._img    = image
        self._tile_w = tile_w
        self._offset = 0.0

    def update(self, speed: float, dt: float) -> None:
        self._offset = (self._offset + speed * dt) % self._tile_w

    def draw(self, surface: pygame.Surface) -> None:
        x = -self._offset
        while x < SCREEN_W:
            surface.blit(self._img, (int(x), 0))
            x += self._tile_w
