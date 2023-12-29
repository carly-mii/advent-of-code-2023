import os
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
with open(file_path, "r") as file:
    inputs = file.read().splitlines()

card_map = dict(zip(['A', 'K', 'Q', 'J', 'T'] + list(map(str, range(9, 1, -1))), 
                    [chr(i) for i in range(ord('a'), 1000)]))

for i, line in enumerate(inputs):
    hand, bid = line.split()
    hs = hand
    bid = int(bid)
    
    for card in card_map:
        hand = hand.replace(card, card_map[card])
    
    inputs[i] = (hand, bid, hs)

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
    htype = list(filter(lambda x: x != 0, [a[0].count(c) for c in card_map.values()]))
    return type_map[tuple(sorted(htype))]

inputs.sort(key = lambda x: x[0])
inputs.sort(key = hand_type, reverse = True)
total = 0
for i, bid in zip(range(len(inputs), 0, -1), map(lambda x: x[1], inputs)):
    total += i*bid
print(total)
    

    

        
    