from pprint import pprint


def read_input(file_path: str) -> tuple[list[list[int]], list[int]]:
    intervals = []
    ids = []
    with open(file_path) as file:
        while line := file.readline().strip():
            start, end = [int(x) for x in line.split("-")]
            intervals.append([start, end])
        while line := file.readline().strip():
            ids.append(int(line))
    return intervals, ids


def brute_force_fresh(intervals: list[list[int]], ids: list[int]):
    counter = 0
    for id_ in ids:
        for interval in intervals:
            if id_ in range(interval[0], interval[1] + 1):
                counter += 1
                break
    return counter


def brute_force_fresh_ingredients(intervals: list[list[int]]):
    # not working
    res = set()
    for interval in intervals:
        for id_ in range(interval[0], interval[1] + 1):
            res.add(id_)
    return len(res)


def fresh_ingredients(intervals: list[list[int]]):
    return sum(interval[1] - interval[0] + 1 for interval in intervals)


def merge_intervals(intervals: list[list[int]]):
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]

    for i in range(1, len(intervals)):
        if intervals[i][0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], intervals[i][1])
        else:
            result.append([intervals[i][0], intervals[i][1]])

    return result


if __name__ == "__main__":
    print(brute_force_fresh(*read_input("day5/sample.txt")))
    print(brute_force_fresh(*read_input("day5/input.txt")))
    print(fresh_ingredients(merge_intervals(read_input("day5/sample.txt")[0])))
    print(fresh_ingredients(merge_intervals(read_input("day5/input.txt")[0])))
