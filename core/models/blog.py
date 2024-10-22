from django.db import models

class BlogTitle(models.Model):
    class Meta:
        verbose_name = "Blog title"  
        verbose_name_plural = "Blog title"

    title = models.CharField(
        verbose_name='Header title',
        max_length=60,
    )

    description = models.TextField(
        verbose_name='Header title',
        max_length=400,
        )

    def __str__(self):
        return 'Blog title'