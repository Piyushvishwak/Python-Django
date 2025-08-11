from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm  # we'll create this

def recipe_list(request):
    recipes = Recipe.objects.filter(is_approved=True)
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.is_approved = False  # keep unapproved until admin approves
            recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})
