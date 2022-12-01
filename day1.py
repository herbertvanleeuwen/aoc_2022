if __name__ ==  "__main__":
    
    with open("data/input_day1.csv") as file:
        snacks_calories = file.read().split('\n') 
    
    # Create final list for total calorie count per elf
    total_calories_per_elf = []        

    # Create temp list to store snacks per elf
    temp_snack_list = []    
    for snack in snacks_calories:
        if snack == '':
            # Add total calorie count for elf to list
            total_calories_per_elf.append(sum(temp_snack_list))
            # Reset temp list
            temp_snack_list = []
            continue
        # Add snack to list 
        temp_snack_list.append(int(snack))

    # Sort list of calorie totals
    total_calories_per_elf.sort()

    # Print results
    print(f'Number of elfs {len(total_calories_per_elf)}')
    print(f'Maximum calories of all {total_calories_per_elf[-1]}')
    print(f'Sum of calories for top 3 elfs {sum(total_calories_per_elf[-3:])}')