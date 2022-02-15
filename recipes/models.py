from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# Classes devem herdar models.Model
class Category(models.Model):
    name = models.CharField(max_length=65)

    # Essa função modifica a visualização em Djanngo Admin exibindo
    # o conteudo em name
    # Ao inves de Object 1, object 2
    def __str__(self):
        exibir = f"{ self.name}"
        return exibir

# Criada a tabela Recipe e


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField(unique=True)
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_units = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None,  # noqa E501
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        exibir = f"{ self.title}"
        return exibir
