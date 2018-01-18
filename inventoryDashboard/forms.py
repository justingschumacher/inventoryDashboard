from django import forms
from inventoryDashboard.models import vmwareGuest


class VmwareGuestForm(forms.ModelForm):

    class Meta:
        model = vmwareGuest
        fields = '__all__'