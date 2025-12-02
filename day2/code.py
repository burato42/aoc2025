from typing import Generator


def get_ranges(rec: str) -> tuple[int, ...]:
    return tuple(int(x) for x in rec.strip().split("-"))


def read_file(file_path, chunk_size=1024) -> Generator[tuple[int, ...], None, None]:
    with open(file_path, "r") as file:
        buffer = ""
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            buffer += chunk
            while "," in buffer:
                rec, buffer = buffer.split(",", 1)
                yield get_ranges(rec)

        if buffer.strip():
            yield get_ranges(buffer.strip())


def sum_wrong_ids(file_path: str) -> int:
    result = []
    for record in read_file(file_path):
        for id_ in range(record[0], record[1] + 1):
            str_id = str(id_)
            size = len(str_id)
            if size % 2 == 0 and str_id[: size // 2] == str_id[size // 2 :]:
                result.append(int(str_id))
    return sum(set(result))


def sum_wrong_ids_advanced(file_path: str) -> int:
    result = []
    for record in read_file(file_path):
        for id_ in range(record[0], record[1] + 1):
            str_id = str(id_)
            size = len(str_id)
            for i in range(1, size // 2 + 1):
                if size % i == 0 and str_id[:i] * (size // i) == str_id:
                    result.append(int(str_id))

    return sum(set(result))


if __name__ == "__main__":
    file_path = "day2/input.txt"
    print(sum_wrong_ids(file_path))
    print(sum_wrong_ids_advanced(file_path))
