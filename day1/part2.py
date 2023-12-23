with open("./day1_input.txt", 'r') as f:
    lines = f.read().split('\n')

digits = [str(i) for i in range(10)] + ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def str_to_num(str_):
    if len(str_) > 1:
        return digits.index(str_) - 9
    return int(str_)

total = 0
for line in lines:
    lowest_id = len(line)
    highest_id = -1

    first_num = 0
    last_num = 0
    for d in digits:
        id1 = line.find(d)
        id2 = line.rfind(d)
        if id1 != -1:
            if id1 < lowest_id:
                lowest_id = id1
                first_num = str_to_num(d)
            if id2 > highest_id:
                highest_id = id2
                last_num = str_to_num(d)

    total += first_num*10 + last_num

print(total)
    
