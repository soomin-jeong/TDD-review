from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse


class List(models.Model):
    def get_absolute_url(self):
        return reverse('lists:view-list', args=[self.id])


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=CASCADE)


