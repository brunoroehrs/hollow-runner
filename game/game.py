# game/game.py — loop principal, eventos, update e draw.

import sys
import pygame

from constants import (
    SCREEN_W, SCREEN_H, FPS, GROUND_Y,
    INITIAL_SPEED, SPEED_CAP, SPEED_INC,
    SPAWN_INTERVAL_MAX, SPAWN_INTERVAL_MIN,
    COLOR_GROUND, COLOR_GROUND_LINE,
)
from entities import Player, Enemy, EntityFactory
from .assets import load_assets
from .background import Background
from .hud import draw_playing_hud, draw_title, draw_dead_screen


class Game:
    """Orquestra o loop, eventos, update e draw."""

    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        pygame.display.set_caption("Hollow Runner")
        self._clock  = pygame.time.Clock()

        self._assets  = load_assets()
        self._factory = EntityFactory(self._assets)
        self._bg      = Background(self._assets["bg"], self._assets["bg_w"])

        self._record = 0
        self._state  = "title"
        self._setup_run()

    def _setup_run(self) -> None:
        """Reinicia apenas o que precisa ser zerado a cada nova tentativa."""
        self._player         = Player(self._assets["knight"])
        self._enemies        : list[Enemy] = []
        self._distance       = 0.0
        self._speed          = INITIAL_SPEED
        self._spawn_timer    = 0.0
        self._spawn_interval = SPAWN_INTERVAL_MAX

    def run(self) -> None:
        while True:
            dt = self._clock.tick(FPS) / 1000.0
            self._handle_events()
            self._update(dt)
            self._draw()

    # --- eventos ---

    def _handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == pygame.KEYDOWN:
                key = event.key
                if self._state == "title":
                    if key in (pygame.K_SPACE, pygame.K_w, pygame.K_UP):
                        self._state = "playing"
                elif self._state == "playing":
                    if key in (pygame.K_SPACE, pygame.K_w, pygame.K_UP):
                        self._player.jump()
                elif self._state == "dead":
                    if key == pygame.K_SPACE:
                        self._setup_run()
                        self._state = "playing"

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s and self._state == "playing":
                    self._player.release_down()

    # --- update ---

    def _update(self, dt: float) -> None:
        if self._state in ("playing", "title"):
            bg_speed = self._speed if self._state == "playing" else INITIAL_SPEED
            self._bg.update(bg_speed, dt)

        if self._state != "playing":
            return

        if pygame.key.get_pressed()[pygame.K_s]:
            self._player.hold_down()

        self._speed    = min(self._speed + SPEED_INC * dt, SPEED_CAP)
        self._distance += (self._speed / INITIAL_SPEED) * dt * 60

        t = (self._speed - INITIAL_SPEED) / (SPEED_CAP - INITIAL_SPEED)
        self._spawn_interval = SPAWN_INTERVAL_MAX - t * (SPAWN_INTERVAL_MAX - SPAWN_INTERVAL_MIN)

        self._player.update(dt, self._speed)

        self._spawn_timer += dt
        if self._spawn_timer >= self._spawn_interval:
            self._spawn_timer = 0.0
            self._enemies.append(self._factory.create())

        for e in self._enemies:
            e.update(dt, self._speed)
        self._enemies = [e for e in self._enemies if e.active]

        prect = self._player.get_rect().inflate(-10, -10)
        for e in self._enemies:
            if e.get_rect().colliderect(prect):
                self._player.kill()
                dist_int = int(self._distance)
                if dist_int > self._record:
                    self._record = dist_int
                self._state = "dead"
                return

    # --- draw ---

    def _draw(self) -> None:
        self._bg.draw(self._screen)

        pygame.draw.rect(self._screen, COLOR_GROUND,
                         pygame.Rect(0, GROUND_Y, SCREEN_W, SCREEN_H - GROUND_Y))
        pygame.draw.line(self._screen, COLOR_GROUND_LINE,
                         (0, GROUND_Y), (SCREEN_W, GROUND_Y), 2)

        for e in self._enemies:
            e.draw(self._screen)
        self._player.draw(self._screen)

        self._draw_hud()
        pygame.display.flip()

    def _draw_hud(self) -> None:
        dist = int(self._distance)
        if self._state == "title":
            draw_title(self._screen, self._record)
        elif self._state == "playing":
            draw_playing_hud(self._screen, dist, self._record)
        elif self._state == "dead":
            draw_dead_screen(self._screen, dist, self._record)
