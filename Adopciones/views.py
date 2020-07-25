from django.shortcuts import render,get_object_or_404,redirect
from .models import Direcciones,Mascotas,Usuario
from .forms import MascotasForm,UsuarioForm
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




def crearUsuario(request):
    form = UsuarioForm(request.POST)
    if form.is_valid():
        form.save()
        form = UsuarioForm
    context = {
        'form' : form,
        "url":Direcciones,
    }
    return render(request, 'usuario/crearUsuario.html', context)
def listaUsuarios(request):
    obj = Usuario.objects.all()
    context = {
        "obj":obj,
        "url":Direcciones,
    }
    return render(request, "usuario/listaUsuario.html", context)
def mostrarUsuario(request, myID):
    obj = get_object_or_404(Usuario, id = myID)
    context = {
        'obj':obj,
        "url":Direcciones,
    }
    return render(request,'usuario/detallesUsuario.html', context)
def eliminarUsuario(request, myID):
    obj = get_object_or_404(Usuario, id = myID)
    if request.method == 'POST':
        obj.delete()
        return redirect('../')
    context = {
        'obj':obj,
        "url":Direcciones,
    }
    return render(request,'usuario/eliminarUsuario.html', context)
def editarUsuario(request, myID):
    obj = Usuario.objects.get(id = myID)
    form = UsuarioForm(request.POST, instance=obj)
    if form.is_valid():
        form.save()
        form = UsuarioForm()
    context = {
        'form' : form,
        "url":Direcciones,
    }
    return render(request, 'usuario/editarUsuario.html', context)
def user(request):
    context = {
        "url":Direcciones,
    }
    return render(request,'usuario/operacionesUsuario.html', context)
