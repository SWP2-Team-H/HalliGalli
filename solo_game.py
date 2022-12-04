import random
import keyboard
import time
import sys


class Player:
    def __init__(self, name):
        self.name = name
        self.suit = 'banana'
        self.num = 0
        self.score = 0

    def __str__(self):
        return self.name + ': ' + '(' + self.suit + ',' + str(self.num) + ')'

    def draw(self, deck):
        self.suit, self.num = deck.pop(random.randint(0, len(card_deck) - 1))

    def clear(self):
        self.suit = 'banana'
        self.num = 0


def hg_check():
    check = {key: 0 for key in fruit}
    for p in p_list:
        check[p.suit] += p.num
    if 5 in check.values():
        if check['goldkiwi'] == 5:
            return 2  # Double
        return 1  # True
    return 0  # False


def print_score(p_list):
    score_string = []
    for p in p_list:
        score_string.append(p.name + ": " + str(p.score))
    print(", ".join(score_string))

def readInput(timeout):

    start_time = time.time()
    input = ''
    while True:
        if keyboard.is_pressed("a"):
            input = "a"
            break
        elif keyboard.is_pressed("s"):
            input = "s"
            break
        if len(input) == 0 and (time.time() - start_time) > timeout:
            break

    if len(input) > 0:
        return input
    else:
        return "k"


fruit = ['banana', 'strawberry', 'blueberry', 'goldkiwi']  # 과일 종류
card_count = [5, 3, 3, 2, 1]  # 카드 종류별 개수 (1, 2, 3, 4, 5)
card_deck = [t for i, t in enumerate(list((f, n) for f in fruit for n in range(
    1, 6))) for c in range(card_count[i % 5])]  # 56장


print(card_deck)

print(len(card_deck))

d = int(input('난이도를 선택하세요(1 ~ 5): '))
difficulty = [5, 4, 3, 2, 1]
diff = difficulty[d - 1]
p_num = 2

p_list = []
# p1 : draw - a, bell - s
# p2 : draw - l, bell - k
draw_key = ['a', 'l']
bell_key = ['s', 'k']

p_name = input('플레이어 이름: ')
p_list.append(Player(p_name))
p_list.append(Player('Computer'))

card_stack = 0  # 쌓인 카드 - > 점수
hg = False  # 현재 상태가 할리갈리 상태인지 아닌지
bell_on = False  # 벨 활성화
t = 1
while len(card_deck) > 0:
    ##################################
    # 키보드 입력 부분 -> pygame 연계하면 바뀔 듯
    while True:
        if hg_check():
            key = readInput(diff)
            if key in draw_key or key in bell_key:
                time.sleep(0.2)
                break
        if t % p_num == 1:
            time.sleep(0.5)
            key = draw_key[1]
            time.sleep(0.2)
            break
        else:
            key = keyboard.read_key()
            time.sleep(0.2)
            break
        time.sleep(0.2)
    ##################################
    if key == draw_key[t % p_num]:  # 카드 뽑기
        print("Turn", t + 1, end="   ")
        card_stack += 1
        p_list[t % p_num].draw(card_deck)
        print(p_list[t % p_num], card_stack)
        t += 1
        bell_on = True
    elif key in bell_key and bell_on:  # 플레이어 1번 종
        bell_p = bell_key.index(key)
        if hg_check() == 2:
            card_stack *= 2
            print("2배! ", end="")
        if hg_check():
            print(f"{p_list[bell_p].name} Yummy!")
            p_list[bell_p].score += card_stack
            card_stack = 0
            for p in p_list:
                p.clear()
        else:
            print(f"{p_list[bell_p].name} Oops!")
            p_list[bell_p].score -= 3
        print_score(p_list)
        bell_on = False
    else:
        continue

score_check = {p.name: p.score for p in p_list}
player_list = [p for p in score_check.keys() if score_check[p] ==
               max(score_check.values())]
print_score(p_list)
print(", ".join(player_list) + " Win!")
