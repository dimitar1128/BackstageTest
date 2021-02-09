from django.db import models
import datetime

class TBLServiceLog(models.Model):
    number = models.IntegerField()
    value = models.IntegerField()
    time = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.time = datetime.datetime.now()
        super().save(*args, **kwargs)