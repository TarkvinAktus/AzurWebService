from django.db import models
from datetime import datetime

class StatisticsUrl(models.Model):
    date_time = models.DateTimeField(blank=True, null=True)
    key_name = models.CharField(max_length=30)
    url = models.CharField(max_length=200)
    url_domain = models.CharField(max_length=30)
    status_code = models.IntegerField(default = 0)
    byte_size = models.IntegerField(default = 0)
    load_time = models.IntegerField(default = 0)

    def __str__(self):
        return self.key_name + " " + self.url_domain

