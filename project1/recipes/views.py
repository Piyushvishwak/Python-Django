from django.shortcuts import render

def recipe_list(request):
    recipes = [
        {"id": 1, "title": "Pasta", "description": "Delicious creamy pasta", "image": "https://img.freepik.com/free-photo/penne-pasta-tomato-sauce-with-chicken-tomatoes-wooden-table_2829-19739.jpg"},
        {"id": 2, "title": "Salad", "description": "Fresh vegetable salad", "image": "https://images.pexels.com/photos/1059905/pexels-photo-1059905.jpeg?cs=srgb&dl=pexels-chanwalrus-1059905.jpg&fm=jpg"},
    ]
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, id):
    recipes = [
        {
            "id": 1,
            "title": "Pasta",
            "description": "Delicious creamy pasta",
            "ingredients": "Pasta, Cream, Cheese",
            "instructions": "Boil pasta and mix with cream.",
            "image": "https://img.freepik.com/free-photo/penne-pasta-tomato-sauce-with-chicken-tomatoes-wooden-table_2829-19739.jpg"
        },
        {
            "id": 2,
            "title": "Salad",
            "description": "Fresh vegetable salad",
            "ingredients": "Lettuce, Tomato, Cucumber",
            "instructions": "Mix all veggies and serve.",
            "image": "https://images.pexels.com/photos/1059905/pexels-photo-1059905.jpeg?cs=srgb&dl=pexels-chanwalrus-1059905.jpg&fm=jpg"
        },
    ]

    recipe = None
    for item in recipes:
        if item["id"] == id:
            recipe = item
            break
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

