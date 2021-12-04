from typing import List

import util


class BingoBoard(object):
    winning_masks = (0b1111100000000000000000000,
                  0b0000011111000000000000000,
                  0b0000000000111110000000000,
                  0b0000000000000001111100000,
                  0b0000000000000000000011111,
                  0b1000010000100001000010000,
                  0b0100001000010000100001000,
                  0b0010000100001000010000100,
                  0b0001000010000100001000010,
                  0b0000100001000010000100001)

    def __init__(self, lines):
        self.board = list(int(number) for line in lines for number in line.split())
        self.board_state = 0

    def check_number(self, number):
        try:
            index = self.board.index(number)
        except ValueError:
            return False
        self.board_state |= 0b1 << index
        return True

    def bingo(self):
        for win_state in self.winning_masks:
            if self.board_state & win_state == win_state:
                return True
        return False

    def stamped(self, index):
        return self.board_state & 0b1 << index == 0b1 << index

    def unstamped(self):
        return (v for i, v in enumerate(self.board) if not self.stamped(i))

    def __repr__(self):
        lines = []
        for i, v in enumerate(self.board):
            if i % 5 == 0:
                lines.append("")
            if self.stamped(i):
                lines[-1] += f"*{v}* "
            else:
                lines[-1] += f" {v}  "

        return "\n".join(lines)


def part1(numbers: List[int], boards: List[BingoBoard]):
    number = None
    winning_board = None
    for number in numbers:
        for board in boards:
            if board.check_number(number) and board.bingo():
                winning_board = board
                break
        if winning_board is not None: break

    util.Answer(1, number * sum(winning_board.unstamped()))


def part2(numbers: List[int], boards: List[BingoBoard]):
    number = None
    losing_board = None
    for number in numbers:
        for board in boards:
            board.check_number(number)
        if len(boards) == 1 and boards[0].bingo():
            losing_board = boards[0]
            break
        boards = list(board for board in boards if not board.bingo())

    util.Answer(2, number * sum(losing_board.unstamped()))


if __name__ == "__main__":
    data = util.ReadPuzzle()

    if False:
        data = ["7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
                "",
                "22 13 17 11  0",
                "8  2 23  4 24",
                "21  9 14 16  7",
                "6 10  3 18  5",
                "1 12 20 15 19",
                "",
                "3 15  0  2 22",
                "9 18 13 17  5",
                "19  8  7 25 23",
                "20 11 10 24  4",
                "14 21 16 12  6",
                "",
                "14 21 17 24  4",
                "10 16 15  9 19",
                "18  8 23 26 20",
                "22 11 13  6  5",
                "2  0 12  3  7", ]

    numbers = list(int(v) for v in data[0].split(","))

    lines = []
    boards = []
    for line in data[2:]:
        if line == "":
            boards.append(BingoBoard(lines))
            lines = []
        else:
            lines.append(line)
    boards.append(BingoBoard(lines))

    part1(numbers, boards)
    part2(numbers, boards)
