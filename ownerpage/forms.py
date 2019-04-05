# This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.

# CODE HISTORY #
# Sontillano     # Mar 29, 2019     # added editOwnerForm, editContactForm, housingForm, housingAddtnlinfoForm, roomCostForm

# File creation date: Mar 29, 2019

from django import forms
from mainpage.models import *


class editOwnerForm(forms.ModelForm):
    
     class Meta:
          model = Owner
          fields = ['ownername', 'firstname', 'lastname', 'email']
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
               self.fields[field].widget.attrs.update({
                    'class': 'form-control'
               })

class editContactForm(forms.ModelForm):

     class Meta:
          model = Contact
          fields = ['contactno']
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
               self.fields[field].widget.attrs.update({
                    'class': 'form-control'
               })

class housingForm(forms.ModelForm):
     maphtml = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), max_length=500, required=False)
     class Meta:
          model = Housing
          fields = ['housingname', 'area', 'address', 'propertytype', 'housetype', 'maphtml']
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
               self.fields[field].widget.attrs.update({
                    'class': 'form-control'
               })

class housingAddtnlinfoForm(forms.ModelForm):
     description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), max_length=300, required=False, )
     class Meta:
          model = HousingAdditionalInfo
          fields = ['additionalinfoid', 'description']
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
               self.fields[field].widget.attrs.update({
                    'class': 'form-control'
               })

class roomCostForm(forms.ModelForm):

     class Meta:
          model = RoomCost
          fields = ['roomname', 'cost']
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
               self.fields[field].widget.attrs.update({
                    'class': 'form-control'
               })
