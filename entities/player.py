# entities/player.py — o cavaleiro controlado pelo jogador.

import pygame

from constants import GROUND_Y, GRAVITY, JUMP_FORCE, MAX_FALL_MULTI, FALL_ACCEL_RATE
from .base import GameObject


class Player(GameObject):
    """O cavaleiro."""

    ANIM_SPEED = 8

    def __init__(self, sprites: list[pygame.Surface]):
        self._sprites = sprites
        w, h = sprites[0].get_width(), sprites[0].get_height()
        super().__init__(100.0, float(GROUND_Y - h), w, h)

        self._vy         = 0.0
        self._on_ground  = True
        self._alive      = True
        self._frame      = 0
        self._anim_tick  = 0
        self._fall_multi = 1.0

    @property
    def alive(self) -> bool:
        return self._alive

    def kill(self) -> None:
        self._alive = False

    def jump(self) -> None:
        if self._on_ground:
            self._vy = JUMP_FORCE
            self._on_ground = False
            self._fall_multi = 1.0

    def hold_down(self) -> None:
        if not self._on_ground and self._vy > 0:
            self._fall_multi = min(self._fall_multi + FALL_ACCEL_RATE, MAX_FALL_MULTI)

    def release_down(self) -> None:
        self._fall_multi = 1.0

    def update(self, dt: float, speed: float) -> None:
        gravity_now = GRAVITY * (self._fall_multi if self._vy > 0 else 1.0)
        self._vy   += gravity_now
        self._y    += self._vy

        ground_limit = float(GROUND_Y - self._h)
        if self._y >= ground_limit:
            self._y, self._vy = ground_limit, 0.0
            self._on_ground   = True
            self._fall_multi  = 1.0

        if self._on_ground:
            self._anim_tick += 1
            if self._anim_tick >= self.ANIM_SPEED:
                self._anim_tick = 0
                self._frame = (self._frame + 1) % len(self._sprites)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self._sprites[self._frame], (int(self._x), int(self._y)))
