from django.shortcuts import render
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

def parts(request):
    parts = Parts.objects.all()

    data = {'parts': parts}
    return render(request, 'parts.html', data)

def scraping(request):
    url = 'https://www.tjmg.jus.br/portal-da-transparencia/contracheque/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', attrs={'class': 'table table-striped table-bordered'})
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        print(cols)
    return render(request, 'scraping.html')