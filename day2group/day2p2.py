#Day 2 solution

file = open("inputs2.txt", "r")
line = file.readline()
numbers = line.split(",")
invalids = []

def find_invalid(start, end):
    for i in range(int(start), int(end)+1):
        i_str = str(i)
        i_half = (len(str(i))//2)
        if(len(i_str) == 10):
            if (i_str[:i_half] == i_str[i_half:]):
                invalids.append(i)

        elif(len(i_str) % 2 == 0):
            if (i_str.count(i_str[0]) == len(i_str)):
                invalids.append(i)
            else:
                for h in range (i_half, 0, -1):
                    print("Part: ", (i_str[0:h]), " Whole: ", i_str)
                    print("comp ", i_str.count(i_str[0:h]), " == ", len(i_str)//h)
                    if(i_str.count(i_str[0:h]) == len(i_str)//h):
                        invalids.append(i)
                        break
        else:
            if (i_str.count(i_str[0]) == len(i_str)):
                invalids.append(i)
            else:
                for h in range (i_half, 0, -1):
                    print("Part: ", (i_str[0:h]), " Whole: ", i_str)
                    print("comp ", i_str.count(i_str[0:h]), " == ", len(i_str) // h)
                    if(i_str.count(i_str[0:h]) == len(i_str)//h):
                        invalids.append(i)
                        break


for index in numbers:
    pairs = index.split("-")
    print(pairs)
    find_invalid(pairs[0], pairs[1])


result = 0
print(invalids)
for n in invalids:
    result += n

print(result)