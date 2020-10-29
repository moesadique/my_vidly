from django.contrib import admin
from .models import Genre, Movies

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class MoviesAdmin(admin.ModelAdmin):
        list_display = ('title', 'rent', 'stock', 'genre')
# Register your models here.

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movies, MoviesAdmin)