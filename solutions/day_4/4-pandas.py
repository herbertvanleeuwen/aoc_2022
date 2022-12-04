from pandas import Interval


def load_data() -> list[str]:
    with open('data/input_day4.txt') as file:
        return file.read().split('\n')


def create_interval(section: list[str]) -> Interval:
    return Interval(int(section[0]), int(section[1]), closed='both')


def get_overlap(assignment_pairs: list[str]) -> tuple[int]:
    fully_contained = 0
    overlapping = 0
    for assignment_pair in assignment_pairs:
        pairs = [create_interval(section.split('-')) for section in assignment_pair.strip().split(',')]
        if pairs[0] in pairs[1] or pairs[1] in pairs[0] :
            fully_contained += 1
        if pairs[0].overlaps(pairs[1]):
            overlapping +=1
    return fully_contained, overlapping


if __name__ == "__main__":
    assignment_pairs = load_data()
    fully_contained, overlapping = get_overlap(assignment_pairs)
    print(fully_contained)
    print(overlapping)
