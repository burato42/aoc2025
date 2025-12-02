from typing import List


def read_input(file_path: str) -> List[int]:
    rotations = []
    with open(file_path) as file:
        for line in file.readlines():
            if line.startswith("L"):
                rotations.append(-int(line[1:]))
            else:
                rotations.append(int(line[1:]))
    return rotations


def get_code(initial_code: int, rotations: List[int]) -> int:
    code = initial_code
    counter = 0
    for rotation in rotations:
        if code == 0:
            counter += 1
        code = (code + rotation) % 100

    if code == 0:
        counter += 1
    return counter


def get_complex_code(initial_code: int, rotations: List[int]) -> int:
    code = initial_code
    counter = 0
    if code == 0:
        counter += 1
    for rotation in rotations:
        tmp_code = code + rotation

        if tmp_code >= 100:
            counter += tmp_code // 100
        elif tmp_code <= 0:
            counter += abs(tmp_code // 100)
            if tmp_code % 100 == 0:
                counter += 1
            elif code == 0:
                counter -= 1

        code = tmp_code % 100

    return counter


def main():
    rotations = read_input("day1/input1.txt")
    print(get_code(50, rotations))
    print(get_complex_code(50, rotations))


if __name__ == "__main__":
    main()
