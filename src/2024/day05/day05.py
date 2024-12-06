from functools import cmp_to_key

def load():
    with open("./src/2024/day05/input.txt", mode="r", encoding="UTF-8") as file:
         rows = file.readlines()
         return rows

def main():
    input_txt = load()
    rules = []
    updates= []
    key = cmp_to_key(lambda a, b: -1 if (a, b) in rules else 1)
    for x in range(len(input_txt)):
        input_txt[x] = input_txt[x].rstrip()
        if "|" in input_txt[x]: rules.append(tuple(map(int, input_txt[x].split("|"))))
        elif "," in input_txt[x]: updates.append(list(map(int, input_txt[x].split(","))))
    
    add1 = 0
    add2 = 0

    for update in updates:
        if sorted(update, key=key) == update:
            add1 += update[len(update) // 2]
        else:
            updated = sorted(update, key=key)
            add2 += updated[len(update) // 2]

    print(add1)
    print(add2)

if __name__ == "__main__":
     main()