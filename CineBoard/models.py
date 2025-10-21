from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.FloatField(default=0)
    tags = models.ManyToManyField('Tag', blank=True)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)  # 🖼️ вот это новое поле!
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.genre})"


class Comment(models.Model):  # ⭐ доп. задание
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Комментарий от {self.author} к {self.movie}'
