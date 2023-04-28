from django.urls import path

from tolist.views import log_in, log_out

from . import views

urlpatterns = [
    
    #Login/Logout/CrearCuenta
    path('login/', log_in, name="login"),
    path('logout/', log_out, name="logout"),
    
    path('', views.index, name="index"),
    
    path('crear_cuenta/', views.crear_cuenta, name="crear_cuenta"),
    
    #ToList 
    path('tolist/tareas_main/', views.tareas_main, name="tareas_main"),
    path('tolist/cargar_tareas/', views.cargar_tareas, name="cargar_tareas"),
    path('tolist/cargar_filtros/', views.cargar_filtros, name="cargar_filtros"),
    path('tolist/crear_tarea/', views.crear_tarea, name="crear_tarea"),

]
