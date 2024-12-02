from django import forms
from .models.contact import UserMessage
from .models.blog import BlogComment
from django.utils.timezone import now


class UserMessageForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'Enter your e-mail'}),
            'phone': forms.TextInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'Phone number - optional'}),
            'subject': forms.TextInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control shadow-none', 'placeholder': 'Type message here...'}),
        }

class UserArticleComment(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'Enter your e-mail'}),
            'message': forms.Textarea(attrs={'class': 'form-control shadow-none', 'placeholder': 'Type message here...'}),
        }
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.uploaded_at = now()  # Ustaw automatycznie bieżącą datę i godzinę
        if commit:
            instance.save()
        return instance