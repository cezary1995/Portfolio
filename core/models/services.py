from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class ServicesTitle(models.Model):
    class Meta:
        verbose_name = "Service title"  
        verbose_name_plural = "Service title"

    title = models.CharField(
        verbose_name='Title',
        max_length=60,
    )

    description = CKEditor5Field(
        verbose_name='Description',
        max_length=1200
    )


class Service(models.Model):
    name = models.CharField(
        verbose_name='Service name',
        max_length=30,
    )

    image = models.FileField(
        verbose_name='SVG file',
        upload_to='uploads/svgs',
        blank=True,
        null=True,
        default=''
    )

    def __str__(self):
        return self.name
        

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
    