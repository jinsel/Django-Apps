from django import forms
from .models import Todo


class TodoInputForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ("text",)
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Add new Task ...', 'class': 'form-control'})
        }
