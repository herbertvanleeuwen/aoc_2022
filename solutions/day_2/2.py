if __name__ == "__main__":
    with open('data/input_day2.txt') as file:
        games=list(map(str.split, file.read().split('\n')))

    total_score = 0
    for game in games:
        score = 0
        if game[1] == 'X':
            score += 1
            if game[0] == 'A':
                score += 3
            elif game[0] == 'C':
                score += 6
        elif game[1] == 'Y':
            score += 2
            if game[0] == 'B':
                score += 3
            elif game[0] == 'A':
                score += 6
        elif game [1] == 'Z':
            score += 3
            if game[0] == 'C':
                score += 3
            elif game[0] == 'B':
                score += 6
        total_score += score 
    print(total_score)

    # X means lose 
    # Y means Draw 
    # Z means Win
    total_score = 0
    for game in games:
        score = 0
        print(game)
        if game[1] == 'X':
            score += 0
            if game[0] == 'A':
                score += 3
            elif game[0] == 'B':
                score += 1
            elif game[0] == 'C':
                score += 2
        elif game[1] == 'Y':
            score += 3
            if game[0] == 'A':
                score += 1
            elif game[0] == 'B':
                score += 2
            elif game[0] == 'C':
                score += 3
        elif game [1] == 'Z':
            score += 6
            if game[0] == 'A':
                score += 2
            elif game[0] == 'B':
                score += 3
            elif game[0] == 'C':
                score += 1

        print(score)
        total_score += score

    print(total_score)
