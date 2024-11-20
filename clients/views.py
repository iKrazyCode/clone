from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import ClientProduct


# Create your views here.
def validations(request):
    product = request.GET.get('product')
    client = request.GET.get('client')
    
    if (product != None) and (client != None):
        try:
            client = ClientProduct.objects.get(client_id=client, product=product)
            data = client.response
            
            return HttpResponse(data)
        except ClientProduct.DoesNotExist:
            return HttpResponse('Cliente não existente')
    
    return HttpResponse('')