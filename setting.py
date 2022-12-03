from game import *
import ctypes
# 게임 세팅을 위한 값을 모아놓기 위한 파일

# 게임 창 설정
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

# 플레이어 리스트
p_list = []

# 색 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 플레이어별 카드 위치
P1_DECK = (255, 505, 390, 230)
P1_DECK_CLEAR = (240, 475, 420, 300)
P1_CARD = [250, 500]
P2_DECK = (width - (265 + 380), 505, 390, 230)
P2_DECK_CLEAR = (width - (265 + 380), 475, 420, 300)
P2_CARD = [width - (250 + 380), 500]
