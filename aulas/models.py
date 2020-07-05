# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Aulas(models.Model):

    nome = models.CharField(verbose_name="Nome", max_length=254)
    url = models.CharField(verbose_name="URL", max_length=512)
    img = models.CharField(verbose_name="URL image", max_length=512)