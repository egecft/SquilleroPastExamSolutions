INPUT_FILE_FOODS = "foods.txt"
INPUT_FILE_RECIPE = "fusilli_alle_olive.txt"
# INPUT_FILE_RECIPE = "polenta_concia.txt"


def read_foods():
    food_dict = dict()
    try:
        with open(INPUT_FILE_FOODS, "r") as input_file:
            for line in input_file:
                clean_line = line.strip()
                splitted_line = clean_line.split("; ")
                food_dict[splitted_line[0]] = splitted_line[1], splitted_line[2]
    except OSError as problem:
        exit(f"We have a problem: {problem}")
    return food_dict


def read_recipe():
    recipe_dict = dict()
    try:
        with open(INPUT_FILE_RECIPE, "r") as input_file:
            for line in input_file:
                clean_line = line.strip()
                if clean_line == "Ingredients:":
                    continue
                elif clean_line == "":
                    break
                splitted_line = clean_line.split("; ")
                recipe_dict[splitted_line[0]] = splitted_line[1]
    except OSError as problem:
        exit(f"We have a problem: {problem}")
    return recipe_dict


def create_output():
    food_dict = read_foods()
    recipe_dict = read_recipe()
    ingredient_number = len(recipe_dict.keys())
    recipe_cost = 0
    recipe_calories = 0

    try:
        for name in recipe_dict.keys():
            recipe_cost += (float(food_dict[name][0]) / 1000) * int(recipe_dict[name])
            recipe_calories += (float(food_dict[name][1]) / 1000) * int(recipe_dict[name])
    except ValueError as problem:
        exit(f"We have a problem: {problem}")

    print("Ingredients:")
    for name, quantity in recipe_dict.items():
        print(f"{name} - {quantity}")
    print("")
    print(f"Number of ingredients: {ingredient_number}")
    print(f"Recipe cost: {recipe_cost:.2f}")
    print(f"Recipe calories: {recipe_calories:.2f}")


def main():
    read_foods()
    read_recipe()
    create_output()


if __name__ == "__main__":
    main()
