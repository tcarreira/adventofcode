#!/usr/bin/env python3

from collections import deque
from pathlib import Path

from solver_1 import get_winner_score, parse_input

curdir = Path(__file__).parent.absolute()


def play_recursive(deck1, deck2):
    decks_history = set()
    while len(deck1) > 0 and len(deck2) > 0:
        history1 = "deck1," + ",".join([str(x) for x in deck1])
        history2 = "deck2," + ",".join([str(x) for x in deck2])
        if history1 in decks_history or history2 in decks_history:
            return get_winner_score(deck1, [])
        else:
            decks_history.add(history1)
            decks_history.add(history2)

        card1, card2 = deck1.popleft(), deck2.popleft()

        if len(deck1) >= card1 and len(deck2) >= card2:
            # recursive game
            subdeck1 = deque([x for i, x in enumerate(deck1) if i < card1])
            subdeck2 = deque([x for i, x in enumerate(deck2) if i < card2])

            play_recursive(subdeck1, subdeck2)
            if len(subdeck1) == 0:
                deck2.append(card2)
                deck2.append(card1)
            else:
                deck1.append(card1)
                deck1.append(card2)
        else:
            if card1 > card2:
                deck1.append(card1)
                deck1.append(card2)
            else:
                deck2.append(card2)
                deck2.append(card1)

    return get_winner_score(deck1, deck2)


def main():
    with open(curdir.joinpath("input.txt")) as f:
        raw_input = f.read().strip()

    player1, player2 = parse_input(raw_input)
    score = play_recursive(player1, player2)

    print(f"Solution: {score}")


if __name__ == "__main__":
    main()
