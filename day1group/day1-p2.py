#Part 2 for Day 1
file = open("inputs1.txt", "r")
nb = 50
final = 0

def indexing(c, n, l):
    count = (c // 100)
    c = c % 100
    inc = 1
    if (n == 0):
        count += inc
        inc = 0
    if(l == "L"):
        if((n - c) < 0):
            count += inc
            n = (n - c) + 100
        else:
          n -= c
    elif(l == "R"):
        if((n + c) > 100):
            count += inc
            n = (n + c) - 100
        elif((n + c) == 100):
            n = 0
        else:
            n += c
    return count, n

for line in file:
    change = int(line[1:])
    letter = line[0:1]
    result, nb = indexing(change, nb, letter)
    final += result

print(final)
