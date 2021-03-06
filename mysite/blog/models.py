# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):  #creates a table called post
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()

    def __unicode__(self):  #str in place of unicode in python3
        return self.title
