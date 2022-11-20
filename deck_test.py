import random


class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.suit = '바나나'
        self.num = 0

    def __str__(self):
        return self.player_name + ': ' + '(' + self.suit + ',' + str(self.num) + ')'

    def draw(self, deck):
        self.suit, self.num = deck.pop(random.randint(0, len(card_deck) - 1))

    def clear(self):
        self.suit = '바나나'
        self.num = 0


fruit = ['바나나', '딸기', '키위', '블루베리']  # 과일 종류
card_count = [5, 3, 3, 2, 1]  # 카드 종류별 개수 (1, 2, 3, 4, 5)
card_deck = [t for i, t in enumerate(list((f, n) for f in fruit for n in range(1, 6))) for c in range(card_count[i % 5])]

print(card_deck)
print(len(card_deck))

p_num = int(input('플레이어 수를 입력하세요: '))

p_list = []
for i in range(p_num):
    p_name = input('플레이어' + str(i + 1) + ' 이름: ')
    p_list.append(Player(p_name))


cnt = 0
for i in range((len(card_deck) - 1)):
    check = {key: 0 for key in fruit}
    p_list[i % p_num].draw(card_deck)
    print(p_list[i % p_num])

    for p in p_list:
        check[p.suit] += p.num
    if 5 in check.values():
        print('할리갈리')
        for p in p_list:
            p.clear()
        cnt += 1
print(cnt)
