from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']
        widgets = {'name':forms.TextInput(attrs = {'class' : 'name-class'}), 'password':forms.PasswordInput(attrs={'class': 'password-class'})}