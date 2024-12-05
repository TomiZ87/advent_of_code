def load():
    with open("./src/2024/day02/input.txt", mode="r", encoding="UTF-8") as file:
         rows = file.readlines()
         return rows
    
def part_one(int_list):
    break_b = True
    order = 0
    diff = []
    for x in range(len(int_list) - 1):
        diff.append(int(int_list[x]) - int(int_list[x + 1]))

    if diff[0] > 0: order = 1
    elif diff[0] < 0: order = 2
    else: break_b = False

    if break_b:
        for y in diff:
            if order == 1 and 0 < y < 4:
                break_b = True
            elif order == 2 and -4 < y < 0:
                break_b = True
            else: 
                break_b = False
                break

    return break_b

def main():
    input_txt = load()
    for x in range(len(input_txt)):
        input_txt[x] = input_txt[x].rstrip().split()
    sum_part_one = sum([part_one(row) for row in input_txt])
    sum_part_two = sum([any([part_one(row[:x] + row[x + 1:]) for x in range(len(row))]) for row in input_txt])
    print(sum_part_one)
    print(sum_part_two)

if __name__ == "__main__":
     main()