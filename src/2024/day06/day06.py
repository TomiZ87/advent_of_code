directon = {"^" : (-1, 0), ">" : (0, 1), "v" : (1, 0), "<" : (0, -1)}

class InfLoop(Exception):
    """Error Infinite Loop"""

def load():
    with open("./src/2024/day06/input.txt", mode="r", encoding="UTF-8") as file:
         rows = file.read().split("\n")
         return rows

def find_position(input_txt):
    for x in range(len(input_txt)):
        for y in range(len(input_txt[x])):
            if input_txt[x][y] == "^":
                return x, y

def rotate(char):
    rotations = ["^", ">", "v", "<"]
    if char == "^": return ">"
    elif char == ">": return "v"
    elif char == "v": return "<"
    elif char == "<": return "^"


def part_one(input_txt, MODE = "pt1"):
    visited = set()
    y, x = find_position(input_txt)
    current = input_txt[y][x]
    try:
        while (0 <= y < (len(input_txt) - 1)) and (0 < x <= len(input_txt[y]) - 1):
            if input_txt[y + directon[current][0]][x + directon[current][1]] == "#":
                current = rotate(current)
            else:
                input_txt[y + directon[current][0]][x + directon[current][1]] = current
                input_txt[y][x] = "X"

                y = y + directon[current][0]
                x = x + directon[current][1]

                if y == 0 or x == 0 or y == len(input_txt) or x == len(input_txt[y]):
                    input_txt[y][x] = "X"
                
                visit = (y, x, directon[current])
                if visit in visited and MODE == "pt2": 
                    raise InfLoop
                visited.add(visit)

            #draw(input_txt)
    except InfLoop:
        return 1
    
    except Exception as f: 
        print(f, y, x, directon[current])

    if MODE == "pt1":
        draw(input_txt)

        counter = 0
        for i in input_txt:
            for j in i:
                if j == "X": counter += 1
        print("Total X's :", counter)
        return visited
    
    return 0

def part_two(visited):
    loops = 0
    possible_loops = set()
    for x in visited:
        possible_loops.add(x[0:2])
    
    for possiblity in possible_loops:
        input_txt = load()
        for x in range(len(input_txt)):
            input_txt[x] = list(input_txt[x])

        input_txt[possiblity[0]][possiblity[1]] = "#"
        loops += part_one(input_txt, "pt2")
    print("Total Infinite Loops", loops)

def draw(input_txt):
    printing = ""
    for x in input_txt:
        
        for y in x:
            if y == "X":
                printing += "\033[31m" + y
            elif y in ["^", ">", "v", "<"]:
                printing += "\033[92m" + y
            else:
                printing += "\033[0m" + y
        printing += "\n"

    print(printing + "\n")

def main():
    input_txt = load()
    for x in range(len(input_txt)):
        input_txt[x] = list(input_txt[x])
    
    visited = part_one(input_txt)
    part_two(visited)

if __name__ == "__main__":
     main()
