from django.shortcuts import redirect, render
from process.api.serializers import ProcessSerializer
from process.models import Process, Parts
import requests
from bs4 import BeautifulSoup
import re
# Create your views here.

def home(request):
    process = Process.objects.all().order_by('-created')[:3]
    parts = Parts.objects.all()

    data = {
        'process': process,
        'parts': parts,
    }
    return render(request, 'index.html', data)

def process(request):
    process = Process.objects.all().order_by('-created')
    parts = Parts.objects.all()
    
    data = {
        'process': process,
        'parts': parts,

    }
    return render(request, 'processes.html', data)

def process_detail(request, pk):
    process = Process.objects.get(id=pk)
    parts = Parts.objects.all()
    data = {
        'process': process,
        'parts': parts,
    }
    return render(request, 'components\process_detail.html', data)

def process_delete(request, pk):
    process = Process.objects.get(id=pk)
    process.delete()
    return redirect('process')

def parts(request):
    parts = Parts.objects.all()
    data = {
        'parts': parts,
    }
    return render(request, 'parts.html', data)

def scraping_process1(request):
    url = 'http://127.0.0.1:5500/process/templates/processo-01.html'
    response = requests.get(url)
    if response.status_code == 200:
        print('ok')
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        
        process = soup.find('div',{'class':'col-2'})
        process_class = process.find_all('span')
        for i in process_class:
            judicialclass = i.text
        print(judicialclass)

        number_process = soup.find('div',{'class':'col-12 d-flex align-items-center'})
        process_number = number_process.find_all('h4',{'class':'mr-auto'})
        for i in process_number:
            number = i.text.replace('Ativo', '').replace(' ', '')
        print(number)

        parts = soup.find('ul',{'class':'list-group list-group-flush list-group-party'})
        involved = parts.find_all('span', {'class':'mr-auto'})
        parts_list = []
        for i in involved:
            parts = Parts.objects.create(name=i.text.replace('\n','').replace('  ', ''))
            parts.save()
            parts_list.append(parts)
        print(parts_list) 

        judge = soup.find(string=re.compile('Mariana'))
        print(judge)

        process_topic = soup.find(string='Assunto:').find_next('span').text
        print(process_topic)
        
        process = Process.objects.create(
            number = number,
            judicialClass = judicialclass,
            judge = judge,
            topic = process_topic,
        )
        process.save()
    else:
        print('error request')
    return render(request, 'process1.html')

def scraping_process2(request):
    url = 'http://127.0.0.1:5500/process/templates/processo-02.html'
    response = requests.get(url)
    if response.status_code == 200:
        print('ok')
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        
        process = soup.find('div',{'class':'col-2'})
        process_class = process.find_all('span')
        for i in process_class:
            judicialclass = i.text
        print(judicialclass)

        number_process = soup.find('div',{'class':'col-12 d-flex align-items-center'})
        process_number = number_process.find_all('h4',{'class':'mr-auto'})
        for i in process_number:
            number = i.text.replace(' ', '')
        print(number)

        parts = soup.find('ul',{'class':'list-group list-group-flush list-group-party'})
        involved = parts.find_all('span', {'class':'mr-auto'})
        parts_list = []
        for i in involved:
            parts = Parts.objects.create(name=i.text.replace('\n','').replace('  ', ''))
            parts.save()
            parts_list.append(parts)
        print(parts_list)

        judge = soup.find(string=re.compile('Domingos'))
        print(judge)

        process_topic = soup.find(string='Assunto:').find_next('span').text
        print(process_topic)
        
        process = Process.objects.create(
            number = number,
            judicialClass = judicialclass,
            judge = judge,
            topic = process_topic,
            # parts = parts.parts.set(parts_list),
        )
        process.save()
    else:
        print('error request')
    return render(request, 'process2.html')

