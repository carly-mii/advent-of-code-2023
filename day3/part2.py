with open("input.txt", 'r') as f:
    lines = f.read().strip().split('\n')

def adjacent_nums(i: int, j: int) -> list[int]:
    num_info = set()

    for r in range(i-1, i+2):
        for c in range(j-1, j+2):
            if 0 <= r < len(lines) and 0 <= c < len(lines[i]):
                if lines[r][c].isdigit():
                    # short circuit prevents the [6*....] edge case from throwing error
                    i1, i2 = c, c
                    while i1 > 0 and lines[r][i1-1].isdigit():
                        i1 -= 1
                    while i2 < len(lines[i]) and lines[r][i2].isdigit(): # ends up 1 past
                        i2 += 1
                
                    num_info.add((r, i1, int(lines[r][i1:i2])))

    return {e[-1] for e in num_info}
    


n = [str(i) for i in range(10)]
sum = 0

for i, line in enumerate(lines):
    for j, c in enumerate(line + '.'):
        if c == '*':
            nums = list(adjacent_nums(i, j))
            if len(nums) == 2:
                sum += nums[0] * nums[1]
            


print(sum)


        
