with open("./input.txt", 'r') as f:
    lines = f.read().split('\n')

digits = [str(i) for i in range(10)]
total = 0

for line in lines:
    for c1 in line:
        if c1 in digits:
            total += int(c1)*10
            break
    for c2 in line[::-1]:
        if c2 in digits:
            total += int(c2)
            break

print(total)

