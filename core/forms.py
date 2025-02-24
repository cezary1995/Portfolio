from django import forms
from .models.contact import UserMessage
from .models.blog import BlogComment
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

class UserMessageForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control shadow-none', 
                    'placeholder': _('Enter your name')
                    }
                ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control shadow-none', 
                    'placeholder': _('Enter your e-mail')
                    }
                ),

            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control shadow-none', 
                    'placeholder': _('Phone number - optional')
                    }
                ),

            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control shadow-none', 
                    'placeholder': _('Subject')
                    }
                ),
                
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control shadow-none', 
                    'placeholder': _('Type message here...')
                    }
                ),
        }

class UserArticleCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control shadow-none', 
                    'placeholder': _('Enter your name')
                    }
                ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control shadow-none', 
                    'placeholder': _('Enter your e-mail')
                    }
                ),

            'message': forms.Textarea(
                attrs={
                    'class': 'form-control shadow-none', 
                    'placeholder': _('Type message here...')
                    }
                ),
        }
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.uploaded_at = now()  # Set current date
        if commit:
            instance.save()
        return instance