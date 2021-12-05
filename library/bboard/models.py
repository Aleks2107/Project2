from django.db import models
from django.forms import DateInput
from datetime import datetime


class Bb(models.Model):
    title = models.CharField(max_length=50)
    auther = models.CharField(max_length=50)
    genre = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=50)
    data = models.CharField(max_length=50)
    give_out = models.CharField(max_length=50)
    give_in = models.DateTimeField(auto_now_add=True, db_index=True)