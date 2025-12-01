#Part 1 for Day 1
#test
file = open("inputs1.txt", "r")
nb = 50
count = 0

def indexing(c, n, l):
    c = c % 100
    if(l == "L"):
        if((n - c) < 0):
            n = (n - c) + 100
        else:
          n -= c
    if(l == "R"):
        if((n + c) > 99):
            n = (n + c) - 100
        else:
            n += c
    print(n)
    return n

for line in file:
    change = int(line[1:])
    letter = line[0:1]
    nb = indexing(change, nb, letter)
    if(nb == 0):
        count += 1

print(count)
