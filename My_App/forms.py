#creating Django form to add student data

from .models import Vidyarthi
from django import forms

class StudentData(forms.ModelForm):
    class Meta:
        model = Vidyarthi
        fields = ['name','Course','city']