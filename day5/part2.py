import os
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
with open(file_path, "r") as file:
    text = file.read().strip()

# parsing is horrendous as always
maps = text.split('\n\n')
seeds = list(map(int, maps.pop(0).split(':')[1].split()))
seed_list = []
for s, r in zip(seeds[::2], seeds[1::2]):
    seed_list.append(range(s, s+r))

def parse_map(m: str):
    lines = m.split('\n')[1:] # since maps go in order we don't actually care about the names
    def parse_line(line):
        ds, ss, r = list(map(int, line.split(" ")))
        return (range(ss, ss+r), range(ds, ds+r))
    return list(map(parse_line, lines))

maps = list(map(parse_map, maps))

# no because what the fuck is this lol why did I use ranges
# also could shrink this a layer because technically I'm
# going through the seeds in two loops :(
locs = []
for s in seed_list:
    unmatched = [s]
    for m in maps:
        match_dests = []
        while len(unmatched) > 0:
            s = unmatched.pop(0)
            for sr, dr in m:
                if not (s[0] > sr[-1] or s[-1] < sr[0]):
                    start = max(s[0], sr[0])
                    end = min(s[-1], sr[-1])
                    dest = range(dr[start - sr[0]], dr[end - sr[0]]+1)
                    match_dests.append(dest)
                    if s[0] < start:
                        u = range(s[0], start)
                        unmatched.append(u)
                    if s[-1] > end:
                        u = range(end+1, s[-1]+1)
                        unmatched.append(u)     
                    break
            else:
                match_dests.append(s)
        unmatched = match_dests
            
    locs.extend(match_dests)
    # print(f"final dest: {s}\n")

mins = map(lambda r: r[0], locs)
print(min(mins))
        

        
        

