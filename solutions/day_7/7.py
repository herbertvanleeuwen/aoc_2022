def load_data() -> list[str]:
    with open("data/input_day7.txt") as file:
        return file.readlines()


def create_directory_dict(commands: list[str]) -> dict[str, int]:
    directories: dict[str, int] = {}
    directory_history = [""]
    for command in commands:
        if command.startswith("$ cd .."):
            # remove cleared directory
            directory_history.pop()
        elif command.startswith("$ cd "):
            # add directory to command history
            directory_history.append(f"{directory_history[-1]}/{command}")
        elif command.split()[0].isdigit():
            file_size = int(command.split(" ")[0])
            for dir in directory_history:
                if dir in directories.keys():
                    directories[dir] += file_size
                else:
                    directories[dir] = file_size
    return directories


def determine_storage_needed(storage_used, update_size=30000000, total_storage=70000000):
    return update_size - (total_storage - storage_used)


if __name__ == "__main__":
    directories = create_directory_dict(load_data())
    storage_needed = determine_storage_needed(directories[""])
    print(f"Part 1: {sum(size for size in directories.values() if size <= 100000)}")
    print(f"Part 2: {min(size for size in directories.values() if size > storage_needed)}")
