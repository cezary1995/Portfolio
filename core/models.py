from django.db import models
from django.core.exceptions import ValidationError


class My_expert_area(models.Model):
    name = models.CharField(max_length=20, help_text='Technology name')
    image = models.ImageField(upload_to='img/images/', blank=True)

    def clean(self):
        super().clean()
        if My_expert_area.objects.count() >= 3:
            raise ValidationError("You cannot create more than 6 objects.")

    def save(self):
        self.clean()
        super().save()

    def __str__(self):
        return self.name 
    

class Work_experience(models.Model):
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    company =  models.CharField(max_length=20, help_text='The company where I worked')
    position =  models.CharField(max_length=20, help_text='The position I worked at')


    def clean(self):
        super().clean()
        if self.start_year > self.end_year:
            raise ValidationError("The start year must be less than or equal to the end year.")

    def __str__(self):
        return f"{self.start_year} - {self.end_year} | {self.company} - {self. position}"
    