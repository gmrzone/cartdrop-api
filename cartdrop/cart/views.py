from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def test_cart_view(request):
    return HttpResponse("Hello")
