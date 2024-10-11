from django.db import models

class BlogTitle(models.Model):
    header_title = models.CharField(
        verbose_name='Header title',
        max_length=60,
    )

    title_description = models.TextField(
        verbose_name='Header title',
        max_length=400,
        )

    def __str__(self):
        return 'Blog title'