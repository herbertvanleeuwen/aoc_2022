def load_data() -> list[list[int]]:
    with open("data/input_day1.txt") as file:
        return [[int(snack) for snack in (elf.split("\n"))] for elf in file.read().split("\n\n")]


if __name__ == "__main__":
    print(f"Number of elfs {len(load_data())}")
    print(f"Maximum calories of all {max(map(sum, load_data()))}")
    print(f"Sum of calories for top 3 elfs {sum(sorted(map(sum, load_data()))[-3:])}")
