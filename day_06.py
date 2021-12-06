from copy import copy

import util


def pop(data, days):
    fish = copy(data)
    for d in range(days):
        count = len(fish)
        for i in range(count):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] -= 1
    return len(fish)


def part1(data):
    return pop(data, 80)


def part2(data):
    cycle = []
    prev = len(data)
    for i in range(7):
        cycle.append(pop(data, i) - prev)
        prev += cycle[-1]
    # print(cycle)

    pop_data = cycle * (256 // len(cycle) + 1)  # the base cycle is repeated
    for day in range(9, len(pop_data)):
        # it's a 9 day delay, and then 7 day delay
        for prev_day in range(day - 9, -1, -7):
            pop_data[day] += pop_data[prev_day]
    return sum(pop_data[:257]) + len(data)


if __name__ == "__main__":
    assert part1([3, 4, 3, 1, 2]) == 5934
    assert part2([3, 4, 3, 1, 2]) == 26984457539

    data = util.ReadPuzzle()[0]
    data = list(int(v) for v in data.split(","))

    util.Answer(1, part1(data))
    util.Answer(2, part2(data))
