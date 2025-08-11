from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    image_url = models.URLField(max_length=500, blank=True, null=True)

    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
