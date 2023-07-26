def read_recipes(filename):
    cook_book = {}
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        name = lines[i].strip()
        i += 1

        if i >= len(lines):
            break

        ingredient_count_str = lines[i].strip()
        if not ingredient_count_str.isdigit():
            continue

        ingredient_count = int(ingredient_count_str)
        ingredients = []

        for j in range(ingredient_count):
            ingredient_info = lines[i + 1 + j].strip().split('|')
            ingredient = {
                'ingredient_name': ingredient_info[0].strip(),
                'quantity': int(ingredient_info[1].strip()),
                'measure': ingredient_info[2].strip()
            }
            ingredients.append(ingredient)

        cook_book[name] = ingredients
        i += ingredient_count + 1

    return cook_book

def main():
    filename = "recipes.txt"
    cook_book = read_recipes(filename)

    for dish, ingredients in cook_book.items():
        print(f'{dish}:')
        for ingredient in ingredients:
            print(f"  {ingredient['ingredient_name']} - {ingredient['quantity']} {ingredient['measure']}")

if __name__ == '__main__':
    main()
