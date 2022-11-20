import sys
import pygame as pg
import ctypes   # 해상도 구하는 모듈
from pygame.locals import *
from setting import *

# 기능 시작
pg.init()

# 초당 프레임 단위 설정
FPS = 30
FramePerSec = pg.time.Clock()

# 게임 창 설정
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) 
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1) 
Display = pg.display.set_mode(screensize, FULLSCREEN)
Display.fill(WHITE) 

# 글자 설정
font = pg.font.SysFont("arial", 45, False, False)
gamemode = font.render("게임 모드 : ", True, BLACK)

Display.blit(gamemode, (100, 100))

# 덱 위치에 그림자 지게 하기
deck1 = pg.draw.rect(Display, BLACK, (305, 505, 390, 230), 25)
deck2 = pg.draw.rect(Display, BLACK, (width - (315 + 380), 505, 390, 230), 25)

# 종
bell = pg.image.load('src/bell.png')
bell = pg.transform.scale(bell, (200, 200))
Display.blit(bell, [(width/2)-100, 520])

# 좌측 카드 위치 - 이 위치에 카드 튜플이나 리스트로 만들어서 받을 수 있게 해야 할 것 같아요
banana1 = pg.image.load('src/banana1.png')
banana1 = pg.transform.rotate(banana1, 270)
Display.blit(banana1, [300, 500])

# 좌측 카드더미 위치
deck_l = pg.image.load('src/back_s.png')
deck_l = pg.transform.rotate(deck_l, 270)
Display.blit(deck_l, [0, 500])

# 우측 카드 위치 - 이 위치에 카드 튜플이나 리스트로 만들어서 받을 수 있게 해야 할 것 같아요
kiwi3 = pg.image.load('src/kiwi3.png')
kiwi3 = pg.transform.rotate(kiwi3, 90)
Display.blit(kiwi3, [width - (300 + 380) , 500])

# 좌측 카드더미 위치
deck_r = pg.image.load('src/back_s.png')
deck_r = pg.transform.rotate(deck_r, 90)
Display.blit(deck_r, [width - 190, 500])

while True:
    pg.display.update()
    for event in pg.event.get():
        if (event.type == KEYUP) :  # ESC 누르면 종료하도록 설정
            if event.key == pg.K_ESCAPE :
                pg.quit()
                sys.exit()
    FramePerSec.tick(FPS)