#Part 1 for Day 1

def part1():
    file = open("inputs1.txt", "r")
    n = 50
    count = 0
    for line in file:
        n += int(line[1:]) * (-1 if line[0:1] == 'L' else 1)
        if(n % 100 == 0):
            count += 1
    print(count)

part1()

def part2():
    file = open("inputs1.txt", "r")
    n = 50
    count = 0
    for line in file:
        c = int(line[1:]) % 100
        count +=  int(line[1:]) // 100
        n += int(c) * (-1 if line[0:1] == 'L' else 1)
        if(n % 100 == 0):
            count += 1
    print(count)

part2()