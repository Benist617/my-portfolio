from django.db import models


class Project(models.Model):
    objects = models.Manager()
    Image = models.ImageField(upload_to='images/')
    Summary = models.CharField(max_length=200)

    def __str__(self):
        return self.Summary
