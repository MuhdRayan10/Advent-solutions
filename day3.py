import string

priority_rate = {n:i for i, n in enumerate(list(string.ascii_letters), 1)}

with open("day3.txt", "r") as f:
    data = [x.replace("\n", "") for x in f.readlines()]

priority = 0
for line in data:
    point = len(line)//2
    priority += priority_rate[[l for l in line[:point] if l in line[point:]][0]]

print(priority)

#part 2
count = -1
teams = [[]]
for d in data:
    if count < 2:
        count += 1
        teams[-1].append(d)
    else:
        teams.append([d])
        count = 0

priority = 0
for team in teams:
    badge = [x for x in team[0] if x in team[1] and x in team[2]][0]
    priority += priority_rate[badge]

print(priority)