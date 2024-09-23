from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
# Create your views here.

def scrape(request):
    if request.method=="POST":
        site=request.POST.get('site')
        page=requests.get(site)

        soup=BeautifulSoup(page.text,'html.parser')

        # link_address=[]

        for link in soup.find_all('a'):
            link_address=link.get('href')
            likn_text=link.string
            # link_address.append(link.get('href'))
            Link.objects.create(address=link_address,name=likn_text)
        return HttpResponseRedirect('/')
    else:
        data=Link.objects.all()

    return render(request,'result.html',{'data':data})


def clear(request):
    Link.objects.all().delete()
    return render(request,'result.html')
