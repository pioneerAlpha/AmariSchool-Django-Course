from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Student
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django import forms
from .forms import StudentForm

class StudentCreateView(CreateView):
    # model = Student
    # fields = ['name', 'email', 'password']
    # success_url = '/thanks/'
    template_name = 'school/form.html'
    form_class = StudentForm

    # def get_form(self):
    #     form = super().get_form()
    #     form.fields['name'].widget = forms.TextInput(attrs = {'class' : 'name-class'})
    #     form.fields['password'].widget = forms.PasswordInput(attrs = {'class' : 'password-class'})
    #     return form

class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'

class StudentDetailView(DetailView):
    model = Student

