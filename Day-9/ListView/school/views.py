from django.shortcuts import render
from .models import Student
from django.views.generic.list import ListView

class StudentListView(ListView):
    model = Student

    # template_name_suffix = '_get'
    # ordering = ['roll']

    template_name = 'school/student.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.filter(course='English')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['freshers'] = Student.objects.all().order_by('roll')
        return context

