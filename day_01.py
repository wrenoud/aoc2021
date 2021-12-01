import util


def part1(data):
    util.Answer(1, sum(data[i] < v for i,v in enumerate(data[1:])))


def part2(data):
    util.Answer(2, sum(data[i] < v for i,v in enumerate(data[3:])))


if __name__ == "__main__":
    data = util.ReadPuzzle()

    data = list(int(v) for v in data)

    # data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263,]

    part1(data)
    part2(data)
