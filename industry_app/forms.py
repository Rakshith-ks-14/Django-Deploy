from django import forms
from .models import *

class DesktopForms(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = ('type','price','status','issues')

class MobileForms(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ('type','price','status','issues')

class LaptopForms(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ('type','price','status','issues')
