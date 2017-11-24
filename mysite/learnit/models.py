

# Create your models here.

from django.db import models

class Subs(models.Model):
    tech=models.CharField(max_length = 30)
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()

    def __unicode__(self):
        return self.tech




