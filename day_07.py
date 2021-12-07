import util
import math


def cost_linear(data, position):
    return sum(abs(v - position) for v in data)


def cost_binomial(data, position):
    return sum(abs(v - position) * (abs(v - position) + 1) / 2 for v in data)


def part1(data):
    guess = int(sum(data) / len(data))

    best = [None, None]
    for i in range(0, guess):
        c = cost_linear(data, i)
        if best[1] is None or c < best[1]:
            best = [i, c]

    util.Answer(1, best)


def part2(data):
    guess = int(sum(data) / len(data))

    best = [None, None]
    for i in range(0, guess + 100):
        c = cost_binomial(data, i)
        if best[1] is None or c < best[1]:
            best = [i, c]
    util.Answer(2, best)


if __name__ == "__main__":
    data = util.ReadPuzzle()
    data = list(int(v) for v in data[0].split(","))

    part1(data)
    part2(data)
