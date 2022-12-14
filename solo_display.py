import sys
import pygame as pg
from pygame.locals import *
from setting import *
from game import *
import time


class Display():
    def __init__(self):
        # 기능 시작
        pg.init()
        super().__init__()

        # 게임 창 설정
        Display = pg.display.set_mode(screensize, FULLSCREEN)
        Display.fill(WHITE)
        global p_list

        # 글자 설정
        font = pg.font.Font("src/font/EF_hyunygothic.ttf", 45)

        gamemode = font.render("게임 모드 : 솔로 플레이", True, BLACK)
        Display.blit(gamemode, (100, 100))

        player1 = font.render("플레이어1 : " + p_list[0].name, True, BLACK)
        Display.blit(player1, (100, 200))

        p1_score = font.render("점수 : 0", True, BLACK)
        Display.blit(p1_score, (100, 300))

        player2 = font.render("플레이어2 : " + p_list[1].name, True, BLACK)
        Display.blit(player2, (width - 700, 200))

        p2_score = font.render("점수 : 0", True, BLACK)
        Display.blit(p2_score, (width - 700, 300))

        mc = font.render("사회자 :   "+p_list[0].name+"   Turn!", True, BLACK)
        Display.blit(mc, (100, height - 150))

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
        p_num = len(p_list)

        draw_key = [pg.K_a]  # draw key
        bell_key = [pg.K_s]  # bell key

        card_stack = 0  # 쌓인 카드 - > 점수
        bell_on = False  # 벨 활성화
        bell_wait = 0
        t = 0

        pg.display.update()
        while len(card_deck) > 0:
            cur = t % p_num
            if cur == 0:
                for event in pg.event.get():
                    if (event.type == KEYUP):  # ESC 누르면 종료하도록 설정
                        if event.key == pg.K_ESCAPE:
                            pg.quit()
                            sys.exit()
                        if event.key in draw_key:  # 카드 뽑기
                            card_stack += 1
                            p_list[cur].draw(card_deck)
                            deck1 = pg.draw.rect(
                                Display, BLACK, P1_DECK)
                            card1 = pg.image.load(
                                'src/img/' + p_list[cur].suit + str(p_list[cur].num) + '.png')
                            card1 = pg.transform.rotate(card1, 270)
                            Display.blit(card1, P1_CARD)
                            mcbox = pg.draw.rect(
                                Display, WHITE, (100, height - 150, 700, 100))
                            mc = font.render(
                                "사회자 :   "+p_list[(cur + 1) % 2].name+"   Turn!", True, BLACK)
                            Display.blit(mc, (100, height - 150))
                            draw_wait = time.time()
                            pg.display.update()
                            t += 1
                            bell_on = True
                            if hg_check(p_list):
                                bell_wait = time.time()
                        elif event.key in bell_key and bell_on:  # 플레이어 종
                            bell_p = bell_key.index(event.key)
                            if hg_check(p_list):
                                if hg_check(p_list) == 2:
                                    mcbox = pg.draw.rect(
                                        Display, WHITE, (100, height - 150, 700, 100))
                                    mc = font.render(
                                        "사회자 :   "+p_list[bell_p].name+"   2배!", True, BLACK)
                                    Display.blit(mc, (100, height - 150))
                                else:
                                    mcbox = pg.draw.rect(
                                        Display, WHITE, (100, height - 150, 700, 100))
                                    mc = font.render(
                                        "사회자 :   "+p_list[bell_p].name+"   Yummy!", True, BLACK)
                                    Display.blit(mc, (100, height - 150))
                                p_list[bell_p].score += card_stack * \
                                    hg_check(p_list)
                                card_stack = 0
                                for p in p_list:
                                    p.clear()
                                deck1_clear = pg.draw.rect(
                                    Display, WHITE, P1_DECK_CLEAR)
                                deck2_clear = pg.draw.rect(
                                    Display, WHITE, P2_DECK_CLEAR)
                            else:
                                mcbox = pg.draw.rect(
                                    Display, WHITE, (100, height - 150, 700, 100))
                                mc = font.render(
                                    "사회자 :   "+p_list[bell_p].name+"   Oops!", True, BLACK)
                                Display.blit(mc, (100, height - 150))
                                p_list[bell_p].score -= 3
                            bell_on = False
                            score1 = pg.draw.rect(
                                Display, WHITE, (100, 300, 400, 100))
                            player1 = font.render(
                                "점수 : " + str(p_list[0].score), True, BLACK)
                            Display.blit(player1, (100, 300))
                            score2 = pg.draw.rect(
                                Display, WHITE, (width - 700, 300, 400, 100))
                            player2 = font.render(
                                "점수 : " + str(p_list[1].score), True, BLACK)
                            Display.blit(player2, (width - 700, 300))
                            pg.display.update()
            else:
                if time.time() - draw_wait >= 1:
                    card_stack += 1
                    p_list[cur].draw(card_deck)
                    deck2 = pg.draw.rect(
                        Display, BLACK, P2_DECK)
                    card2 = pg.image.load(
                        'src/img/' + p_list[cur].suit + str(p_list[cur].num) + '.png')
                    card2 = pg.transform.rotate(card2, 90)
                    Display.blit(card2, P2_CARD)
                    mcbox = pg.draw.rect(
                        Display, WHITE, (100, height - 150, 700, 100))
                    mc = font.render(
                        "사회자 :   "+p_list[(cur + 1) % 2].name+"   Turn!", True, BLACK)
                    Display.blit(mc, (100, height - 150))
                    pg.display.update()
                    t += 1
                    bell_on = True
                    if hg_check(p_list):
                        bell_wait = time.time()
                for event in pg.event.get():
                    if (event.type == KEYUP):
                        if event.key in bell_key and bell_on:  # 플레이어 종
                            bell_p = bell_key.index(event.key)
                            if hg_check(p_list):
                                if hg_check(p_list) == 2:
                                    mcbox = pg.draw.rect(
                                        Display, WHITE, (100, height - 150, 700, 100))
                                    mc = font.render(
                                        "사회자 :   "+p_list[bell_p].name+"   2배!", True, BLACK)
                                    Display.blit(mc, (100, height - 150))
                                else:
                                    mcbox = pg.draw.rect(
                                        Display, WHITE, (100, height - 150, 700, 100))
                                    mc = font.render(
                                        "사회자 :   "+p_list[bell_p].name+"   Yummy!", True, BLACK)
                                    Display.blit(mc, (100, height - 150))
                                p_list[bell_p].score += card_stack * \
                                    hg_check(p_list)
                                card_stack = 0
                                for p in p_list:
                                    p.clear()
                                deck1_clear = pg.draw.rect(
                                    Display, WHITE, P1_DECK_CLEAR)
                                deck2_clear = pg.draw.rect(
                                    Display, WHITE, P2_DECK_CLEAR)
                            else:
                                mcbox = pg.draw.rect(
                                    Display, WHITE, (100, height - 150, 700, 100))
                                mc = font.render(
                                    "사회자 :   "+p_list[bell_p].name+"   Oops!", True, BLACK)
                                Display.blit(mc, (100, height - 150))
                                p_list[bell_p].score -= 3
                            bell_on = False
                            score1 = pg.draw.rect(
                                Display, WHITE, (100, 300, 400, 100))
                            player1 = font.render(
                                "점수 : " + str(p_list[0].score), True, BLACK)
                            Display.blit(player1, (100, 300))
                            score2 = pg.draw.rect(
                                Display, WHITE, (width - 700, 300, 400, 100))
                            player2 = font.render(
                                "점수 : " + str(p_list[1].score), True, BLACK)
                            Display.blit(player2, (width - 700, 300))
                            pg.display.update()
            if time.time() - bell_wait >= p_list[1].diff and hg_check(p_list):
                if hg_check(p_list) == 2:
                    mcbox = pg.draw.rect(
                        Display, WHITE, (100, height - 150, 700, 100))
                    mc = font.render(
                        "사회자 :   "+p_list[1].name+"   2배!", True, BLACK)
                    Display.blit(mc, (100, height - 150))
                else:
                    mcbox = pg.draw.rect(
                        Display, WHITE, (100, height - 150, 700, 100))
                    mc = font.render(
                        "사회자 :   "+p_list[1].name+"   Yummy!", True, BLACK)
                    Display.blit(mc, (100, height - 150))
                p_list[1].score += card_stack * \
                    hg_check(p_list)
                card_stack = 0
                for p in p_list:
                    p.clear()
                deck1_clear = pg.draw.rect(
                    Display, WHITE, P1_DECK_CLEAR)
                deck2_clear = pg.draw.rect(
                    Display, WHITE, P2_DECK_CLEAR)
                bell_on = False
                score1 = pg.draw.rect(
                    Display, WHITE, (100, 300, 400, 100))
                player1 = font.render(
                    "점수 : " + str(p_list[0].score), True, BLACK)
                Display.blit(player1, (100, 300))
                score2 = pg.draw.rect(
                    Display, WHITE, (width - 700, 300, 400, 100))
                player2 = font.render(
                    "점수 : " + str(p_list[1].score), True, BLACK)
                Display.blit(player2, (width - 700, 300))
                pg.display.update()

        mcbox = pg.draw.rect(
            Display, WHITE, (100, height - 150, 700, 100))
        mc = font.render("사회자 :   " + win_player(p_list), True, BLACK)
        Display.blit(mc, (100, height - 150))
        pg.display.update()
        while True:
            for event in pg.event.get():
                if (event.type == KEYUP):  # ESC 누르면 종료하도록 설정
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()


if __name__ == '__main__':
    Display()
