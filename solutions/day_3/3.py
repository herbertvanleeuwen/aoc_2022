def load_data():
    with open("data/input_day3.txt") as file:
        return file.read().split('\n')


def generate_priority(item: str) -> int:
    """Function that takes an item and retuns the priority as integer"""
    o = ord(item)
    if 65 <= o <= 90:
        return o - 38
    if 97 <= o <= 122:
        return o - 96
    raise ValueError(f"Unexpected item: {item}")


# Part 1
def split_items_in_compartments(rugsack: str) -> list[str]:
    split_index = len(rugsack) // 2
    return (rugsack[:split_index], rugsack[split_index:])


def get_unique_items_per_compartment(rugsack: str) -> list[set]:
    return map(set, split_items_in_compartments(rugsack))


def get_missplaced_items(rugsack: str) -> str:
    return set.intersection(*get_unique_items_per_compartment(rugsack)).pop()


def sum_of_misplaced_items(rugsacks: list[str]) -> int:
    return sum(generate_priority(get_missplaced_items(rugsack)) for rugsack in rugsacks)


# Part 2
def get_unique_items_per_rugsack(group: list[str]):
    return map(set, group)


def get_group_badge(group: list[str]):
    return set.intersection(*get_unique_items_per_rugsack(group)).pop()


def sum_of_badges(rugsacks: list[str], number_of_elfs_per_group: int = 3) -> int:
    return sum(generate_priority(get_group_badge(rugsacks[i : i + number_of_elfs_per_group])) 
               for i in range(0, len(rugsacks), number_of_elfs_per_group))


if __name__ == "__main__":
    rugsacks = load_data()
    print(f'Sum of priority for misplaced items {sum_of_misplaced_items(rugsacks)}')
    print(f'Sum of priority of group badges {sum_of_badges(rugsacks)}')