with open("day4.txt", "r") as f:
    pairs = [x.replace("\n", "").split(",") for x in f.readlines()]

count = 0
for pair in pairs:
    start, end = [int(n) for n in pair[0].split("-")]
    start2, end2 = [int(n) for n in pair[1].split("-")]

    if (start >= start2 and end <= end2) or (start2 >= start and end2 <= end):
        count += 1

print(count)
    
# part 2
count = 0
for pair in pairs: 
    start, end = [int(n) for n in pair[0].split("-")]
    start2, end2 = [int(n) for n in pair[1].split("-")]

    print(start, end, start2, end2)

    if (end >= start2 and start <= end2):
        count += 1
        print("overlap!")

print(count)