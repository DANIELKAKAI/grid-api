from django.db import models

from main.utils import calculate_closest_points


class Grid(models.Model):
    points = models.CharField(max_length=255)
    closest_points = models.CharField(max_length=255)

    class Meta:
        db_table = 'grid'

    def save(self, *args, **kwargs):
        self.closest_points = calculate_closest_points(self.points)
        return super().save(*args, **kwargs)
