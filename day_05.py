import util
from util import Point


class Line(object):
    def __init__(self, str_repl):
        start, end = str_repl.split(" -> ")
        self.start = Point(*(int(v) for v in start.split(",")))
        self.end = Point(*(int(v) for v in end.split(",")))

        self._step = self.end - self.start
        self._step /= max(abs(self._step.x), abs(self._step.y))

    def is_perpendicular(self):
        return self.start.x == self.end.x or self.start.y == self.end.y

    def __iter__(self):
        self._current = self.start
        return self

    def __next__(self):
        ret = self._current
        if self._current - self._step == self.end:
            raise StopIteration()
        self._current += self._step
        return ret

    def __repl__(self):
        return f"Line({self.start},{self.end})"

    def __str__(self):
        return self.__repl__()


def map_map(rows, cols):
    map = []
    for r in range(rows):
        map.append([])
        for c in range(cols):
            map[-1].append(0)
    return map


def part1(data):
    map = map_map(1000, 1000)

    lines = list(line for line in data if line.is_perpendicular())

    for i, line in enumerate(lines):
        for v in line:
            map[v.y][v.x] += 1

    util.Answer(1, sum(c > 1 for r in map for c in r))


def part2(data):
    map = map_map(1000, 1000)

    for i, line in enumerate(data):
        for v in line:
            map[v.y][v.x] += 1

    for r in map:
        pass  # print("".join(str(v) if v > 0 else "." for v in r))

    util.Answer(2, sum(c > 1 for r in map for c in r))


if __name__ == "__main__":
    data = util.ReadPuzzle()
    if False:
        data = [
            "0,9 -> 5,9",
            "8,0 -> 0,8",
            "9,4 -> 3,4",
            "2,2 -> 2,1",
            "7,0 -> 7,4",
            "6,4 -> 2,0",
            "0,9 -> 2,9",
            "3,4 -> 1,4",
            "0,0 -> 8,8",
            "5,5 -> 8,2",
        ]

    data = list(Line(v) for v in data)
    part1(data)
    part2(data)
