from util import Answer, ReadPuzzle, ReadExamplePuzzle


def part1(data):
    return None


def part2(data):
    return None


def preprocess_data(data):
    """Do any additional parsing to the data to prep for answers"""
    return data


if __name__ == "__main__":
    # test answer on example data
    test_data, test_answer1 = ReadExamplePuzzle()
    data = preprocess_data(ReadPuzzle())
    test_data = preprocess_data(test_data)

    assert part1(test_data) == test_answer1
    # assert part2(test_data) == None

    # my answer
    for v in data:
        print(v)

    Answer(1, part1(data))
    Answer(2, part2(data))
