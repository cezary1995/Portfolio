from django import forms
from .models.contact import UserMessage


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