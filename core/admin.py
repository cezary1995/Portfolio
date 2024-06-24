from django.contrib import admin
from .models.index import (
    MyExpertArea, 
    WorkExperience, 
    SocialMediaLink,  
    OfferedService, 
    Project, 
    ProfilePicture,
)


admin.site.register(MyExpertArea)
admin.site.register(WorkExperience)
admin.site.register(SocialMediaLink)
admin.site.register(OfferedService)
admin.site.register(Project)
admin.site.register(ProfilePicture)