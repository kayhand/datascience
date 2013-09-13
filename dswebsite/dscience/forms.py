from django import forms
from django.forms import ModelForm
from dscience.models import Feedback

class PresentationForm(forms.Form):
    presFile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
)

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )

class AssignmentForm(forms.Form):
    assignfile = forms.FileField(
        label='Upload your assigment',
    )
    dueDate = forms.DateField( widget=forms.TextInput(attrs={'id':'id_form_date_field'}))

class MyAssignmentForm(forms.Form):
    myassignfile = forms.FileField(
                            label='Upload your assigment',
                 )

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['clarity', 'exposition', 'smoothness', 'qa', 'comments']
        widgets = {'clarity' : forms.RadioSelect(), 'exposition' : forms.RadioSelect(), 'smoothness' : forms.RadioSelect(), 'qa' : forms.RadioSelect(), }
