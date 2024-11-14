from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
from ckeditor.fields import RichTextField

class WorksTitle(models.Model):
    class Meta:
        verbose_name = "Works - title"  
        verbose_name_plural = "Works - title"

    title = models.CharField(
        verbose_name='Title',
        max_length=60,
    )

    description = RichTextField(
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

    description = models.CharField(
        verbose_name='Project description',
        max_length=300, 
        default='project desc',
        blank=True,
        null=True,
    )

    category = models.CharField(
        verbose_name='Project category',
        max_length=40, 
        default='<category>',
        blank=True,
        null=True,
    )

    def clean(self):
        super().clean()

        img = Image.open(self.image)
        if img.height < 50 or img.width < 50:
            raise ValidationError("Image is too small.")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 900 or img.width > 1300:
            output_size = (900, 1300)
            img.thumbnail(output_size, Image.LANCZOS)
            img.save(self.image.path)