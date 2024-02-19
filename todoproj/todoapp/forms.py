from .models import Name
from django import forms 


class TodoForm(forms.ModelForm):
    class Meta:
        model =Name
        fields =['name','date','image']