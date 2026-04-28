# game/assets.py — carregamento de todos os assets gráficos.

import os
import pygame

from constants import SCREEN_H

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load(name: str, scale_h: int | None = None) -> pygame.Surface:
    path = os.path.join(BASE, name)
    img  = pygame.image.load(path).convert()
    img.set_colorkey((0, 0, 0))
    if scale_h is not None:
        w, h  = img.get_size()
        new_w = int(w * scale_h / h)
        img   = pygame.transform.scale(img, (new_w, scale_h))
    return img


def load_assets() -> dict:
    assets: dict = {}

    assets["knight"] = [
        _load("run1.png", scale_h=80),
        _load("run2.png", scale_h=80),
    ]
    assets["crawlid"]  = _load("crawlid.png",  scale_h=45)
    assets["vengefly"] = _load("vengefly.png",  scale_h=55)

    bg_raw   = pygame.image.load(os.path.join(BASE, "background.png")).convert()
    bw, bh   = bg_raw.get_size()
    scaled_w = int(bw * SCREEN_H / bh)
    assets["bg"]   = pygame.transform.scale(bg_raw, (scaled_w, SCREEN_H))
    assets["bg_w"] = scaled_w

    return assets
