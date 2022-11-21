import random
import keyboard
import time


class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.suit = 'banana'
        self.num = 0
        self.score = 0

    def __str__(self):
        return self.player_name + ': ' + '(' + self.suit + ',' + str(self.num) + ')'

    def draw(self, deck):
        self.suit, self.num = deck.pop(random.randint(0, len(card_deck) - 1))

    def clear(self):
        self.suit = 'banana'
        self.num = 0


def hg_check():
    # global p_list
    check = {key: 0 for key in fruit}
    for p in p_list:
        check[p.suit] += p.num
    if 5 in check.values():
        if check['goldkiwi'] == 5:
            return 2  # Double
        return 1  # True
    return 0  # False


fruit = ['banana', 'strawberry', 'blueberry', 'goldkiwi']  # 과일 종류
card_count = [5, 3, 3, 2, 1]  # 카드 종류별 개수 (1, 2, 3, 4, 5)
card_deck = [t for i, t in enumerate(list((f, n) for f in fruit for n in range(
    1, 6))) for c in range(card_count[i % 5])]  # 56장


print(card_deck)
print(len(card_deck))

p_num = int(input('플레이어 수를 입력하세요: '))

p_list = []
# p1 : draw - a, bell - s
# p2 : draw - l, bell - k
draw_key = ['a', 'l']
bell_key = ['s', 'k']

for i in range(p_num):
    p_name = input('플레이어' + str(i + 1) + ' 이름: ')
    p_list.append(Player(p_name))

card_stack = 0  # 쌓인 카드 - > 점수
hg = False  # 현재 상태가 할리갈리 상태인지 아닌지
t = 0
while len(card_deck) > 0:
    print("Turn", t, end="   ")
    ##################################
    # 키보드 입력 부분 -> pygame 연계하면 바뀔 듯
    while True:
        key = keyboard.read_key()
        time.sleep(0.2)
        if key in draw_key[t % p_num] or key in bell_key:
            break
    ##################################
    if key == draw_key[t % p_num]:  # 카드 뽑기
        card_stack += 1
        p_list[t % p_num].draw(card_deck)
        print(p_list[t % p_num], card_stack)
        t += 1
    elif key in bell_key:  # 플레이어 1번 종
        bell_p = bell_key.index(key)
        if hg_check() == 2:
            card_stack *= 2
            print("2배! ", end="")
        if hg_check():
            p_list[bell_p].score += card_stack
            card_stack = 0
            for p in p_list:
                p.clear()
        else:
            p_list[bell_p].score -= 3
        print(f"p1: {p_list[0].score}, p2: {p_list[1].score}")

score_check = {p.player_name: p.score for p in p_list}
player_list = [p for p in score_check.keys() if score_check[p] ==
               max(score_check.values())]
print(", ".join(player_list) + " win!")
