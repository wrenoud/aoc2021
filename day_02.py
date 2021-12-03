from typing import List

import util


class Action(object):
    def __init__(self, action: str):
        self.dir, self.step = action.split(" ")
        self.step = int(self.step)
        if self.dir == "up":
            self.step = -self.step


def part1(data: List[Action]):
    pos = 0
    depth = 0
    for action in data:
        if action.dir == "forward":
            pos += action.step
        else:
            depth += action.step
    util.Answer(1, pos * depth)


def part2(data):
    aim = 0
    pos = 0
    depth = 0
    for action in data:
        if action.dir == "forward":
            pos += action.step
            depth += action.step * aim
        else:
            aim += action.step
    util.Answer(2, pos * depth)


if __name__ == "__main__":
    data = util.ReadPuzzle()
    if False:
        data = ["forward 5",
                "down 5",
                "forward 8",
                "up 3",
                "down 8",
                "forward 2", ]

    data = list(Action(v) for v in data)
    part1(data)
    part2(data)
