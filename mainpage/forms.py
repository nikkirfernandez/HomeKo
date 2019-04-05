# License: MIT License
# CODE HISTORY #
# Sontillano     # Feb 5, 2019     # added SearchHousing, AddRequest, SignUp
# Sontillano     # Mar 6, 2019     # added ReportComment

# File creation date: Feb. 5, 2019

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from .choices import *
from .models import *


class SearchHousing(forms.Form):
     area = forms.ChoiceField(choices=AREA_CHOICES, widget=forms.Select(), required=False)
     propertyType = forms.ChoiceField(choices=PROPERTY_CHOICES, widget=forms.Select(), required=False)
     homeType = forms.ChoiceField(choices=HOME_CHOICES, widget=forms.Select(), required=False)
     priceMin = forms.FloatField(required=False)
     priceMax = forms.FloatField(required=False)
     kitchen = forms.BooleanField(initial=False, required=False)
     aircon = forms.BooleanField(initial=False, required=False)
     washer = forms.BooleanField(initial=False, required=False)
     dryer = forms.BooleanField(initial=False, required=False)
     wifi = forms.BooleanField(initial=False, required=False)
     iron = forms.BooleanField(initial=False, required=False)
     tv = forms.BooleanField(initial=False, required=False)
     parking = forms.BooleanField(initial=False, required=False)
     pet = forms.BooleanField(initial=False, required=False)
     smoking = forms.BooleanField(initial=False, required=False)
     curfew = forms.BooleanField(initial=False, required=False)


class AddRequest(forms.ModelForm):
     message = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 3}), max_length=500)

     class Meta:
          model = Request
          fields = ['sender', 'reqtype', 'message']
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
               self.fields[field].widget.attrs.update({
                    'class': 'form-control'
               })

class AddComment(forms.ModelForm):
     comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), max_length=500, required=True, )
     class Meta:
          model = Feedback
          fields = ['comment']
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
               self.fields[field].widget.attrs.update({
                    'class': 'form-control'
               })

class OwnerLogin(forms.Form):
     uname = forms.CharField(max_length=50, required=True)
     pw = forms.CharField(max_length=50, required=True)

class OwnerRegistrationForm(UserCreationForm):
     first_name = forms.CharField()
     last_name = forms.CharField()
     email = forms.EmailField()
     contact = forms.CharField()

     class Meta:
          model = User
          fields = ['first_name','last_name','username','email','contact','password1','password2']

     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.helper = FormHelper()
          self.helper.form_show_labels = False
          super(OwnerRegistrationForm, self).__init__(*args, **kwargs)
          self.fields['email'].required = False
          self.fields['contact'].required = False
