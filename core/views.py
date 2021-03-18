from django.http import JsonResponse
from django.shortcuts import render

from .models import *
from accounts.models import *
from accounts.forms import *

def home(request):
    s=Song.objects.all().order_by('-upvotes','downvotes')
    context={
        'songs':s,
        'form': RegistrationForm,
    }

    return render(request,'home.html',context)

def upload(request):
    pass

def artists(request):
    pass



