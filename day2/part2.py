with open("./input.txt", 'r') as f:
    lines = f.read().split('\n')

total = 0
for line in lines:
    colors = {"red": 0, "green": 0, "blue": 0}
    game, results = line.split(": ")
    id = int(game.split(' ')[1])
    rounds = results.split("; ")
    for round in rounds:
        draws = round.split(", ")
        for draw in draws:
            num, color = draw.split(' ')
            num = int(num)
            if num > colors[color]:
                colors[color] = num

    power = colors["red"]*colors["green"]*colors["blue"]
    total += power
   
print(total)
