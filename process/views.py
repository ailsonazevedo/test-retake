from django.shortcuts import render
from process.models import Process, Parts
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

    data = {'process': process}
    return render(request, 'processes.html', data)