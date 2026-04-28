# entities/base.py — classe base abstrata para todos os objetos do jogo.

import pygame
from abc import ABC, abstractmethod


class GameObject(ABC):
    """Classe base abstrata para todos os objetos do jogo."""

    def __init__(self, x: float, y: float, w: int, h: int):
        self._x      = x
        self._y      = y
        self._w      = w
        self._h      = h
        self._active = True

    @property
    def x(self) -> float:     return self._x
    @property
    def y(self) -> float:     return self._y
    @property
    def active(self) -> bool: return self._active

    def deactivate(self) -> None:
        self._active = False

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(int(self._x), int(self._y), self._w, self._h)

    def is_offscreen(self) -> bool:
        return self._x + self._w < -10

    @abstractmethod
    def update(self, dt: float, speed: float) -> None: ...

    @abstractmethod
    def draw(self, surface: pygame.Surface) -> None: ...
