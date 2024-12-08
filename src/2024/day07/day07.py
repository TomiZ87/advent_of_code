def load():
    with open("./src/2024/day07/input.txt", mode="r", encoding="UTF-8") as file:
         rows = file.read().split("\n")
         return rows

def sum_if_target_calc(input_txt, add_concat = False):
    sum_id = 0
    
    if add_concat: operators = [lambda x, y: int(x) + int(y), lambda x, y: int(x) * int(y), lambda x, y: int(str(x)+str(y))]
    else: operators = [lambda x, y: int(x) + int(y), lambda x, y: int(x) * int(y)]

    for id, values in input_txt:
        possible_equations = caulculation(values[0], values[1:], operators)

        if id in possible_equations:
            sum_id += id
            print("Calibrated Successfully", id)
            continue

    print("Calibration Failed", id)
    return sum_id

def caulculation(first, other, operators):
    results = []
    if len(other) == 0:
        results.append(first)
        return results
    
    for operation in operators:
        results.append(caulculation(operation(first, other[0]), other[1:], operators))

    return sum(results, [])

def main():
    input_txt = load()
    for x in range(len(input_txt)):
        input_txt[x] = input_txt[x].split(": ")
        input_txt[x][0] = int(input_txt[x][0])
        input_txt[x][1] =  input_txt[x][1].split()

    print("Pt.1")
    pt1 = sum_if_target_calc(input_txt)

    print("Pt.2")
    pt2 = sum_if_target_calc(input_txt, True)

    print("Pt.1", pt1)
    print("Pt.2", pt2)

if __name__ == "__main__":
    main()
