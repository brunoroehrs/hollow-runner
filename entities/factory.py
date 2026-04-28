# entities/factory.py — fábrica de inimigos.

import random

from .enemies import Enemy, Crawlid, Vengefly


class EntityFactory:
    """Cria inimigos aleatoriamente. 55% Crawlid, 45% Vengefly."""

    def __init__(self, assets: dict):
        self._assets = assets

    def create(self) -> Enemy:
        if random.random() < 0.55:
            return Crawlid(self._assets["crawlid"])
        return Vengefly(self._assets["vengefly"])
