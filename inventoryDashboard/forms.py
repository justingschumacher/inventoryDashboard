from django import forms
from .models import Vmguest


class VmguestForm(forms.ModelForm):

    class Meta:
        model = Vmguest
        fields = '__all__'

