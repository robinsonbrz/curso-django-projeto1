from django.contrib import admin

from .models import Category, Recipe

# Register your models here.


# Register your models here.
# Registrando aqui é disponibilizado na area administrativa do Django
class CategoryAdmin(admin.ModelAdmin):
    ...


# Registrando com decorator
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...


# pode-se registrar com decorator:
# @admin.register()
admin.site.register(Category, CategoryAdmin)
