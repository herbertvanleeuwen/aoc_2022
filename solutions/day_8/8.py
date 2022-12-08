def load_data():
    with open("data/input_day8.txt") as file:
        return file.read().splitlines()


def determine_visible_trees(forest: list[str]) -> set[tuple[int, int]]:
    max_y = len(forest)
    max_x = len(forest[0])
    visible_coordinates = set()
    for y in range(max_y):
        max_tree_height = -1
        for x in range(max_x):
            tree_height = int(forest[y][x])
            if tree_height > max_tree_height:
                visible_coordinates.add((y, x))
                max_tree_height = tree_height

        max_tree_height = -1
        for x in reversed(range(max_x)):
            tree_height = int(forest[y][x])
            if tree_height > max_tree_height:
                visible_coordinates.add((y, x))
                max_tree_height = tree_height

    for x in range(max_x):
        max_tree_height = -1
        for y in range(max_y):
            tree_height = int(forest[y][x])
            if tree_height > max_tree_height:
                visible_coordinates.add((y, x))
                max_tree_height = tree_height

        max_tree_height = -1
        for y in reversed(range(max_y)):
            tree_height = int(forest[y][x])
            if tree_height > max_tree_height:
                visible_coordinates.add((y, x))
                max_tree_height = tree_height

    return visible_coordinates


def determine_scenic_scores(forest: list[str]) -> list[int]:
    max_y = len(forest)
    max_x = len(forest[0])
    scenic_scores = []
    for y in range(max_y):
        for x in range(max_x):
            left, right, up, down = 0, 0, 0, 0
            tree_height = forest[y][x]

            # count left
            for i in reversed(range(0, x)):
                left += 1
                if forest[y][i] >= tree_height:
                    break

            # count right
            for i in range(x + 1, max_x):
                right += 1
                if forest[y][i] >= tree_height:
                    break

            # count down
            for i in range(y + 1, max_y):
                down += 1
                if forest[i][x] >= tree_height:
                    break

            # count up
            for i in reversed(range(0, y)):
                up += 1
                if forest[i][x] >= tree_height:
                    break

            scenic_scores.append(left * right * up * down)

    return scenic_scores


if __name__ == "__main__":
    print(f"Number of trees visible from outside the forest: {len(determine_visible_trees(load_data()))}")
    print(f"Maximum scenic score in the forest: {max(determine_scenic_scores(load_data()))}")
