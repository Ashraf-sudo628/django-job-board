from django import forms

from .models import Apply , JOb

#Apply to a Job Class
class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['Name','Email','Website','CV','Cover_Litter']


# Add New Job Class

class AddJobForm(forms.ModelForm):
     class Meta:
         model =JOb
         fields = '__all__'
         exclude =  ('slug','Owner')
       