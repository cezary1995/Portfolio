from django.db import models
from django.utils.timezone import now
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


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

    slug = models.SlugField(
        verbose_name='URL',
    )

    image = models.ImageField(
        verbose_name='Image',
        upload_to='uploads/article_img',
    )

    category = models.CharField(
        verbose_name='Category',
        max_length=40,
    )

    content = CKEditor5Field(
        verbose_name='Article content',
        null=True,
        blank=True,
    )

    uploaded_at = models.DateTimeField(
        verbose_name='Uploaded at',
        default=now,
    )

    reading_time = models.SmallIntegerField(
        verbose_name='Aprox. reading time',
    ) 

    def get_absolute_url(self):
        # Wygeneruje URL na podstawie nazwy widoku 'article' i argumentu slug
        return reverse('article', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class BlogComment(models.Model):

    name = models.CharField(
        verbose_name='Name',
        max_length=50,
    )

    email = models.EmailField(
        verbose_name='Email',
        max_length=50,
    )

    message = models.TextField(
        verbose_name='Comment',
        max_length=2000,

    )

    uploaded_at = models.DateTimeField(
        verbose_name='Uploaded at',
        auto_now_add=True
    )
