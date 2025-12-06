from pprint import pprint
from typing import Optional

type Plan = list[list[str]]


def read_input(file_path: str) -> Plan:
    result = []
    with open(file_path) as file:
        row = []
        for line in file.readlines():
            for el in line.strip():
                row.append(el)
            result.append(row)
            row = []
    return result


def is_roll_available(i: int, j: int, plan: Plan) -> bool:
    if plan[i][j] != "@":
        return False
    cnt = 0
    for x in [i - 1, i, i + 1]:
        if 0 <= x < len(plan):
            for y in [j - 1, j, j + 1]:
                if (
                    0 <= y < len(plan[0])
                    and (x, y) != (i, j)
                    and plan[x][y] in ("@", "x")
                ):
                    cnt += 1
    return cnt < 4


def count_rolls(plan: Plan) -> int:
    counter = 0
    for m in range(len(plan)):
        for n in range(len(plan[0])):
            if is_roll_available(m, n, plan):
                counter += 1
    return counter


def remove_rolls(plan: Plan, cnt: int) -> tuple[Optional[Plan], int]:
    counter = 0
    for m in range(len(plan)):
        for n in range(len(plan[0])):
            if is_roll_available(m, n, plan):
                plan[m][n] = "x"
    for m in range(len(plan)):
        for n in range(len(plan[0])):
            if plan[m][n] == "x":
                counter += 1
                plan[m][n] = "."
    if counter == 0:
        return None, cnt
    return plan, cnt + counter


def count_all_rolls(plan: Plan) -> int:
    count = 0
    while plan:
        plan, count = remove_rolls(plan, count)
    return count


if __name__ == "__main__":
    pprint(count_rolls(read_input("day4/sample.txt")))
    pprint(count_rolls(read_input("day4/input.txt")))
    pprint(count_all_rolls(read_input("day4/sample.txt")))
    pprint(count_all_rolls(read_input("day4/input.txt")))
