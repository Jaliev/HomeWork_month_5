from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name="Введите имя режиссёра")
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Режиссёр'
        verbose_name_plural = 'Режиссёры'


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name="Введите название фильма")
    description = models.TextField(verbose_name="Укажите описание")
    duration = models.CharField(max_length=50, verbose_name="Продолжительность фильма")
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='directors_list', verbose_name='Выберите режиссёра')

    def __str__(self):
        return f'{self.title} - {self.duration}'

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

class Review(models.Model):
    rate_stars = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    text = models.TextField(max_length=1500, verbose_name='Отзыв о фильме')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movies_list', verbose_name='Выберите фильм')
    stars = models.CharField(max_length=5, choices=rate_stars, verbose_name='Укажите рейтинг', null=True)
    def __str__(self):
        return f'{self.text} - {self.stars}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'