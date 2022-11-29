import random
import keyboard
import time


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


def hg_check(p_list):
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


fruit = ['banana', 'strawberry', 'blueberry', 'goldkiwi']  # 과일 종류
card_count = [5, 3, 3, 2, 1]  # 카드 종류별 개수 (1, 2, 3, 4, 5)
card_deck = [t for i, t in enumerate(list((f, n) for f in fruit for n in range(
    1, 6))) for c in range(card_count[i % 5])]  # 56장
