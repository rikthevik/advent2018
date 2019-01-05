#!/usr/bin/env python3

""" https://adventofcode.com/2018/day/2 """


inputstr = """
initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
"""

inputstr = """
initial state: ##.###.......#..#.##..#####...#...#######....##.##.##.##..#.#.##########...##.##..##.##...####..####

#.#.# => #
.##.. => .
#.#.. => .
..### => #
.#..# => #
..#.. => .
####. => #
###.. => #
#.... => .
.#.#. => #
....# => .
#...# => #
..#.# => #
#..#. => #
.#... => #
##..# => .
##... => .
#..## => .
.#.## => #
.##.# => .
#.##. => #
.#### => .
.###. => .
..##. => .
##.#. => .
...## => #
...#. => .
..... => .
##.## => .
###.# => #
##### => #
#.### => .
"""


import re, collections, itertools
Node = collections.namedtuple('Node', 'a children metadata')

regex = re.compile('^(\d+) players; last marble is worth (\d+) points')
    
    
def display_state(r, state):
    print("%02d: " % r, end='')
    for i in range(-40, 140):
        print(state.get(i, "-"), end='')
    print()

def main():
    lines = inputstr.strip().splitlines()
    initial_state = lines[0][15:]
    rules = [ s.split(" => ") for s in lines[2:] ]

    print("INITIAL", initial_state)
    state = dict(enumerate(initial_state)) 
    display_state(0, state)


    for r in range(1, 21):
        newstate = {}
        # print("!!", min(state.keys()), max(state.keys()))
        for i in range(min(state.keys())-4, max(state.keys())+4):
            s = "".join(state.get(i+j, '.') for j in range(-2, 3))
            # print("s=", s)
            found = None
            for match, result in rules:
                # print("match=", match, "s=", s)
                if match == s:
                    assert not found
                    found = result
                    # print("MATCH AT ", i)
                    break
            newstate[i] = found or '.'
        state = newstate
        display_state(r, state)
        
    print(sum( k for k, v in state.items() if v == '#' ))



if __name__ == '__main__':
    main()
