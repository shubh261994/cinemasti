from django.contrib import admin
from .models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'genre','release_date']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['release_date']
admin.site.register(Movie,  MovieAdmin)