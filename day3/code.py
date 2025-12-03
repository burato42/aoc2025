from typing import Callable


def read_input(file_path) -> list[list[int]]:
    result = []
    with open(file_path) as file:
        for line in file.readlines():
            battery = []
            for digit in line.strip():
                battery.append(int(digit))
            result.append(battery)
    return result


def find_max_joltage(battery: list[int]) -> int:
    max_joltage = 0
    max_joltage_idx = 0
    for idx, joltage in enumerate(battery[:-1]):
        if joltage > max_joltage:
            max_joltage = joltage
            max_joltage_idx = idx
    second_max_joltage = max(battery[max_joltage_idx + 1 :])

    return max_joltage * 10 + second_max_joltage


def sum_joltages(
    max_func: Callable[[list[int]], int], batteries: list[list[int]]
) -> int:
    return sum([max_func(battery) for battery in batteries])


def find_max_joltage_long(battery: list[int]) -> int:
    res = []
    max_idx = -1
    for i in range(12):
        if i == 11:
            max_val = max(battery[max_idx + 1 :])
        else:
            max_val = max(battery[max_idx + 1 : -12 + i + 1])
        max_idx = max_idx + 1 + battery[max_idx + 1 :].index(max_val)
        res.append(max_val)
    return int("".join([str(x) for x in res]))


if __name__ == "__main__":
    print(sum_joltages(find_max_joltage, read_input("day3/sample.txt")))
    print(sum_joltages(find_max_joltage, read_input("day3/input.txt")))
    print(sum_joltages(find_max_joltage_long, read_input("day3/sample.txt")))
    print(sum_joltages(find_max_joltage_long, read_input("day3/input.txt")))
