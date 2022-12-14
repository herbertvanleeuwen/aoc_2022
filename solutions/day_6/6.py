def load_data() -> list[str]:
    with open("data/input_day6.txt", "r") as f:
        return [letter for letter in f.read().strip()]


def data_stream_processing(data_stream: list[str], nr_unique: int) -> int:
    for char_ix in range(0, len(data_stream) + 1):
        if len(set(data_stream[char_ix : char_ix + nr_unique])) == len((data_stream[char_ix : char_ix + nr_unique])):
            return char_ix + nr_unique
    raise Exception("Starting string not found")


if __name__ == "__main__":
    data_stream = load_data()
    print(f"Start of the packet: {data_stream_processing(data_stream, 4)}")
    print(f"Start of the message: {data_stream_processing(data_stream, 14)}")
