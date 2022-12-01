def get_max_calories(calorie_list: list[str]) -> int:
    biggest_elf_calories: int = 0
    current_elf_calories: int = 0

    for calorie in calorie_list:
        calorie: str = calorie.strip()

        if calorie.isdigit():
            current_elf_calories += int(calorie)
        else:
            current_elf_calories = 0

        biggest_elf_calories = max(biggest_elf_calories, current_elf_calories)

    return biggest_elf_calories

with open('input.txt') as infile:
    print(get_max_calories(infile.readlines()))
