with open("input.txt", 'r') as f:
    lines = f.read().strip().split('\n')

def is_adjacent(i: int, start: int, end: int) -> bool:


    for r in range(i-1, i+2):
        for c in range(start-1, end+2):
            if 0 <= r < len(lines) and 0 <= c < len(lines[i]):
                if not lines[r][c].isdigit() and lines[r][c] != '.':
                    return True

    return False
    


n = [str(i) for i in range(10)]
sum = 0

for i, line in enumerate(lines):
    possible_num = False
    start, end = 0, 0

    for j, c in enumerate(line + '.'):
        if c in n:
            if possible_num:
                end += 1
            else:
                start = j
                end = j
                possible_num = True
        elif possible_num:
            if is_adjacent(i, start, end):
                sum += int(line[start:end+1])
            
            possible_num = False

print(sum)


        
