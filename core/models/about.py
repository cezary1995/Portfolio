from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now
from core.utils import RATES

class AboutMe(models.Model):
    class Meta:
        verbose_name = "About me"  
        verbose_name_plural = "About me"

    name = models.CharField(
        verbose_name='Name',
        max_length=60,
    )

    content = RichTextField(
        verbose_name='Informations about',
        max_length=1000,
        )

    def __str__(self):
        return 'About me'
    

class Review(models.Model):
    content = models.TextField(
        verbose_name='Review content',
        max_length=3000,
    )

    rate = models.IntegerField(
        verbose_name='Rate',
        choices=RATES,
    )

    reviewer = models.CharField(
        verbose_name='Reviewer name',
        max_length=50,
    )

    uploaded_at = models.DateTimeField(
        verbose_name='Uploaded at',
        # auto_now_add=True,
        default=now,
    )

    def truncated_content(self):
        if len(self.content) > 200:
            return self.content[:200] + '...'
        return self.content
