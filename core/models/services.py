from django.db import models
from ckeditor.fields import RichTextField

class ServicesTitle(models.Model):
    class Meta:
        verbose_name = "Service title"  
        verbose_name_plural = "Service title"

    title = models.CharField(
        verbose_name='Title',
        max_length=60,
    )

    description = RichTextField(
        verbose_name='Description',
        max_length=1200
    )

class AskedQuestion(models.Model):
    question = models.CharField(
        verbose_name='Asked question',
        max_length=120,
    )

    response = models.TextField(
        verbose_name='Response',
        max_length=500,
        )

    def __str__(self):
        return 'question'