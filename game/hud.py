# game/hud.py — renderização da interface do jogador (HUD).

import pygame

from constants import (
    SCREEN_W, SCREEN_H,
    COLOR_UI, COLOR_RECORD, COLOR_DEAD_TITLE, COLOR_HINT, COLOR_SCORE,
)

_font_cache: dict = {}


def get_font(size: int, bold: bool = True) -> pygame.font.Font:
    key = (size, bold)
    if key not in _font_cache:
        _font_cache[key] = pygame.font.SysFont("consolas", size, bold=bold)
    return _font_cache[key]


def draw_text(surface: pygame.Surface, text: str, size: int,
              x: int, y: int, color: tuple,
              anchor: str = "topleft", bold: bool = True,
              shadow: bool = False) -> None:
    font = get_font(size, bold)
    if shadow:
        s = font.render(text, True, (0, 0, 0))
        surface.blit(s, s.get_rect(**{anchor: (x + 2, y + 2)}))
    surf = font.render(text, True, color)
    surface.blit(surf, surf.get_rect(**{anchor: (x, y)}))


def draw_playing_hud(surface: pygame.Surface, distance: int, record: int) -> None:
    draw_text(surface, f"{distance:05d} m",
              22, SCREEN_W - 20, 14, COLOR_SCORE, anchor="topright", shadow=True)
    if record > 0:
        draw_text(surface, f"REC {record:05d} m",
                  16, SCREEN_W - 20, 44, COLOR_RECORD, anchor="topright", shadow=True)


def draw_title(surface: pygame.Surface, record: int) -> None:
    panel = pygame.Surface((460, 110), pygame.SRCALPHA)
    panel.fill((0, 0, 0, 160))
    surface.blit(panel, (SCREEN_W // 2 - 230, SCREEN_H // 2 - 65))

    draw_text(surface, "HOLLOW RUNNER",
              38, SCREEN_W // 2, SCREEN_H // 2 - 52,
              (255, 220, 100), anchor="center", shadow=True)
    draw_text(surface, "ESPAÇO  para iniciar",
              20, SCREEN_W // 2, SCREEN_H // 2,
              COLOR_UI, anchor="center", shadow=True)
    draw_text(surface, "W / ↑ pula   •   S desce mais rápido",
              15, SCREEN_W // 2, SCREEN_H // 2 + 32,
              COLOR_HINT, anchor="center")
    if record > 0:
        draw_text(surface, f"Recorde: {record} m",
                  16, SCREEN_W // 2, SCREEN_H // 2 + 58,
                  COLOR_RECORD, anchor="center")


def draw_dead_screen(surface: pygame.Surface, distance: int, record: int) -> None:
    overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 155))
    surface.blit(overlay, (0, 0))

    draw_text(surface, "VOCÊ MORREU",
              50, SCREEN_W // 2, SCREEN_H // 2 - 80,
              COLOR_DEAD_TITLE, anchor="center", shadow=True)
    draw_text(surface, f"Morreu em  {distance} m",
              26, SCREEN_W // 2, SCREEN_H // 2 - 16,
              COLOR_UI, anchor="center", shadow=True)

    if distance >= record:
        draw_text(surface, "★  NOVO RECORDE  ★",
                  20, SCREEN_W // 2, SCREEN_H // 2 + 22,
                  COLOR_RECORD, anchor="center", shadow=True)
    else:
        draw_text(surface, f"Recorde: {record} m",
                  18, SCREEN_W // 2, SCREEN_H // 2 + 22,
                  COLOR_RECORD, anchor="center")

    draw_text(surface, "Aperte ESPAÇO para recomeçar",
              20, SCREEN_W // 2, SCREEN_H // 2 + 58,
              COLOR_HINT, anchor="center", shadow=True)
    draw_text(surface, f"REC {record:05d} m",
              22, SCREEN_W - 20, 14, COLOR_RECORD, anchor="topright", shadow=True)
