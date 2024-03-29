from django import forms
from.models import Masterdata5,Mark_Attendance2



class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)

class MasterForm(forms.ModelForm):
	class Meta:
		model = Masterdata5
		fields = ['name', 'roll_number', 'class_name', 'email']


class AttForm(forms.ModelForm):
	class Meta:
		model = Mark_Attendance2
		fields = ['roll_number', 'class_name', 'subject']
		
class CheckAttForm(forms.Form):
	roll_number = forms.CharField(max_length=100)

class CheckByDate(forms.Form):
	class Meta:
		date1 = forms.CharField(max_length =100)
		fields = ['roll_number', 'class_name', 'subject']

	