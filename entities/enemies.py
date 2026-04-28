# entities/enemies.py — inimigos do jogo.

import math
import random
import pygame
from abc import abstractmethod

from constants import SCREEN_W, GROUND_Y
from .base import GameObject


class Enemy(GameObject):
    """Base para inimigos: movimento horizontal compartilhado."""

    def __init__(self, x: float, y: float, sprite: pygame.Surface):
        self._sprite    = sprite
        self._anim_tick = 0
        super().__init__(x, y, sprite.get_width(), sprite.get_height())

    def update(self, dt: float, speed: float) -> None:
        self._x        -= speed * dt
        self._anim_tick += 1
        if self.is_offscreen():
            self.deactivate()

    @abstractmethod
    def draw(self, surface: pygame.Surface) -> None: ...


class Crawlid(Enemy):
    """Rasteja pelo chão."""

    def __init__(self, sprite: pygame.Surface):
        h = sprite.get_height()
        super().__init__(float(SCREEN_W + 20), float(GROUND_Y - h), sprite)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self._sprite, (int(self._x), int(self._y)))

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(int(self._x) + 8, int(self._y) + 5,
                           self._w - 16, self._h - 8)


class Vengefly(Enemy):
    """Voa em altura variável."""

    def __init__(self, sprite: pygame.Surface):
        base_y = float(random.randint(60, GROUND_Y - 120))
        super().__init__(float(SCREEN_W + 20), base_y, sprite)
        self._base_y    = base_y
        self._phase     = random.uniform(0, math.tau)
        self._amplitude = random.uniform(8, 20)

    def update(self, dt: float, speed: float) -> None:
        super().update(dt, speed)
        self._y = self._base_y + math.sin(self._anim_tick * 0.06 + self._phase) * self._amplitude

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self._sprite, (int(self._x), int(self._y)))

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(int(self._x) + 6, int(self._y) + 6,
                           self._w - 12, self._h - 12)
