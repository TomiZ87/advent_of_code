def load():
    with open("./src/2024/day10/input.txt", mode="r", encoding="UTF-8") as file:
         rows = file.read().split("\n")
         return rows

def search_for_trails(x, y, current, visited, input_txt, row_len, column_len):
    # Base Steps
    if current == 9:
        if (x, y) in visited:
            visited[(x, y)] += 1
            return 0
        else:
            visited[(x, y)] = 1
            return 1
    
    # Recursive Step
    num_trails = 0
    directions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for next_row, next_column in directions:
        if -1 < next_row < row_len and -1 < next_column < column_len:
            if input_txt[next_row][next_column] == current + 1:
                num_trails += search_for_trails(next_row, next_column, (current + 1), visited, input_txt, row_len, column_len)

    return num_trails

def main():
    input_txt = load()
    for x in range(len(input_txt)):
        input_txt[x] = list(map(int, input_txt[x]))

    pt1 = 0
    pt2 = 0

    for x in range(len(input_txt)):
        for y in range(len(input_txt[x])):
            if input_txt[x][y] == 0:
                visited = dict()
                pt1 += search_for_trails(x, y, input_txt[x][y], visited, input_txt, len(input_txt), len(input_txt[x]))
                
                for z in visited: pt2 += visited[z]

    print("Pt.1:", pt1)
    print("Pt.2:", pt2)

if __name__ == "__main__":
    main()
