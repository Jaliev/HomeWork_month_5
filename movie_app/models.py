from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name="Введите имя режиссёра")

    def __str__(self):
        return f'{self.name}'


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name="Введите название фильма")
    description = models.TextField(verbose_name="Укажите описание")
    duration = models.CharField(max_length=50, verbose_name="Продолжительность фильма")
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='directors_list', verbose_name='Выберите режиссёра')

    def __str__(self):
        return f'{self.title} - {self.duration}'

class Review(models.Model):
    text = models.TextField(max_length=1500, verbose_name="Отзыв о фильме")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movies_list', verbose_name='Выберите фильм')

    def __str__(self):
        return f'{self.text}'