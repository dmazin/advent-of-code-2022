def get_top_n_calories(calorie_list: list[str], n: int) -> list[int]:
    elf_calorie_counts: list[int] = []
    index: int = -1

    # The below code is a lot cleaner if it can assume that the very first item
    # of calorie_list is a blank string.
    if bool(calorie_list[0]):
        calorie_list.insert(0, '')

    for calorie in calorie_list:
        calorie: str = calorie.strip()

        if calorie.isdigit():
            elf_calorie_counts[index] += int(calorie)
        else:
            index += 1
            elf_calorie_counts.append(0)

    elf_calorie_counts.sort()
    return elf_calorie_counts[-n:]

with open('input.txt') as infile:
    print(sum(get_top_n_calories(infile.readlines(), 3)))
