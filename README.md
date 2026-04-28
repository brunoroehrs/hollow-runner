# Hollow Runner

Runner 2D feito com Pygame, inspirado em Hollow Knight.

## Como rodar

```bash
pip install pygame
python main.py
```

## Controles

| Tecla | Ação |
|-------|------|
| Espaço / W / ↑ | Pular |
| S | Cair mais rápido |

## Estrutura

```
hollow_runner/
├── main.py           # Ponto de entrada
├── constants.py      # Todas as constantes
├── entities/
│   ├── base.py       # GameObject (ABC)
│   ├── player.py     # Player
│   ├── enemies.py    # Enemy, Crawlid, Vengefly
│   └── factory.py    # EntityFactory
└── game/
    ├── assets.py     # Carregamento de imagens
    ├── background.py # Scroll infinito
    ├── hud.py        # Interface do jogador
    └── game.py       # Loop principal
```
