from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.template import RequestContext, Template

from custom_admin.models import TemplateCopy, Account
from custom_admin.utils import auto_get_page, form_injection
import requests

import re

# Create your views here.



def home(request, url):
    url = url

    if request.method == 'POST':
        ...
    else:
        context = RequestContext(request)
        html_modelo = TemplateCopy.objects.get(url_fake__icontains=url)
        

        template = Template(html_modelo.content)
        rended = template.render(RequestContext(request))
        return HttpResponse(rended)




