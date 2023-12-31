from django.core.paginator import Paginator
from django.shortcuts import render


DATA = {
        'omlet': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        },
        'pasta': {
            'макароны, г': 0.3,
            'сыр, г': 0.05,
        },
        'buter': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        },
        # можете добавить свои рецепты ;)
    }

def recipes(request):
    templates_name = 'calculator/main.html'
    context = {
        'recipe_name': DATA.keys()
               }
    return render(request, templates_name, context)

def recipe_view(request, meal_name):
    templates_name = 'calculator/index.html'
    servings = int(request.GET.get('servings', 1))
    recipe = {}
    for meal, quantity in DATA[meal_name].items():
        recipe[meal] = quantity * servings

    context = {
        'recipe' : recipe
    }
    return render(request, templates_name, context)



# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }