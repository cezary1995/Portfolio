from django.db import models
from PIL import Image, ExifTags
from django.core.exceptions import ValidationError
from core.utils import ICON_CHOICES, VIEWS
from django.utils.timezone import now
from django.core.exceptions import ObjectDoesNotExist
from django_ckeditor_5.fields import CKEditor5Field


class PersonalInfo(models.Model):
    class Meta:
        verbose_name = "Personal info"  
        verbose_name_plural = "Personal info"

    name = models.CharField(
        verbose_name='Name',
        max_length=50, 
        null=True
    )

    short_desc =models.TextField(
        verbose_name='Short description',
        default='',
    )  

    def __str__(self):
        return "Personal inforamtions"


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

    image = models.ImageField(
        verbose_name='Image',
        blank=True,
        null=True,
        upload_to='uploads/icons',
        default='',
    )

    position =  models.CharField(
        verbose_name='Position',
        max_length=30, 
        help_text='The position I worked at',
        blank=True
    )

    job_desc = models.TextField(
        verbose_name='Job description',
        max_length=600,
        null=True,
        blank=True,
    )

    def clean(self):
        super().clean()
        if self.start_year > self.end_year:
            raise ValidationError("The start year must be less than or equal to the end year.")

    def __str__(self):
        return f"{self.start_year} - {self.end_year} | {self.company} - {self.position_en}"

 
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
    

class SliderText(models.Model):
    view = models.CharField(
        verbose_name='View',
        max_length=100,
        choices=VIEWS,
        unique=True
    )
    
    slider_text = models.CharField(
        verbose_name='Slider text',
        max_length=150
    )

    # Make sure that view field will be lowercase
    def save(self, *args, **kwargs):
        if self.view:
            self.view = self.view.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.view 
    

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
    )
    
    uploaded_at = models.DateTimeField(
        verbose_name='Uploaded at',
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
        try:
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            exif = img._getexif()
            
            if exif is not None:
                orientation = exif.get(orientation)
                
                # Obracamy obraz zgodnie z wartością EXIF
                if orientation == 3:
                    img = img.rotate(180, expand=True)
                elif orientation == 6:
                    img = img.rotate(270, expand=True)
                elif orientation == 8:
                    img = img.rotate(90, expand=True)
        except (AttributeError, KeyError, IndexError):
            # Jeśli obraz nie ma danych EXIF lub wystąpił błąd, po prostu przejdź dalej
            pass

        # Resize image if its too big
        if img.height > 250 or img.width > 180:
            output_size = (180, 250)
            img.thumbnail(output_size, Image.LANCZOS)
            img.save(self.image.path)  # Save image after modyfications
