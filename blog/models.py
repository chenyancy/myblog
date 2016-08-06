#! -*- encoding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        app_label = 'blog'
        verbose_name = u'文章'
        verbose_name_plural = u'文章'
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField(default='default_text')
    #markdown_text = models.TextField()
    #markdown_pretext = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Category)
    is_markdown = models.BooleanField(default=False)
    markdown_text = models.TextField(default='default_text')
    tinymce_text = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
