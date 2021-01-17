from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView, DetailView

from pations.models import Patient


class HomePage(TemplateView):
    template_name = 'home.html'


class CreatePatiant(CreateView):
    model = Patient
    template_name = 'patient/new_patient.html'
    fields = ['name','surname','adress','phonenumber','discrict','diagnos']

