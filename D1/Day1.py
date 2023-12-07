# Sol Steele
import re

def part_one():
    with open("input") as f:
        total = 0
        for line in f:
            num = [c for c in line if c.isdigit()]
            total += int(num[0]+num[-1])
        print(total)


# part 1 hard:
print(sum([int(a[0]+a[-1])for a in[[c for c in l if c.isdigit()]for l in open("a")]]))
print(sum(int(a[0]+a[-1])for a in("".join(filter(str.isdigit,l))for l in open("a"))))
print(sum(int(a[0]+a[-1])for a in(list(filter(str.isdigit,l))for l in open("a"))))
print(sum(int(a[0]+a[-1])for a in(re.sub("\D","",i)for i in open("a"))))



test = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".split("\n")

numbers = {
    "one": "1",
    "two": "2",
    "six": "6",
    "four": "4",
    "five": "5",
    "nine": "9",
    "three": "3",
    "seven": "7",
    "eight": "8",
}


def part_two():
    with open("input") as f:
        total = 0
        for line in f:
            num = ""
            for i, char in enumerate(line):
                for n in numbers:
                    if line[i:i+len(n)] == n:
                        num += numbers[n]
                if char.isdigit():
                    num += char
            total += int(num[0]+num[-1])
        print(total)

def part_two_hard():
    number = ["one","two","six","four","five","nine","three","seven","eight","nine"]
    with open("input") as f:
        total = 0
        for line in f:
            num = ""
            for i, char in enumerate(line):
                for n in numbers:
                    if line[i:i+len(n)] == n:
                        num += numbers[n]
                if char.isdigit():
                    num += char
            total += int(num[0]+num[-1])
        print(total)

part_one()
part_two()
