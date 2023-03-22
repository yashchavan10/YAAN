from django.db import models
from django.contrib.auth.models import User


class PastDetail(models.Model):
    updated = models.DateTimeField(auto_now=True)
    start_address =models.CharField(max_length=256,default='')
    end_address=  models.CharField(max_length=256,default='')
