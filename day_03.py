from copy import copy

import util


def get_bits(data):
    bits = len(data[0]) * [0, ]

    for line in data:
        for i, char in enumerate(line):
            if char == "1":
                bits[i] += 1
    return bits


def part1(data):
    bits = get_bits(data)

    gamma = ""
    epsilon = ""
    for bit in bits:
        if bit > len(data) / 2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    util.Answer(1, int(gamma, 2) * int(epsilon, 2))


def part2(data):
    oxygen_list = copy(data)
    oxygen_bits = get_bits(data)
    CO2_list = copy(data)
    CO2_bits = get_bits(data)

    for i in range(len(data[0])):
        if len(oxygen_list) > 1:
            oxygen_list = list(v for v in oxygen_list if v[i] == str(int(oxygen_bits[i] >= len(oxygen_list) / 2)))
            oxygen_bits = get_bits(oxygen_list)
        if len(CO2_list) > 1:
            CO2_list = list(v for v in CO2_list if v[i] == str(int(CO2_bits[i] < len(CO2_list) / 2)))
            CO2_bits = get_bits(CO2_list)

    util.Answer(2, int(oxygen_list[0], 2) * int(CO2_list[0], 2))


if __name__ == "__main__":
    data = util.ReadPuzzle()
    if False:
        data = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]

    part1(data)
    part2(data)
