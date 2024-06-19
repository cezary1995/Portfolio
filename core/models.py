from django.db import models
from django.core.exceptions import ValidationError


class MyExpertArea(models.Model):
    name = models.CharField(max_length=30, help_text='Technology name')
    img_link = models.CharField(max_length=80)

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
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    company =  models.CharField(max_length=30, help_text='The company where I worked')
    position =  models.CharField(max_length=30, help_text='The position I worked at')
    img_link = models.CharField(max_length=80) 


    def clean(self):
        super().clean()
        if self.start_year > self.end_year:
            raise ValidationError("The start year must be less than or equal to the end year.")

    def __str__(self):
        return f"{self.start_year} - {self.end_year} | {self.company} - {self. position}"
    

class ProfilePicture(models.Model):
    profile_picture = models.ImageField(upload_to='img/images/', blank=True)


class SocialMediaLink(models.Model):
    ICON_CHOICES = [
        ('fa-facebook', 'Facebook'),
        ('fa-twitter', 'Twitter'),
        ('fa-instagram', 'Instagram'),
        ('fa-linkedin', 'LinkedIn'),
        ('fa-github', 'GitHub'),
    ]    
    name = models.CharField(max_length=30, choices=ICON_CHOICES)
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
