def load_data() -> list[str]:
    with open('data/input_day4.txt') as file:
        return file.read().split('\n')


def generate_full_set(section: list[str]) -> set:
    return set(range(int(section[0]), int(section[1]) +1 ))


def get_overlap(assignment_pairs: list[str]) -> tuple[int, int]:
    fully_contained = 0
    overlapping = 0
    for assignment_pair in assignment_pairs:
        pairs = [generate_full_set(section.split('-')) for section in assignment_pair.strip().split(',')]
        if pairs[0].issubset(pairs[1]) or pairs[1].issubset(pairs[0]):
            fully_contained += 1
        if bool(pairs[0] & pairs[1]):
            overlapping +=1
    return fully_contained, overlapping


if __name__ == "__main__":
    assignment_pairs = load_data()
    fully_contained, overlapping = get_overlap(assignment_pairs)
    print(fully_contained)
    print(overlapping)
