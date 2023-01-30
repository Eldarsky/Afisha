from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=20)

    @property
    def count(self):
        movies_count = self.movies_count.count()
        return movies_count


class Movie(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    duration = models.CharField(max_length=15)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movies_count')

    def __str__(self):
        return self.title

    @property
    def rating(self):
        count = self.movie_reviews.count()
        if count == 0:
            return 0
        total = 0
        for i in self.movie_reviews.all():
            total += i.stars
        return total / count


CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(choices=CHOICES, default=0)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, related_name='movie_reviews')

    def __str__(self):
        return self.text