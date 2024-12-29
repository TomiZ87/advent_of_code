def load():
    with open("./src/2015/day01/input.txt", mode="r", encoding="UTF-8") as file:
        rows = file.read()         
        return rows.strip()
    
def main():
    position = 0
    current_floor = 0
    is_zero = False
    for x in load():
        if x == "(": current_floor += 1
        elif x == ")": current_floor -= 1

        if not is_zero:
            position += 1
            if current_floor < 0: is_zero = True
    
    print("Part 1", current_floor)
    print("Part 2", position)
    
if __name__ == "__main__":
    main()