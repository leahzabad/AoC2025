#Day 2 solution Part 1

file = open("inputs2.txt", "r")
line = file.readline()
numbers = line.split(",")
invalids = []

def find_invalid(start, end):
    for i in range(int(start), int(end)+1):
        print(i)
        i_str = str(i)
        #print(i)
        if(len(i_str) % 2 == 0):
            i_half = (len(str(i))//2)
            if(i_str[:i_half] == i_str[i_half:]):
                invalids.append(i)
            elif(i_str.count(i_str[0]) == len(i_str)):
                invalids.append(i)

for index in numbers:
    pairs = index.split("-")
    print(pairs)
    find_invalid(pairs[0], pairs[1])

result = 0
print(invalids)
for n in invalids:
    result += n

print(result)