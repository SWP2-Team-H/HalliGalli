import sys
import time
import pygame as pg
import ctypes   # 해상도 구하는 모듈
from pygame.locals import *
from setting import *
from game import *

# 기능 시작
class Display() :
    def __init__(self) :
        pg.init()
        super().__init__()

        # 게임 창 설정
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) 
        width = user32.GetSystemMetrics(0)
        height = user32.GetSystemMetrics(1) 
        Display = pg.display.set_mode(screensize, FULLSCREEN)
        Display.fill(WHITE) 

        # 글자 설정
        font = pg.font.Font("src/font/EF_hyunygothic.ttf", 45)

        gamemode = font.render("게임 모드 : ", True, BLACK)
        Display.blit(gamemode, (100, 100))

        player1 = font.render("플레이어1 : ", True, BLACK)
        Display.blit(player1, (100, 200))

        p1_score = font.render("점수 : ", True, BLACK)
        Display.blit(p1_score, (100, 300))

        player2 = font.render("플레이어2 : ", True, BLACK)
        Display.blit(player2, (width - 700, 200))

        p2_score = font.render("점수 : ", True, BLACK)
        Display.blit(p2_score, (width - 700, 300))

        mc = font.render("사회자 : ", True, BLACK)
        Display.blit(mc, (100, height - 150))

        time_ = font.render("남은 시간 : ", True, BLACK)
        Display.blit(time_, (width - 500, height - 150))

        # 종
        bell = pg.image.load('src/img/bell.png')
        bell = pg.transform.scale(bell, (200, 200))
        Display.blit(bell, [(width/2)-100, 520])

        # 좌측 카드더미 위치
        deck_l = pg.image.load('src/img/back_s.png')
        deck_l = pg.transform.rotate(deck_l, 270)
        Display.blit(deck_l, [0, 500])

        # 우측 카드더미 위치
        deck_r = pg.image.load('src/img/back_s.png')
        deck_r = pg.transform.rotate(deck_r, 90)
        Display.blit(deck_r, [width - 190, 500])

        while True:
            for event in pg.event.get():
                if (event.type == KEYUP) :  # ESC 누르면 종료하도록 설정
                    if event.key == pg.K_ESCAPE :
                        pg.quit()
                        sys.exit()
                    elif event.key == pg.K_a :
                        deck1 = pg.draw.rect(Display, BLACK, (255, 505, 390, 230))
                        card1 = pg.image.load('src/img/'+fruit[0]+str(card_count[2])+'.png')
                        card1 = pg.transform.rotate(card1, 270)
                        Display.blit(card1, [250, 500])
                    elif event.key == pg.K_l :
                        deck2 = pg.draw.rect(Display, BLACK, (width - (265 + 380), 505, 390, 230))
                        card2 = pg.image.load('src/img/kiwi3.png')
                        card2 = pg.transform.rotate(card2, 90)
                        Display.blit(card2, [width - (250 + 380) , 500])

            pg.display.update()

