def load_data():
    with open("data/input_day5.txt") as file:
        input = file.read().split("\n\n")
        start_stacks = input[0].splitlines()[:-1]
        instructions = input[1].splitlines()
    return start_stacks, instructions


def get_starting_stacks_as_list(start_stacks: list[str]) -> list[list[str]]:
    number_of_stacks = len(start_stacks)
    # Iniate empty list of list
    stacks = [[] for _ in range(number_of_stacks + 1)]

    # For every layer put the crate in the list corresponding to the right stack
    for layer in range(-1, -(number_of_stacks) - 1, -1):
        for stack, crate in enumerate(start_stacks[layer][1::4]):
            # skip positions if there is no crate
            if crate != " ":
                stacks[stack].append(crate)
    return stacks


def get_instructions_as_ints(instructions):
    int_instructions = []
    for ins in instructions:
        _, number_of_crates, _, from_stack, _, to_stack = ins.split()
        int_instructions.append([int(number_of_crates), int(from_stack), int(to_stack)])
    return int_instructions


def move_crates(int_instructions, stacks):
    stacks_deep_copy = [stack.copy() for stack in stacks]
    for number_of_crates, from_stack, to_stack in int_instructions:
        for j in range(0, number_of_crates):
            stacks[to_stack - 1].append(stacks[from_stack - 1][-1])
            stacks[from_stack - 1].pop()
            stacks_deep_copy[to_stack - 1].append(stacks_deep_copy[from_stack - 1][j - number_of_crates])
            stacks_deep_copy[from_stack - 1].pop(j - number_of_crates)

    return stacks, stacks_deep_copy


if __name__ == "__main__":
    start_stacks, instructions = load_data()
    stacks = get_starting_stacks_as_list(start_stacks)
    int_instructions = get_instructions_as_ints(instructions)
    results = move_crates(int_instructions, stacks)

    print("Part 1:", "".join([stack[-1] for stack in results[0]]))
    print("Part 2:", "".join([stack[-1] for stack in results[1]]))
