from django.shortcuts import render
from process.api.serializers import ProcessSerializer
from process.models import Process, Parts
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
    parts = Parts.objects.all()
    
    data = {
        'process': process,
        'parts': parts,

    }
    return render(request, 'processes.html', data)

# def parts(request):
#     parts = Parts.objects.all()

#     data = {'parts': parts}
#     return render(request, 'parts.html', data)

def scraping_process2(request):
    url = 'http://127.0.0.1:5500/process/templates/processo-02.html'
    response = requests.get(url)
    if response.status_code == 200:
        print('ok')
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        process = soup.find('div',{'class':'col-2'})
        process_class = process.find_all('span')

        number_process = soup.find('div',{'class':'col-12 d-flex align-items-center'})
        process_number = number_process.find_all('h4',{'class':'mr-auto'})

        parts = soup.find('ul',{'class':'list-group list-group-flush list-group-party'})
        involved = parts.find_all('span')

        judge = soup.find('div',{'class':'col-2'})
        judge_name = judge.find_all('span')
        for i in judge_name:
            judge = i.text
        print(judge)
        
        full_parts = []
        for i in involved:
            # full_parts.append(i.text.replace(' ','').replace('\n','').strip())
            parts = Parts.objects.create(name=i.text.replace(' ','').replace('\n',''))
        print(parts)  

        for i in process_class:
            judicialclass = i.text
        print(judicialclass)
        for i in process_number:
            number = i.text.replace(' ', '')
        print(number)
        process = Process.objects.create(
            number = number,
            judicialClass = judicialclass,
            judge = judge,
        )
        process.save()
    else:
        print('error')
    return render(request, 'parts.html')

