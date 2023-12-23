with open("input.txt", 'r') as f:
    lines = f.read().strip().split('\n')

for i, line in enumerate(lines):
    line = line.split(':')[1]
    win, you = line.split('|')
    win = list(map(int, win.split()))
    you = list(map(int, you.split()))
    
    lines[i] = (win, you)

sum = 0
for win, you in lines:
    # this works if there are no duplicates allowed otherwise a dupe in
    # your list of numbers would be counted once
    n = len(set(win) & set(you))
    if n > 0:
        sum += 2**(n-1)
    
print(sum)