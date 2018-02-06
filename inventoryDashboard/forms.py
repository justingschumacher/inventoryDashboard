from django import forms
from .models import DjangoReportCore


class VmguestForm(forms.ModelForm):

    class Meta:
        model = DjangoReportCore
        fields = '__all__'

