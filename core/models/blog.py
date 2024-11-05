from django.db import models
from django.utils.timezone import now

class BlogTitle(models.Model):
    class Meta:
        verbose_name = "Blog title"  
        verbose_name_plural = "Blog title"

    title = models.CharField(
        verbose_name='Title',
        max_length=60,
    )

    description = models.TextField(
        verbose_name='Description',
        max_length=400,
        )

    def __str__(self):
        return 'Blog'
    
class BlogArticle(models.Model):

    title = models.CharField(
        verbose_name='Article title',
        max_length=100,
    )

    image = models.ImageField(
        verbose_name='Image',
        upload_to='uploads/article_img',
    )

    category = models.CharField(
        verbose_name='Category',
        max_length=40,
    )

    uploaded_at = models.DateTimeField(
        verbose_name='Uploaded at',
        default=now,
    )

    reading_time = models.SmallIntegerField(
        verbose_name='Aprox. reading time',
    ) 

    def __str__(self):
        return self.title