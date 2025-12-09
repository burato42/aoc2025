from pprint import pprint

type Diagram = list[list[str]]


def read_file(file_path: str) -> Diagram:
    diagram = []
    with open(file_path) as file:
        for line in file.readlines():
            diagram.append([el for el in line.strip()])

    return diagram


def propagate(diagram: Diagram) -> int:
    splits = 0
    for h in range(1, len(diagram)):
        for l in range(len(diagram[0])):
            if diagram[h - 1][l] in ("S", "|") and diagram[h][l] != "^":
                diagram[h][l] = "|"
            elif diagram[h][l] == "^" and diagram[h - 1][l] == "|":
                if l == 0:
                    diagram[h][l + 1] = "|"
                elif l == len(diagram[0]) - 1:
                    diagram[h][l - 1] = "|"
                else:
                    diagram[h][l + 1] = "|"
                    diagram[h][l - 1] = "|"
                splits += 1

    return splits


def quantum_propagate(diagram: Diagram) -> int:
    rows = len(diagram)
    cols = len(diagram[0]) if rows > 0 else 0

    start_l = diagram[0].index("S")
    memo = {}

    def dfs(h, l):
        if (h, l) in memo:
            return memo[(h, l)]
        if h == rows - 1:
            return 1
        ways = 0

        if diagram[h + 1][l] == ".":
            ways += dfs(h + 1, l)
        elif diagram[h + 1][l] == "^":
            if l > 0:
                ways += dfs(h + 1, l - 1)
            if l < cols - 1:
                ways += dfs(h + 1, l + 1)

        memo[(h, l)] = ways
        return ways

    return dfs(0, start_l)


if __name__ == "__main__":
    # pprint(propagate(read_file("day7/sample.txt")))
    # pprint(propagate(read_file("day7/input.txt")))
    pprint(quantum_propagate(read_file("day7/sample.txt")))
    pprint(quantum_propagate(read_file("day7/input.txt")))
