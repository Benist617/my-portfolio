from django.db import models


class ToDo(models.Model):
    #objects = models.Manager()
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)
