# constants.py — todas as constantes do jogo em um único lugar.

# --- janela ---
SCREEN_W = 900
SCREEN_H = 400
FPS      = 60

# --- mundo ---
GROUND_Y = 330

# --- física ---
GRAVITY         = 0.65
JUMP_FORCE      = -15.5
MAX_FALL_MULTI  = 2.0
FALL_ACCEL_RATE = 0.04

# --- velocidade ---
INITIAL_SPEED = 230.0
SPEED_CAP     = 520.0
SPEED_INC     = 9.0

# --- spawn ---
SPAWN_INTERVAL_MAX = 1.8
SPAWN_INTERVAL_MIN = 0.8

# --- cores HUD (RGB) ---
COLOR_UI         = (200, 185, 255)
COLOR_RECORD     = (255, 220,  80)
COLOR_DEAD_TITLE = (220,  70,  70)
COLOR_HINT       = (160, 145, 200)
COLOR_SCORE      = (220, 210, 255)

# --- chão ---
COLOR_GROUND      = (20,  15,  35)
COLOR_GROUND_LINE = (60,  50,  90)
