from django.db import models


class Tasks(models.Model):
    name = models.CharField(max_length=128)
    done = models.BooleanField(default=False)
