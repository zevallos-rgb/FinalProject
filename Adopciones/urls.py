from django.urls import path
from Adopciones.views import(
    Home,
    MascotasCreateView,
    ListaMascotas,
    DetallesMascotas,
)
app_name = 'Adopciones'
urlpatterns = [
    path('',Home,name = "index"),
    path('create/',MascotasCreateView,name ="create"),
    path('mascotas/',ListaMascotas,name ="lista_mascotas"),
    path('<int:myID>/',DetallesMascotas,name ="detalles")
]