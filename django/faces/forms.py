from django import forms
 
# from faces.models import Face
 
 
class UploadFileForm(forms.Form):
     
    file = forms.FileField()