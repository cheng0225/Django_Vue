from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Things(models.Model):
    name=models.CharField(max_length=25)
    price=models.SmallIntegerField(max_length=25,default=25)

    def __unicode__(self):
        return self.name

