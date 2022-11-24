import sys
import time
import pygame as pg
import ctypes   # 해상도 구하는 모듈
from pygame.locals import *
from setting import *
from game import *

# 기능 시작


class Display():
    def __init__(self):
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

        # 게임 기본 설정
        p_list = [Player("a"), Player("b")]  # 나중에 PyQt 연계해서 정보 가져오기
        p_num = len(p_list)

        draw_key = [pg.K_a, pg.K_l]  # draw key
        bell_key = [pg.K_s, pg.K_k]  # bell key

        card_stack = 0  # 쌓인 카드 - > 점수
        hg = False  # 현재 상태가 할리갈리 상태인지 아닌지
        bell_on = False  # 벨 활성화
        t = 0

        while len(card_deck) > 0:
            for event in pg.event.get():
                if (event.type == KEYUP):  # ESC 누르면 종료하도록 설정
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
                    elif event.key == draw_key[t % p_num]:  # 카드 뽑기
                        card_stack += 1
                        p_list[t % p_num].draw(card_deck)
                        # print(p_list[t % p_num], card_stack)
                        if t % p_num == 0:
                            deck1 = pg.draw.rect(
                                Display, BLACK, (255, 505, 390, 230))
                            card1 = pg.image.load(
                                'src/img/' + p_list[t % p_num].suit + str(p_list[t % p_num].num) + '.png')
                            card1 = pg.transform.rotate(card1, 270)
                            Display.blit(card1, [250, 500])
                        else:
                            deck2 = pg.draw.rect(
                                Display, BLACK, (width - (265 + 380), 505, 390, 230))
                            card2 = pg.image.load(
                                'src/img/' + p_list[t % p_num].suit + str(p_list[t % p_num].num) + '.png')
                            card2 = pg.transform.rotate(card2, 90)
                            Display.blit(card2, [width - (250 + 380), 500])
                        t += 1
                        bell_on = True
                    elif event.key in bell_key and bell_on:  # 플레이어 1번 종
                        bell_p = bell_key.index(event.key)
                        if hg_check(p_list) == 2:
                            card_stack *= 2
                            # print("2배! ", end="")
                        if hg_check(p_list):
                            # print(f"{p_list[bell_p].name} Yummy!")
                            p_list[bell_p].score += card_stack
                            card_stack = 0
                            for p in p_list:
                                p.clear()
                        else:
                            # print(f"{p_list[bell_p].name} Oops!")
                            p_list[bell_p].score -= 3
                        # print_score(p_list)
                        bell_on = False
                    else:
                        continue
                    pg.display.update()
        while True:
            for event in pg.event.get():
                if (event.type == KEYUP):  # ESC 누르면 종료하도록 설정
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
