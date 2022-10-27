from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import ClientForm
from .models import Company, Service, Advantage


# Create your views here.

class MiniProfileView(TemplateView):

    def get_content_data(self):

        form = ClientForm(initial={'phone': '+7'})
        service1, service2, service3, service4 = Service.objects.all()[:4]
        data = {
            'company': Company.objects.all()[0],
            'service1': service1,
            'service2': service2,
            'service3': service3,
            'service4': service4,
            'advantages': Advantage.objects.all()[0],
            'form': form,

        }
        return data

    def get(self, request):
        data= self.get_content_data()
        return render(request, 'company_profile/index.html', context=data)

    def post(self, request):
        data = self.get_content_data()
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'success')
            return HttpResponseRedirect('/')
        data['form'] = form
        messages.error(request, 'fail')
        return render(request,  'company_profile/index.html', context=data)
