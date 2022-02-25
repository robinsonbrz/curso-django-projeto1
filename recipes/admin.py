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
    list_display = ['id', 'title', 'created_at', 'is_published', 'author']
    list_display_links = 'title', 'created_at',
    search_fields = 'id', 'title', 'description', 'slug', 'preparation_steps',
    list_filter = 'category', 'author', 'is_published', \
        'preparation_steps_is_html',
    list_per_page = 10
    list_editable = 'is_published',
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('title',)
    }


# pode-se registrar com decorator:
# @admin.register()
admin.site.register(Category, CategoryAdmin)
