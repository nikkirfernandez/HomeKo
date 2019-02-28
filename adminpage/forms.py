# This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.

# CODE HISTORY #
# Sontillano     # Feb 11, 2019     # added AdminLogin, addAdditionalinfo, addArea, addContact, addFeedback, addHousetype, addHousingAddtnlinfo, addHousingOwner, addHousingRequest, addHousing, addOwner, addPicture, addPropertytype, addRequest, addRoomCost

# File creation date: Feb. 11, 2019

from django import forms
from .choices import *
from mainpage.models import *

class AdminLogin(forms.Form):
     uname = forms.CharField(max_length=50, required=True)
     pw = forms.CharField(max_length=50, required=True)

class addAdditionalinfoForm(forms.ModelForm):
    
     class Meta:
          model = Additionalinfo
          fields = ['additionalinfoname', 'additionalinfotype']
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
               self.fields[field].widget.attrs.update({
                    'class': 'form-control'
               })

class addAreaForm(forms.ModelForm):

     class Meta:
          model = Area
          fields = ['areaname']
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
               self.fields[field].widget.attrs.update({
                    'class': 'form-control'
               })
		
class addContactForm(forms.ModelForm):

     class Meta:
          model = Contact
          fields = ['contactno', 'ownerid']
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
               self.fields[field].widget.attrs.update({
                    'class': 'form-control'
               })

class addFeedbackForm(forms.ModelForm):
  
     class Meta:
          model = Feedback
          fields = ['status']
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
               self.fields[field].widget.attrs.update({
                    'class': 'form-control'
               })

class addHousetypeForm(forms.ModelForm):

     class Meta:
          model = Housetype
          fields = ['housetypename']
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
               self.fields[field].widget.attrs.update({
                    'class': 'form-control'
               })

class addHousingAddtnlinfoForm(forms.ModelForm):
     description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), max_length=300, required=False, )
     class Meta:
          model = HousingAdditionalInfo
          fields = ['additionalinfoid', 'description', 'housingid']
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
               self.fields[field].widget.attrs.update({
                    'class': 'form-control'
               })

class addHousingOwnerForm(forms.ModelForm):

     class Meta:
          model = HousingOwner
          fields = ['housingid', 'ownerid']
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
               self.fields[field].widget.attrs.update({
                    'class': 'form-control'
               })

class addHousingRequestForm(forms.ModelForm):

     class Meta:
          model = HousingRequest
          fields = ['housingid', 'requestid']
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
               self.fields[field].widget.attrs.update({
                    'class': 'form-control'
               })

class addHousingForm(forms.ModelForm):
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

class addOwnerForm(forms.ModelForm):

     class Meta:
          model = Owner
          fields = ['ownername', 'firstname', 'lastname', 'email']
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
               self.fields[field].widget.attrs.update({
                    'class': 'form-control'
               })

class addPictureForm(forms.ModelForm):

     class Meta:
          model = Picture
          fields = ['filename', 'housingid']
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
               self.fields[field].widget.attrs.update({
                    'class': 'form-control'
               })


class addPropertytypeForm(forms.ModelForm):

     class Meta:
          model = Propertytype
          fields = ['propertytypename']
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
               self.fields[field].widget.attrs.update({
                    'class': 'form-control'
               })

class addRequestForm(forms.ModelForm):

     class Meta:
          model = Request
          fields = ['reqtype', 'status']
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
               self.fields[field].widget.attrs.update({
                    'class': 'form-control'
               })

class addRoomCostForm(forms.ModelForm):

     class Meta:
          model = RoomCost
          fields = ['roomname', 'cost', 'housingid']
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
               self.fields[field].widget.attrs.update({
                    'class': 'form-control'
               })
		