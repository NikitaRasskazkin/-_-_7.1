class cookBook:

    def __init__(self):
        self.cook_book = dict()

    # Читает весь список рецептов из файла в переменную cook_book.
    def read_recipes(self):
        # Читает рецепт одного блюда и возвращает словарь вида {'название блюба' : список ингридиентов}.
        def read_dish(file_recipes):
            key = file_recipes.readline().rstrip()
            number_of_ingredients = int(file_recipes.readline().rstrip())
            value = []
            for i in range(number_of_ingredients):
                split_line = file_recipes.readline().rstrip().split(' | ')
                value.append(
                    {'ingredient_name': split_line[0],
                     'quantity': int(split_line[1]),
                     'measure': split_line[2]}
                )
            return {key: value}

        with open("files/recipes.txt", encoding="utf8") as file:
            while True:
                self.cook_book.update(read_dish(file))
                if not file.readline():
                    break

    # Выводит в консоль содержимое cook_book.
    def print(self):
        for dish, ingredients in self.cook_book.items():
            print()
            print(f"{dish}:")
            for ingredient in ingredients:
                print(f"\t{ingredient['ingredient_name']} - "
                      f"{ingredient['quantity']} {ingredient['measure']}")

    # Принимает на вход список продуктов  колличество персон,
    # возвращает словарь вида {'ингридиент': {'measure': еди. змерения, 'quantity': колличество}}.
    def get_shop_list_by_dishes(self, dishes, person_count):
        ingredients = dict()
        for dish in dishes:
            if dish in self.cook_book:
                for ingredient in self.cook_book[dish]:
                    if ingredient['ingredient_name'] not in ingredients:
                        ingredients.update({
                            ingredient['ingredient_name']: {
                                'measure': ingredient['measure'],
                                'quantity': ingredient['quantity'] * person_count
                            }
                        })
                    else:
                        ingredients[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
            else:
                print(f'Блюдо {dish} не найдено')
        return ingredients


cook_book = cookBook()
cook_book.read_recipes()
cook_book.print()
shopping_list = cook_book.get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
print('\nСписок покупок:')
for key, value in shopping_list.items():
    print(f'{key}: {value["quantity"]} {value["measure"]}')
