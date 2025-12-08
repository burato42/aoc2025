import operator
from functools import reduce
from pprint import pprint


def read_file_part1(file_path: str) -> list[list[str]]:
    lines = []
    with open(file_path) as file:
        for line in file.readlines():
            lines.append(line.split())
    return lines


def calculate_part1(lines: list[list[str]]) -> int:
    statements = list(zip(*lines))
    res = 0
    for stmt in statements:
        numbers = map(int, stmt[:-1])
        if stmt[-1] == "+":
            res += reduce(operator.add, numbers, 0)
        elif stmt[-1] == "*":
            res += reduce(operator.mul, numbers, 1)
        else:
            raise Exception("Unknown operator")
    return res


def read_file_part2(file_path: str) -> list[list[str]]:
    field_sizes = []
    res = []
    with open(file_path) as file:
        raw_lines = file.readlines()
    last_line = raw_lines[-1]

    cur = last_line[0]
    for idx in range(1, len(last_line)):
        if last_line[idx] != " ":
            field_sizes.append(len(cur) - 1)
            cur = last_line[idx]
        else:
            cur += " "
    field_sizes.append(len(cur))

    for line in raw_lines[:-1]:
        temp = []
        prev_idx = 0
        for size in field_sizes:
            temp.append(line[prev_idx : prev_idx + size])
            prev_idx = prev_idx + size + 1
        res.append(temp)
    res.append(raw_lines[-1].split())
    return res


def calculate_part2(lines: list[list[str]]) -> int:
    statements = list(zip(*lines))
    res = 0
    for stmt in statements:
        numbers = []
        for digits in zip(*stmt[:-1]):
            numbers.append(int("".join(digits)))
        if stmt[-1] == "+":
            res += reduce(operator.add, numbers, 0)
        elif stmt[-1] == "*":
            res += reduce(operator.mul, numbers, 1)
        else:
            raise Exception("Unknown operator")

    return res


if __name__ == "__main__":
    pprint(calculate_part2(read_file_part2("day6/sample.txt")))
    pprint(calculate_part2(read_file_part2("day6/input.txt")))
