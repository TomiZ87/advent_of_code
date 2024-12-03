import re
def load():
    with open("./src/day03/input.txt", mode="r", encoding="UTF-8") as file:
         rows = file.read()
         return rows
    
def part_one(input_txt):
    sum_mul = 0
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input_txt)
    for x in range(len(matches)):
        sum_mul += (int(matches[x][0]) * int(matches[x][1]))
    return sum_mul

def part_two(input_txt):
    sum_mul = 0
    input_txt = input_txt.split("do()")
    for x in input_txt:
        x = x.split("don't()", 1)[0]
        sum_mul += part_one(x)
    print(sum_mul)

def main():
    input_txt = load()
    p_1 = part_one(input_txt)
    print(p_1)
    part_two(input_txt)

if __name__ == "__main__":
     main()
