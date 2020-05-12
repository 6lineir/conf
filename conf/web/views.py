from django.shortcuts import render
from .models import ads
# Create your views here.
def index(request):
    ads_list = ads.objects.all()
    context = {
        'ads_list' : ads_list
    }
    print (context)
    return render(request, 'web/index.html', context)

def about(request):
    return render(request, 'web/about.html')