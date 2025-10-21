from django.contrib import admin
from .models import Genre, Tag, Movie, Comment

admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(Movie)
admin.site.register(Comment)
