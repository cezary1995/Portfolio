from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from core.utils import ICON_CHOICES
from django.utils.timezone import now

class MyExpertArea(models.Model):
    name = models.CharField(
        verbose_name='Technology name',
        max_length=30,
        help_text='Technology name',
    )

    img_link = models.CharField(
        verbose_name='Image',
        max_length=80
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
    start_year = models.PositiveSmallIntegerField(
        verbose_name = 'Start Year'
    )
    end_year = models.IntegerField()
    company =  models.CharField(
        max_length=30,
        help_text='The company where I worked'
    )
    position =  models.CharField(
        verbose_name='Position',
        max_length=30, 
        help_text='The position I worked at'
    )
    img_link = models.CharField(
        verbose_name='IMG_link',
        max_length=80
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
        default='Default Title',    
    )

    image = models.ImageField(
        verbose_name='Image',
        upload_to='media/uploads/profile_pictures',
        default='default_img.jpg',
    )
    
    uploaded_at = models.DateTimeField(
        verbose_name='Uploaded at',
        auto_now_add=True,
        default=now,
    )

    display = models.BooleanField(
        verbose_name='Display',
        default=False,
    )

    def __str__(self):
        return self.title


class SocialMediaLink(models.Model):
    name = models.CharField(
        verbose_name='Social Media Name',
        max_length=30,
        choices=ICON_CHOICES,
    )
    url = models.URLField()

    def __str__(self):
        return self.get_name_display()
    

class OfferedService(models.Model):
    name = models.CharField(max_length=30, help_text='Service name')
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
        

class Project(models.Model):
    link = models.CharField(max_length=80, default='link_to_project') 
