from django.db import models
from django.utils.timezone import now
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from core.utils import CATEGORIES


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
        max_length=1000,
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
        max_length=50,
        choices=CATEGORIES,
        blank=True,
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

    def get_categories_display(self):
        return dict(CATEGORIES).get(self.category, self.category)
    
    # It changes column name in admin app 'get_categories_display' -> 'category'
    get_categories_display.short_description = "category"

    def get_absolute_url(self):
        # Wygeneruje URL na podstawie nazwy widoku 'article' i argumentu slug
        return reverse('article', kwargs={'slug': self.slug, 'article_id': self.id})
    
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

    article = models.ForeignKey(
        BlogArticle,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.article.title}: {self.message[:50]}"
