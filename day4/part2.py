with open("input.txt", 'r') as f:
    lines = f.read().strip().split('\n')

for i, line in enumerate(lines):
    line = line.split(':')[1]
    win, you = line.split('|')
    win = list(map(int, win.split()))
    you = list(map(int, you.split()))
    
    lines[i] = (win, you)

cards_won = {}
def find_cards_won(i: int):
    if i in cards_won:
        return cards_won[i]
    
    w, y = lines[i]
    n = len(set(w) & set(y))
    acc = n
    for j in range(i+1, i+1+n):
        acc += find_cards_won(j)
    
    cards_won[i] = acc
    return acc

total_cards = 0
for i, line in enumerate(lines):
    total_cards += find_cards_won(i) + 1

    
print(total_cards)