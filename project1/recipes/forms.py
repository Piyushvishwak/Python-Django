from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'image_url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter recipe title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Short description'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'List ingredients'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Cooking steps'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Paste image URL here'}),
        }
