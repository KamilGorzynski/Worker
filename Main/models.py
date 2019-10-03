from django.db import models
from django.utils.timezone import now


class UrlObject(models.Model):
    url = models.TextField()
    interval = models.IntegerField()


class RequestHistory(models.Model):
    url_object = models.ForeignKey(UrlObject, on_delete=models.CASCADE, blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    duration = models.DecimalField(max_digits=19, decimal_places=9, blank=True, null=True)
    created_at = models.DateTimeField(default=now(), blank=True, null=True)
