# This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.

# CODE HISTORY #
# Sontillano     # Feb 11, 2019     # added AdminLogin, addAdditionalinfo, addArea, addContact, addFeedback, addHousetype, addHousingAddtnlinfo, addHousingOwner, addHousingRequest, addHousing, addOwner, addPicture, addPropertytype, addRequest, addRoomCost

# File creation date: Feb. 11, 2019

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

class editHousingForm(forms.ModelForm):
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

class editHousingAddtnlinfoForm(forms.ModelForm):
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

class editRoomCostForm(forms.ModelForm):

     class Meta:
          model = RoomCost
          fields = ['roomname', 'cost']
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
               self.fields[field].widget.attrs.update({
                    'class': 'form-control'
               })
