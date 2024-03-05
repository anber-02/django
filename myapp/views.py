
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login (request):
    return render(request,'login.html')

def main (request):
    return HttpResponse('Hello word')

# Create your views here.
