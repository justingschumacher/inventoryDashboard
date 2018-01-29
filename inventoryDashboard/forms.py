from django import forms
from .models import Vmguest


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Vmguest
        fields = '__all__'
