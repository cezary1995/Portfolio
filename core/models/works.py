from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

class WorksTitle(models.Model):
    class Meta:
        verbose_name = "Works - title"  
        verbose_name_plural = "Works - title"

    title = models.CharField(
        verbose_name='Title',
        max_length=60,
    )

    description = CKEditor5Field(
        verbose_name='Description',
        max_length=1200
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

    description = CKEditor5Field(
        verbose_name='Project description',
        max_length=3000,
        null=True,
        blank=True,
    )
    
    slug = models.SlugField(
        verbose_name='URL',
    )

    def clean(self):
        super().clean()

        img = Image.open(self.image)
        if img.height < 50 or img.width < 50:
            raise ValidationError("Image is too small.")
        
    def get_absolute_url(self):
        # Wygeneruje URL na podstawie nazwy widoku 'article' i argumentu slug
        return reverse('project_details', kwargs={'slug': self.slug, 'project_id': self.id})
    
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

        