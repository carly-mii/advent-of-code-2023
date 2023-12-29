import os
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
with open(file_path, "r") as file:
    inputs = file.read().splitlines()

card_map = dict(zip(['A', 'K', 'Q', 'T'] + list(map(str, range(9, 1, -1))) + ['J'], 
                    [chr(i) for i in range(ord('a'), 1000)]))

for i, line in enumerate(inputs):
    hand, bid = line.split()
    
    for card in card_map:
        hand = hand.replace(card, card_map[card])
    
    inputs[i] = (hand, int(bid))

type_map = {
    (5,): 6,
    (1, 4): 5,
    (2, 3): 4,
    (1, 1, 3): 3,
    (1, 2, 2): 2,
    (1, 1, 1, 2): 1,
    (1, 1, 1, 1, 1): 0

}
def hand_type(a) -> int:
    htype = sorted([a[0].count(c) for c in set(card_map.values()) - set(['m'])])
    htype[-1] += 5 - sum(htype)
    htype = list(filter(lambda x: x != 0, htype))
    return type_map[tuple(htype)]

inputs.sort(key = lambda x: x[0])
inputs.sort(key = hand_type, reverse = True)
total = 0
for i, bid in zip(range(len(inputs), 0, -1), map(lambda x: x[1], inputs)):
    total += i*bid
print(total)
    

    

        
    