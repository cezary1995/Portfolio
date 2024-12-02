from django.db import models
from django.utils.timezone import now
from django_ckeditor_5.fields import CKEditor5Field


class ContactTitle(models.Model):
    class Meta:
        verbose_name = "Contact - title"  
        verbose_name_plural = "Contact - title"

    title = models.CharField(
        verbose_name='Title',
        max_length=60,
    )

    description = CKEditor5Field(
        verbose_name='Description',
        max_length=1200
    )


class UserMessage(models.Model):
    class Meta:
        verbose_name_plural = "MESSAGES"  

    name = models.CharField(
        verbose_name='Name',
        max_length=50,
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=50,
    )

    phone = models.IntegerField(
        verbose_name='Phone number',
        blank=True,
        null=True
    )

    subject = models.CharField(
        verbose_name='Subject',
        max_length=100,
    )

    message = models.TextField(
        verbose_name='Content message',
    )

    uploaded_at = models.DateTimeField(
        verbose_name='Created at',
        default=now,
    )

    def __str__(self):
        return f'Sender: {self.email}'