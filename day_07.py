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
    return best[1]


def part2(data):
    guess = int(sum(data) / len(data))

    best = [None, None]
    for i in range(0, guess + 100):
        c = cost_binomial(data, i)
        if best[1] is None or c < best[1]:
            best = [i, c]
    return best[1]


def preprocess_data(data):
    """Do any additional parsing to the data to prep for answers"""
    return list(int(v) for v in data[0].split(","))


if __name__ == "__main__":
    test_data, test_answer1 = util.ReadExamplePuzzle()
    test_data = preprocess_data(test_data)

    assert part1(test_data) == test_answer1
    assert part2(test_data) == 168

    data = util.ReadPuzzle()
    data = preprocess_data(data)

    util.Answer(1, part1(data))
    util.Answer(1, part2(data))
