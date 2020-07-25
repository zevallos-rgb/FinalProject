from django.urls import path
from Adopciones.views import(
    Home,
    MascotasCreateView,
    ListaMascotas,
    DetallesMascotas,
    user,
    crearUsuario,
    listaUsuarios,
    mostrarUsuario,
    eliminarUsuario,
    editarUsuario,
)
app_name = 'Adopciones'
urlpatterns = [
    path('', Home, name = "index"),
    path('create/',MascotasCreateView,name ="create"),
    path('mascotas/',ListaMascotas,name ="lista_mascotas"),
    path('<int:myID>/',DetallesMascotas,name ="detalles"),
    path('user/', user, name="operacionesUsuario"),
    path('crearUsuario/', crearUsuario, name='crearUsuario'),
    path('usuarios/', listaUsuarios, name='listaUsuarios'),
    path('usuarios/<int:myID>/', mostrarUsuario, name='detallesUsuario'),
    path('usuarios/<int:myID>/eliminar', eliminarUsuario, name='eliminarUsuario'),
    path('usuarios/<int:myID>/editar', editarUsuario, name='editarUsuario'),
] 
