import datetime
from django.db import models
from django.utils import timezone


class Schedule(models.Model):
    """スケジュール"""
    DATA = [
        ('0', 'labo'),
        ('1', 'fujii'),
        ('2', 'nishikawa'),
        ('3', 'inoue'),
        ('4', 'ito'),
        ('5', 'ma'),
        ('6', 'kondoh'),
        ('7', 'tanaka'),
        ('8', 'tukamoto'),
        ('9', 'tecd'),
    ]
    labo = models.CharField(
        max_length=100,
        choices=DATA,
        default='0',
    )
    description = models.TextField( blank=True)
    start_time = models.TimeField( default=datetime.time(9, 0, 0))
    end_time = models.TimeField(default=datetime.time(9, 0, 0))
    date = models.DateField()
    created_at = models.DateTimeField( default=timezone.now)

    def __str__(self):
        return '<Schedule:id=' + str(self.id) + ', ' + str(self.date) + ', ' + self.labo + ')>'

# Create your models here.
