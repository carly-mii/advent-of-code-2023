import os
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
with open(file_path, "r") as file:
    text = file.read().strip()

# parsing is horrendous as always
maps = text.split('\n\n')
seeds = list(map(int, maps.pop(0).split(':')[1].split()))

def parse_map(m: str):
    lines = m.split('\n')[1:] # since maps go in order we don't actually care about the names
    def parse_line(line):
        ds, ss, r = list(map(int, line.split(" ")))
        return (range(ss, ss+r), range(ds, ds+r))
    return list(map(parse_line, lines))

maps = list(map(parse_map, maps))

locs = []
for s in seeds:
    for m in maps:
        for sr, dr in m:
            if s in sr:
                s = dr[s - sr[0]]
                break
    locs.append(s)
    # print(f"final dest: {s}\n")

print(min(locs))
        

        
        

