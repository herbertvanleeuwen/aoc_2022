def load_data() -> list[str]:
    with open("data/input_day4.txt") as file:
        return file.read().split("\n")


def get_overlap(assignment_pairs: list[str]) -> tuple[int, int]:
    fully_contained = 0
    overlapping = 0
    for pair in assignment_pairs:
        pairs = list(
            map(
                int,
                [plot for section in pair.strip().split(",") for plot in section.split("-")],
            )
        )
        if (pairs[0] <= pairs[2] and pairs[1] >= pairs[3]) or (pairs[2] <= pairs[0] and pairs[3] >= pairs[1]):
            fully_contained += 1
        if (
            ((pairs[0] >= pairs[2]) and (pairs[0] <= pairs[3])) or ((pairs[0] >= pairs[2]) and (pairs[0] <= pairs[3]))
        ) or (
            ((pairs[2] >= pairs[0]) and (pairs[2] <= pairs[1])) or ((pairs[3] >= pairs[0]) and (pairs[3] <= pairs[1]))
        ):
            overlapping += 1

    return fully_contained, overlapping


if __name__ == "__main__":
    assignment_pairs = load_data()
    fully_contained, overlapping = get_overlap(assignment_pairs)
    print(fully_contained)
    print(overlapping)
