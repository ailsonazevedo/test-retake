from django.shortcuts import render
from process.models import Process, Parts, JudicialClass
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
    
    print(parts)
    print(judicialclass)
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