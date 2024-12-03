import copy

from django.shortcuts import render

# Create your views here.
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
}

def recipe_view(request, recipe):
    servings = request.GET.get('servings')
    recipe_data = {}

    if servings is None:
        recipe_data = copy.copy(DATA[recipe])
    else:
        for ingridient, count in DATA[recipe].items():
            recipe_data[ingridient] = count * int(servings)

    context = {
      'recipe': recipe_data
    }

    return render(request, 'index.html', context)
