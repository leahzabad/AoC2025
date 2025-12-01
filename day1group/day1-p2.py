#Part 2 for Day 1
#test
file = open("inputs1.txt", "r")
nb = 50
final = 0

def indexing(c, n, l):
    count = 0
    count += (c // 100)
    c = c % 100
    if(l == "L"):
        if((n - c) < 0):
            count +=1
            #print("increment count cuz n - c => ", n, " - ", c, " = ", (n-c))
            n = (n - c) + 100
        else:
          n -= c
    elif(l == "R"):
        if((n + c) > 100):
            count += 1
            #print("increment count cuz n + c => ", n, " + ", c, " = ", (n + c))
            n = (n + c) - 100
        else:
            n += c
    if(n == 0):
        count += 1
        #print("increment count cuz n = 0")
    #print("final n: ", n)
    return count, n

for line in file:
    change = int(line[1:])
    letter = line[0:1]
    result, nb = indexing(change, nb, letter)
    final += result

print(final)
