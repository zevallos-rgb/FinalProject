from django.shortcuts import render,get_object_or_404
from .models import Direcciones,Mascotas
from .forms import MascotasForm
# Create your views here.
def Home(request):
    context = {
        "url":Direcciones
    }
    return render(request,'index.html',context)
def MascotasCreateView(request):
    form = MascotasForm(request.POST,files = request.FILES)
    if form.is_valid():
        form.save()
        form = MascotasForm
    context = {
        'form' : form
    }
    return render(request,'createMascotas.html',context)
def ListaMascotas(request):
    obj = Mascotas.objects.all()
    context = {
    "obj":obj
    }
    return render(request,"mascotas.html",context)
def DetallesMascotas(request,myID):
    obj = get_object_or_404(Mascotas, id = myID)
    context = {
        'objecto':obj
    }
    return render(request,'detalles.html',context)