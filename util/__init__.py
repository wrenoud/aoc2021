from util.puzzle import ReadPuzzle, Answer


class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        else:
            return Point(self.x - other, self.y - other)

    def __truediv__(self, other):
        if isinstance(other, Point):
            return Point(self.x // other.x, self.y // other.y)
        else:
            return Point(self.x // other, self.y // other)

    def __hash__(self):
        return self.x << 16 & self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repl__(self):
        return f"Point({self.x},{self.y})"

    def __str__(self):
        return self.__repl__()
