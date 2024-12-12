history = dict()

def load():
    with open("./src/2024/day11/input.txt", mode="r", encoding="UTF-8") as file:
         return file.read().strip().split()
    
def iter_stone_count(stone, iteration, history):
    # Base Cases, if last iteration, just return 1 stone
    if iteration == 0:
        return 1
    
    # Saves the time and memory of the computer by already fishing out the already calculated stone blinks. (Mostly For Part 2)
    elif (stone, iteration) in history:
        return history[(stone, iteration)]
    
    # Rule 1 (0 --> 1)
    if stone == 0:
        stone_num = iter_stone_count(1, iteration - 1, history)
    
    # Rule 2 (if stone even - split --> 10 --> 1 0)
    elif len(str(stone)) % 2 == 0:
        mid_index = len(str(stone)) // 2
        stone_num = iter_stone_count(int(str(stone)[:mid_index]), iteration - 1, history) + iter_stone_count(int(str(stone)[mid_index:]), iteration - 1, history)
    
    # Rule 3 (Else *2024)
    else:
        stone_num = iter_stone_count(stone * 2024, iteration - 1, history)

    history[(stone, iteration)] = stone_num
    return stone_num

def main():
    txt_input = list(map(int, load()))

    # Part 1 - 25 iterations
    sum_p1 = 0
    for stone in txt_input:
        sum_p1 += iter_stone_count(stone, 25, history)
    print("Part 1 -", sum_p1)
    
    # Part 2 - 75 iterations
    sum_p2 = 0
    for stone in txt_input:
        sum_p2 += iter_stone_count(stone, 75, history)
    print("Part 2 -", sum_p2)

if __name__ == "__main__":
    main()