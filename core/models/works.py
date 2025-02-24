from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language
from django.utils.translation import activate
# from ckeditor.fields import RichTextField


class WorksTitle(models.Model):
    class Meta:
        verbose_name = "Works - title"  
        verbose_name_plural = "Works - title"

    desc = models.TextField(
        verbose_name='Description',
        max_length=1200,
        null=True
    )


class Project(models.Model):
    name = models.CharField(
        verbose_name='Project name',
        max_length=30,
    )

    image = models.ImageField(
        verbose_name='Image',
        blank=True,
        null=True,
        upload_to='uploads/projects',
        default='',
    )

    link = models.CharField(
        verbose_name='link to project',
        max_length=80, 
        default='link_to_project',
        blank=True,
        null=True,
    ) 

    proj_desc = models.TextField(
        verbose_name='Project description',
        max_length=3000,
        null=True,
        blank=True,
    )
    
    slug = models.SlugField(
        verbose_name='URL',
        unique=True
    )

    def clean(self):
        super().clean()

        img = Image.open(self.image)
        if img.height < 50 or img.width < 50:
            raise ValidationError("Image is too small.")
        
    def get_translated_slug(self):
        lang = get_language()
        translated_slug = getattr(self, f'slug_{lang}', self.slug)
        print(f'Language: {lang}, Slug: {translated_slug}')
        return translated_slug
        
    def get_absolute_url(self):
        lang = get_language()
        translated_slug = getattr(self, f'slug_{lang}', self.slug)
        return reverse('project_details', kwargs={'slug': translated_slug})

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        
        if img.height > 900 or img.width > 1300:
            output_size = (900, 1300)
            img.thumbnail(output_size, Image.LANCZOS)
            img.save(self.image.path)
    
    def __str__(self):
        return self.name

        