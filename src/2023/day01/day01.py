import re
def load():
    with open("./src/2023/day01/input.txt", mode="r", encoding="UTF-8") as file:
         rows = file.readlines()         
         return rows

def part_one(input_txt):
    addition = 0
    digits = "0123456789"
    for x in input_txt:
        left = ""
        right = ""
        for y in x:
            if y in digits:
                left = y
                break
        for y in x[::-1]:
            if y in digits:
                right = y
                break 
        if left != "" or right != "":
            addition += (int(left + right))   
    print(addition)

def part_two(input_txt):
    addition = 0
    digits = "0123456789"
    digits_str = "one|two|three|four|five|six|seven|eight|nine"
    rev_digits_str = "enin|thgie|neves|xis|evif|ruof|eerht|owt|eno"
    dics = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    for x in range(len(input_txt)):
        left = ""
        right = ""
        string_left = re.search(digits_str, input_txt[x])
        string_right = re.search(rev_digits_str, input_txt[x][::-1])
        print(x, string_left, string_right)
        for y in range(len(input_txt[x])):
            if input_txt[x][y] in digits:
                left = input_txt[x][y]
                break
            if string_left is not None and string_left.start() < y:
                left = str(dics[string_left.group(0)])
                break
        for y, z in enumerate(input_txt[x][::-1]):
            if z in digits:
                right = z
                break 
            if string_right is not None and string_right.start() < y:
                right = str(dics[string_right.group(0)[::-1]])
                break
        print(x, left, right)
        if left != "" or right != "":
            addition += (int(left + right))   
    print(addition)

def main():
    input_txt = load()
    for x in range(len(input_txt)):
            input_txt[x] = input_txt[x].rstrip()
    part_one(input_txt)
    part_two(input_txt)
    

if __name__ == "__main__":
     main()