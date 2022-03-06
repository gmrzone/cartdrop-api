from django.http import HttpResponse
from django.shortcuts import render

from .models import Cart

# Create your views here.


def test_cart_view(request):
    Cart(request)
    return HttpResponse("Hello")
