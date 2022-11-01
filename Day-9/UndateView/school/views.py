from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Student
from django.views.generic.base import TemplateView
from .forms import StudentForm

class StudentCreateView(CreateView):
    # model = Student
    # fields = ['name', 'email', 'password']
    success_url = '/thanks/'

    # def get_form(self):
    #     form = super().get_form()
    #     form.fields['name'].widget = forms.TextInput(attrs = {'class' : 'name-class'})
    #     form.fields['password'].widget = forms.PasswordInput(attrs = {'class' : 'password-class'})
    #     return form
    form_class = StudentForm
    template_name = 'school/student_form.html'


class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'

class StudentUpdateView(UpdateView):
    model = Student
    # fields = ['name', 'email', 'password']
    success_url = '/thanks-update/'

    # def get_form(self):
    #     form = super().get_form()
    #     form.fields['name'].widget = forms.TextInput(attrs = {'class' : 'name-class'})
    #     form.fields['password'].widget = forms.PasswordInput(attrs = {'class' : 'password-class'})
    #     return form

    form_class = StudentForm
    template_name = 'school/student_form.html'

class ThanksUpdateTemplateView(TemplateView):
    template_name = 'school/thanks-update.html'