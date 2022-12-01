if __name__ == "__main__":
    with open("data/input_day1.txt") as file:
        snack_calorie_list_per_elf = [[int(snack) for snack in (elf.split('\n'))] for elf in file.read().split('\n\n')]
        
    print(f'Number of elfs {len(snack_calorie_list_per_elf)}')
    print(f'Maximum calories of all {max(map(sum, snack_calorie_list_per_elf))}')
    print(f'Sum of calories for top 3 elfs {sum(sorted(map(sum, snack_calorie_list_per_elf))[-3:])}')