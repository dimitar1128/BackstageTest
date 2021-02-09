from django.db import models

class TBLServiceLog(models.Model):
    number = models.IntegerField()
    value = models.IntegerField()
    occurrences = models.IntegerField(default=0)