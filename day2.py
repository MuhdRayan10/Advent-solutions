with open("day2.txt", "r") as f:
    guide = [x.replace("\n", "").split(" ") for x in f.readlines()]

#translate
shape = {'X':1, 'Y':2, 'Z':3, 'A':1, 'B':2, 'C':3}
guide = [(shape[x[0]], shape[x[1]]) for x in guide]

#calculate points
points = 0
for opp, pers in guide:
    points += pers
    points += 6 if opp + 1 == pers or pers + 2 == opp else 3 if opp == pers else 0

print(points)
    

#part 2
wrapping = {0:3, 1:1, 2:2, 3:3, 4:1}
points = 0
for opp, win in guide:
    points += (3 + opp) if win == 2 else wrapping[opp-1] if win == 1 else (6 + wrapping[opp+1])

print(points)

    
