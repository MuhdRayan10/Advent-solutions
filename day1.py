with open("day1.txt","r") as f:
    data = [x.replace("\n", "") for x in f.readlines()]

calories = {}
elf = 1
for calorie in data:
    if calorie == "":
        elf += 1
    else:
        calories[elf] = calories.get(elf, 0) + int(calorie)

#top elf
print(max(list(calories.values())))

#top 3 elf
print(sum(sorted(list(calories.values()), reverse=True)[:3]))