def load():
    with open("./src/day01/input.txt", mode="r", encoding="UTF-8") as file:
         rows = file.readlines()
         
         return rows

def find_smallest(list_int):
    min_value = max(list_int)
    min_index = 0
    for x in range(len(list_int)):
        if min_value > list_int[x]:
            min_value = list_int[x]
            min_index = x

    return min_value, min_index
            
def part_one(list1, list2):
    distance = 0
    while len(list1) != 0:
        first = find_smallest(list1)
        second = find_smallest(list2)
        distance += (abs(first[0] - second[0]))
        del list1[first[1]]
        del list2[second[1]]
    print(distance)

def part_two(list1, list2):
    distance = 0
    for x in list1:
        amount = 0
        for y in list2:
            if x == y:
                amount += 1
        distance += (x * amount)
    print(distance)

def main():
    input_txt = load()
    list1 = []
    list2 = []
    for x in range(len(input_txt)):
            input_txt[x] = input_txt[x].rstrip().split()
            list1.append(int(input_txt[x][0]))
            list2.append(int(input_txt[x][1]))
    part_two(list1, list2)
    part_one(list1, list2)
    

if __name__ == "__main__":
     main()