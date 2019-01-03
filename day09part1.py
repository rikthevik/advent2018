#!/usr/bin/env python3

""" https://adventofcode.com/2018/day/2 """


inputstr = """
9 players; last marble is worth 23 points: high score is 32
10 players; last marble is worth 1618 points: high score is 8317
10 players; last marble is worth 1618 points: high score is 8317
13 players; last marble is worth 7999 points: high score is 146373
17 players; last marble is worth 1104 points: high score is 2764
21 players; last marble is worth 6111 points: high score is 54718
30 players; last marble is worth 5807 points: high score is 37305
476 players; last marble is worth 71657 points
"""

import re, collections, itertools
Node = collections.namedtuple('Node', 'a children metadata')

regex = re.compile('^(\d+) players; last marble is worth (\d+) points:')

def go(num_players, last_marble):
    marble_gen = itertools.count(0)
    player_gen = itertools.cycle(range(num_players))
    scores = [ 0 for i in range(num_players) ]
    print(num_players, last_marble)
    marble_idx = 0
    marbles = [ next(marble_gen) ] 
    for turn in range(26):
        player_idx = next(player_gen)

        if turn == 0:
            marbles.append(next(marble_gen))
            marble_idx = 1
        else:
            next_marble_idx = (marble_idx + 2) % len(marbles)
            print("insert at", next_marble_idx)
            marbles.insert(next_marble_idx, next(marble_gen)) 
            marble_idx = (next_marble_idx + 0) % len(marbles)

        print("[%d]" % (player_idx+1), end="")
        for i, m in enumerate(marbles):
            if i == marble_idx:
                print(" *%02d" % m, end="")
            else:
                print("  %02d" % m, end="")
        print("  marble_idx=", marble_idx)

def main():
    for l in inputstr.strip().splitlines():
        num_players, last_marble = map(int, regex.match(l).groups())
        go(num_players, last_marble)
        break

if __name__ == '__main__':
    main()
