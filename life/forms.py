from django import forms
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class SendForm(forms.Form):
  name = forms.CharField(label = "Applicant Name", max_length=50)
  email = forms.CharField(label = "Applicant Email", max_length = 50)
  phone = forms.CharField(label = "Applicant Phone Number", max_length = 20)
  date = forms.DateField(label = "Select Interview Date", widget=AdminDateWidget)
  time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
  

class JobForm(forms.Form):
  job_title = forms.CharField(label = "Job Title", max_length = 50)
  description = forms.CharField(label = "Job Description",widget=forms.Textarea)

  
def __init__(self, *args, **kwargs):
    super(SendForm, self).__init__(*args, **kwargs)
    self.fields['date'].widget.attrs['class'] = 'datetimepicker'