with open("input.txt", 'r') as f:
    lines = f.read().strip().split('\n')

for i, line in enumerate(lines):
    line = line.split(':')[1]
    lines[i] = tuple((nums.split() for nums in line.split('|')))

card_appears = [1]*len(lines)
total_cards = 0
for i, (w, y) in enumerate(lines):
    n = len(set(w) & set(y))
    for j in range(i+1, i+1+n):
        card_appears[j] += card_appears[i]

print(sum(card_appears))