from typing import Any
from django.shortcuts import render
from app.forms import *
# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView,FormView

#TemplateView
class Template(TemplateView):
    template_name='Temp.html'

    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='Mythu'
        ECDO['SFO']=StudentForm
        return ECDO
    
    def post(self,request):
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data is Inserted')


#FormView    
class StudentInsertForm(FormView):
    form_class=StudentForm
    template_name='StudentInsertForm.html'
    def form_valid(self, form) -> HttpResponse:
        form.save()
        return HttpResponse('Data Inserted Succesfully')
