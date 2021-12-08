from util import Answer, ReadPuzzle, ReadExamplePuzzle


class Segment(object):
    def __init__(self, wire, digits):
        self.wire = wire
        self.digits = []
        for digit in digits:
            if self.wire in digit:
                self.digits.append(digit)
            self.digits = sorted(self.digits, key=len)

    def __eq__(self, other):
        """check the graph equality, we don't care about wire designation equality, just that the wires map to digits of the same segment count"""

        # must be connected to the same number of digits
        if len(self.digits) != len(other.digits):
            return False

        # check each digit is the same segment count, i.e. is the same digit
        for i, v in enumerate(self.digits):
            if len(v) != len(other.digits[i]):
                return False
        return True


class Display(object):
    standard_digits = {
        "abcefg": "0",
        "cf": "1",
        "acdeg": "2",
        "acdfg": "3",
        "bcdf": "4",
        "abdfg": "5",
        "abdefg": "6",
        "acf": "7",
        "abcdefg": "8",
        "abcdfg": "9",
    }
    standard_segments = (Segment("a", standard_digits.keys()), Segment("b", standard_digits.keys()),
                         Segment("c", standard_digits.keys()), Segment("d", standard_digits.keys()),
                         Segment("e", standard_digits.keys()), Segment("f", standard_digits.keys()),
                         Segment("g", standard_digits.keys()))

    def __init__(self, evidence):
        evidence = list(sorted(digit) for digit in evidence)
        segments = [Segment("a", evidence), Segment("b", evidence),
                    Segment("c", evidence), Segment("d", evidence),
                    Segment("e", evidence), Segment("f", evidence),
                    Segment("g", evidence)]

        # map segment wires by checking graph for each segment against the standard segment graph
        self.map = {}
        for segment in segments:
            for standard_segment in self.standard_segments:
                if segment == standard_segment:
                    self.map[segment.wire] = standard_segment.wire

    def display(self, digits):
        """use wire map to generate standard segment display and look up associated digit"""
        number = ""
        for digit in digits:
            segments = ""
            for segment in digit:
                segments += self.map[segment]
            number += self.standard_digits["".join(sorted(segments))]
        return int(number)


def part1(data):
    count = 0
    for _, output in data:
        for digit in output:
            # we can shortcut here and just use segment count for finding 1,4,7 and 8 in the output
            if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
                count += 1
    return count


def part2(data):
    total = 0
    for evidence, output in data:
        display = Display(evidence)
        total += display.display(output)
    return total


def preprocess_data(data):
    output_data = []
    for evidence, output in list(line.split(" | ") for line in data):
        output_data.append((evidence.split(), output.split()))
    return output_data


if __name__ == "__main__":
    # test answer on example data
    _, test_answer1 = ReadExamplePuzzle()
    test_data = preprocess_data([
        "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
        "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
        "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
        "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
        "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
        "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
        "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
        "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
        "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
        "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
    ])

    assert part1(test_data) == test_answer1
    assert part2(test_data) == 61229

    # my answer
    data = preprocess_data(ReadPuzzle())

    Answer(1, part1(data))
    Answer(2, part2(data))
