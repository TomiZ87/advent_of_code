import re
def load():
    with open("./src/2024/day04/input.txt", mode="r", encoding="UTF-8") as file:
         txt = file.readlines()
         return txt
    
def part_one(input_txt):
    counter = 0
    for x in range(len(input_txt)):
        for y in range(len(input_txt[x]) - 3):
            if input_txt[x][y + 3] == "X" and input_txt[x][y + 2] == "M" and input_txt[x][y + 1] == "A" and input_txt[x][y] == "S":
                    counter += 1
            if input_txt[x][y + 3] == "S" and input_txt[x][y + 2] == "A" and input_txt[x][y + 1] == "M" and input_txt[x][y] == "X":
                    counter += 1
    for x in range(len(input_txt) - 3):
        for y in range(len(input_txt[x])):
            if input_txt[x][y] == "X" and input_txt[x + 1][y] == "M" and input_txt[x + 2][y] == "A" and input_txt[x + 3][y] == "S":
                counter += 1
            if input_txt[x][y] == "S" and input_txt[x + 1][y] == "A" and input_txt[x + 2][y] == "M" and input_txt[x + 3][y] == "X":
                counter += 1
        for y in range(len(input_txt[x]) - 3):
            if input_txt[x][y] == "X" and input_txt[x + 1][y + 1] == "M" and input_txt[x + 2][y + 2] == "A" and input_txt[x + 3][y + 3] == "S":
                counter += 1
            if input_txt[x][y] == "S" and input_txt[x + 1][y + 1] == "A" and input_txt[x + 2][y + 2] == "M" and input_txt[x + 3][y + 3] == "X":
                counter += 1
            
            if input_txt[x][y + 3] == "X" and input_txt[x + 1][y + 2] == "M" and input_txt[x + 2][y + 1] == "A" and input_txt[x + 3][y] == "S":
                counter += 1
            if input_txt[x][y + 3] == "S" and input_txt[x + 1][y + 2] == "A" and input_txt[x + 2][y + 1] == "M" and input_txt[x + 3][y] == "X":
                counter += 1
    print(counter)

def part_two(input_txt):
    counter = 0
    for x in range(len(input_txt) - 2):
        for y in range(len(input_txt[x]) - 2):
            if input_txt[x + 1][y + 1] == "A" and (((input_txt[x][y] == "M" and input_txt[x + 2][y + 2] == "S") or (input_txt[x][y] == "S" and input_txt[x + 2][y + 2] == "M")) and ((input_txt[x][y + 2] == "M" and input_txt[x + 2][y] == "S") or (input_txt[x][y + 2] == "S" and input_txt[x + 2][y] == "M"))):
                counter += 1
    print(counter)

def main():
    input_txt = load()
    for x in range(len(input_txt)):
            input_txt[x] = input_txt[x].rstrip()

    part_one(input_txt)
    part_two(input_txt)

if __name__ == "__main__":
     main()
