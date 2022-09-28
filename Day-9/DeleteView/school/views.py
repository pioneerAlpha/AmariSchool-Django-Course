from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Student
from django.views.generic.base import TemplateView
from .forms import StudentForm

class StudentCreateView(CreateView):
    success_url = '/thanks/'
    form_class = StudentForm
    template_name = 'school/student_form.html'

class StudentUpdateView(UpdateView):
    model = Student
    success_url = '/thanks-update/'
    form_class = StudentForm
    template_name = 'school/student_form.html'

class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/thanks-delete/'
    template_name = 'school/delete.html'

class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'

class ThanksUpdateTemplateView(TemplateView):
    template_name = 'school/thanks-update.html'

class ThanksDeleteTemplateView(TemplateView):
    template_name = 'school/thanks-delete.html'
