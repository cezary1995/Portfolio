from django.db import models
from PIL import Image
from django.core.exceptions import ValidationError
from core.utils import ICON_CHOICES
from django.utils.timezone import now
from ckeditor.fields import RichTextField
from django.core.exceptions import ObjectDoesNotExist


class MyExpertArea(models.Model):
    name = models.CharField(
        verbose_name='Technology name',
        max_length=30,
        help_text='Technology name',
    )

    image = models.ImageField(
        verbose_name='Image',
        blank=True,
        null=True,
        upload_to='uploads/icons',
        default='',
    )

    def clean(self):
        super().clean()
        if MyExpertArea.objects.count() >= 6:
            raise ValidationError("You cannot create more than 6 objects.")

    def save(self):
        self.clean()
        super().save()

    def __str__(self):
        return self.name 
    

class WorkExperience(models.Model):

    class Meta:
        ordering = ['start_year'] # Sortowanie obiektów (w panelu admina i na stronie) w kolejności chronoligcznej

    start_year = models.PositiveSmallIntegerField(
        verbose_name = 'Start year',
    )

    end_year = models.PositiveSmallIntegerField(
        verbose_name = 'End year',
    )

    company =  models.CharField(
        max_length=30,
        help_text='The company where I worked',
    )

    position =  models.CharField(
        verbose_name='Position',
        max_length=30, 
        help_text='The position I worked at',
    )

    img_link = models.CharField(
        verbose_name='IMG_link',
        max_length=80,
    )

    job_description = RichTextField(
        verbose_name='Job description',
        max_length=400,
        null=True,
        blank=True,
    )


    def clean(self):
        super().clean()
        if self.start_year > self.end_year:
            raise ValidationError("The start year must be less than or equal to the end year.")

    def __str__(self):
        return f"{self.start_year} - {self.end_year} | {self.company} - {self. position}"
    

class ProfilePicture(models.Model):

    title = models.CharField(
        verbose_name='Title',
        max_length=100,
        blank=True, 
        null=True,   
    )

    image = models.ImageField(
        verbose_name='Image',
        upload_to='uploads/profile_pictures',
        # default='default_img.jpg',
    )
    
    uploaded_at = models.DateTimeField(
        verbose_name='Uploaded at',
        # auto_now_add=True,
        default=now,
    )

    display = models.BooleanField(
        verbose_name='Display',
        default=False,
    )

    def clean(self):
        super().clean()  # Call the base class clean() method

        # Overload the clean method with own validation
        img = Image.open(self.image)
        if img.height < 50 or img.width < 50:
            raise ValidationError("Image is too small.")

    def save(self, *args, **kwargs):

        # Save the imge in db
        super().save(*args, **kwargs)

        # Image is available to modify after saving
        img = Image.open(self.image.path)

        # Resize image if its too big
        if img.height > 250 or img.width > 180:
            output_size = (180, 250)
            img.thumbnail(output_size, Image.LANCZOS)
            img.save(self.image.path)  # Finally save image after modyfications
 


class PersonalInfo(models.Model):
    class Meta:
        verbose_name = "Personal info"  
        verbose_name_plural = "Personal info"

    name = models.CharField(
        verbose_name='Name',
        max_length=40,
        default='',   
    )

    short_desc = RichTextField(
        verbose_name='Short description',
        default='',
    )   

    def __str__(self):
        return "Personal inforamtions"


class SocialMedia(models.Model):
    name = models.CharField(
        verbose_name='Social Media Name',
        max_length=30,
        choices=ICON_CHOICES,
    )

    url = models.URLField(
        verbose_name='URL'
    )

    personal_info = models.ForeignKey(
        PersonalInfo, 
        on_delete=models.CASCADE,
        related_name='social_media',
        null=True,
        blank=True,
    )


    @classmethod
    def get_instance(cls):
        try:
            return cls.objects.get()
        except ObjectDoesNotExist:
            return cls()

    def __str__(self):
        return self.name


class OfferedService(models.Model):
    name = models.CharField(
        verbose_name='Service name',
        max_length=30,
    )

    img_link = models.CharField(
        verbose_name='Path to static file',
        max_length=100,
    )

    def __str__(self):
        return self.name
        

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
