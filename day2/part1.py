with open("./input.txt", 'r') as f:
    lines = f.read().split('\n')

total = 0
colors = {"red": 12, "green": 13, "blue": 14}
for line in lines:
    game, results = line.split(": ")
    id = int(game.split(' ')[1])
    rounds = results.split("; ")
    valid = True
    for round in rounds:
        draws = round.split(", ")
        for draw in draws:
            num, color = draw.split(' ')
            num = int(num)
            if num > colors[color]:
                valid = False
                break
        if not valid:
            break
    if valid:
        total += id
print(total)
