from django.db import models

class Use(models.Model):
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    DATA = [
        ('0', 'labo'),
        ('1', 'fujii'),
        ('2', 'inoue'),
    ]
    labo = models.CharField(
        max_length=100,
        choices=DATA,
        default='0',
    )
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return '<Use:id=' + str(self.id) + ', ' + str(self.date) + ', ' + self.labo + ')>'
    
