from django.http import HttpResponse
from django.shortcuts import render

def read_item(request):
   name = request.GET.get('name', 'World')
   message = request.GET.get('message', 'Давай дружить!')
   return HttpResponse(f"Hello, {name}! {message}")
