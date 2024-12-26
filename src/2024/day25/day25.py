def input_parsing():
    with open("./src/2024/day25/input.txt") as file:
        file = file.read().split('\n\n')
    return file

# Checks the height of either lock or a key, returning the heights
def process_schematics(schematics):
    keys, locks = [], []
    for schematic in schematics:
        lines = schematic.split('\n')

        columns = zip(*lines) # Fancy trick to transpose the 2d array (rows become columns)
        if lines[0] == '#####':
            keys.append([column.count('#') for column in columns])
        else:
            locks.append([column.count('#') for column in columns])

    return keys, locks

# Gets all the unique key-lock pairs
def part1(keys, locks):
    unique_pairs = 0
    for lock in locks:
        for key in keys:
            pairs = zip(key, lock)
            if all(k + l <= 7 for k, l in pairs): unique_pairs += 1

    return unique_pairs

def main():
    schematics = input_parsing()
    keys, locks = process_schematics(schematics)
    print("Part 1:", part1(keys, locks))
    print("No part 2 I guess")

if __name__ == '__main__':
    main()