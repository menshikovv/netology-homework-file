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

def multiply_ingredients(ingredients, person_count):
    multiplied_ingredients = {}
    for ingredient in ingredients:
        name = ingredient['ingredient_name']
        quantity = ingredient['quantity'] * person_count
        measure = ingredient['measure']
        multiplied_ingredients[name] = {
            'measure': measure,
            'quantity': quantity
        }
    return multiplied_ingredients

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            multiplied_ingredients = multiply_ingredients(ingredients, person_count)

            for ingredient, data in multiplied_ingredients.items():
                if ingredient in shop_list:
                    shop_list[ingredient]['quantity'] += data['quantity']
                else:
                    shop_list[ingredient] = data

    return shop_list

def main():
    filename = 'recipes.txt'
    cook_book = read_recipes(filename)

    dishes = ['Запеченный картофель', 'Омлет']
    person_count = 2
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)

    for ingredient, data in shop_list.items():
        print(f"{ingredient}: {data['quantity']} {data['measure']}")

if __name__ == '__main__':
    main()

