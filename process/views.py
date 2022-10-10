from django.shortcuts import render
from process.api.serializers import ProcessSerializer
from process.models import Process, Parts, JudicialClass
import requests
from bs4 import BeautifulSoup
# Create your views here.

def home(request):
    process = Process.objects.all().order_by('-created')
    parts = Parts.objects.all()

    data = {
        'process': process,
        'parts': parts,
    }
    return render(request, 'index.html', data)

def process(request):
    process = Process.objects.all().order_by('-created')
    judicialclass = JudicialClass.objects.all()
    parts = Parts.objects.all()
    
    data = {
        'process': process,
        'JudicialClass': judicialclass,
        'parts': parts,

    }
    return render(request, 'processes.html', data)

# def parts(request):
#     parts = Parts.objects.all()

#     data = {'parts': parts}
#     return render(request, 'parts.html', data)


def scraping_parts(request):
    url = 'http://127.0.0.1:5500/process/templates/processo-02.html' 
    response = requests.get(url)
    if response.status_code == 200:
        print('ok')
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        parts = soup.find('ul',{'class':'list-group list-group-flush list-group-party'})
        envolvidos = parts.find_all('span')
        full_parts = []
        for i in envolvidos:
            full_parts.append(i.text)
            # def clean_parts(self):
            #     data = self.cleaned_data["full_parts"]
            #     data = data.replace("\n", " ")
            #     return data
        print(full_parts)       
    else:
        print('error')

    data = {'parts': full_parts}
    return render(request, 'parts.html', data)
