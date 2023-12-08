#!/usr/bin/env python3

from pathlib import Path
from collections import Counter
from functools import cmp_to_key, lru_cache


currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip()

# 7 Five of a kind, where all five cards have the same label: AAAAA
# 6 Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# 5 Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# 4 Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# 3 Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# 2 One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# 1 High card, where all cards' labels are distinct: 23456


cards = "23456789TJQKA"


def rank(hand):
    c = Counter(hand)
    comm = c.most_common()
    if len(c) == 1:
        return 7
    elif len(c) == 2:
        if comm[0][1] == 4:
            return 6
        elif comm[0][1] == 3:
            return 5
        else:
            raise RuntimeError("unexpected len(c) == 2: ")
    elif len(c) == 3:
        if comm[0][1] == 3:
            return 4
        elif comm[0][1] == 2:
            return 3
        else:
            raise RuntimeError("unexpected len(c) == 3: ")
    elif len(c) == 4:
        return 2
    else:
        return 1


def cmp(bet1, bet2):
    hand1, hand2 = bet1[0], bet2[0]
    r1, r2 = rank(hand1), rank(hand2)
    if r1 < r2:
        return -1
    elif r1 > r2:
        return 1
    else:
        for k1, k2 in zip(hand1, hand2):
            if cards.index(k1[0]) < cards.index(k2[0]):
                return -1
            if cards.index(k1[0]) > cards.index(k2[0]):
                return 1
        else:
            raise RuntimeError("unexpected else")


# 1:11:07
def part1(p_input):
    hands = [l.split(" ") for l in p_input]
    hands.sort(key=cmp_to_key(cmp))

    solution = 0
    for i, hand in enumerate(hands):
        # print(f"{i+1:4d}", rank(hand[0]), hand[0], int(hand[1]))
        solution += (i + 1) * int(hand[1])

    return solution


cardsJ = "J23456789TQKA"


@lru_cache(maxsize=0)
def jokerize(hand):
    if "J" not in hand:
        return hand

    if hand == "JJJJJ":
        return "AAAAA"

    possibles = []
    for i, k in enumerate(hand):
        if k != "J":
            continue
        for newK in cardsJ[1:]:
            if newK not in hand:
                continue  # This line makes ALL the difference in speed!!!
            new_hand = jokerize(hand[:i] + newK + hand[i + 1 :])
            possibles.append((new_hand, 1))

    possibles = list(set([c for c in possibles if "J" not in c]))
    possibles.sort(key=lambda h: rank(h[0]))
    return possibles[-1][0]


def cmp2(bet1, bet2):
    hand1, hand2 = bet1[0], bet2[0]
    joker1, joker2 = bet1[2], bet2[2]
    r1, r2 = rank(joker1), rank(joker2)
    if r1 < r2:
        return -1
    elif r1 > r2:
        return 1
    else:
        for k1, k2 in zip(hand1, hand2):
            if cardsJ.index(k1[0]) < cardsJ.index(k2[0]):
                return -1
            if cardsJ.index(k1[0]) > cardsJ.index(k2[0]):
                return 1
        else:
            raise RuntimeError("unexpected else")


# 1:42:56
def part2(p_input):
    jokerize("JJJJJ")
    hands = [l.split(" ") for l in p_input]
    for i, hand in enumerate(hands):
        new_hand = jokerize(hand[0])
        hands[i].append(new_hand)

    hands.sort(key=cmp_to_key(cmp2))

    solution = 0
    for i, hand in enumerate(hands):
        # print(f"{i+1:4d}", rank(hand[0]), hand[0], int(hand[1]))
        solution += (i + 1) * int(hand[1])

    return solution


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input

    # simple treat input
    p_input = [line for line in raw_input.splitlines()]
    # p_input = [int(line) for line in raw_input.splitlines()]

    print("Solution to Part 1:")
    print(part1(p_input))

    print("Solution to Part 2:")
    print(part2(p_input))


if __name__ == "__main__":
    main()
