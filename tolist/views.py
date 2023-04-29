from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib import messages

from datetime import datetime

import logging

from challenge_tolist.settings import LOGIN_PAGE, LOGIN_OK
from controllers import tolist_controller
from tolist.models import *

_log = logging.getLogger("tolist")


# Create your views here.

@csrf_exempt
def log_in(request):
    context = RequestContext(request)
    
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            messages.add_message(request, messages.ERROR, "Por favor complete todos los campos")
            return render (request , LOGIN_PAGE, context.flatten())
        else:
            
            try:
                user = User.objects.get(username=username)
            
            except Exception as e:
                _log.error(str(e))
                
                messages.add_message(request, messages.ERROR, "Usuario y/o contraseña incorrecta")
                
                return render (request , LOGIN_PAGE, context.flatten())
            
            user = authenticate(username=username,password=password)
            
            if user:
                
                if user.is_authenticated:
                    
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS, f"Bienvenido {username}")
                    
                    return redirect(LOGIN_OK)
                
                else:
                    messages.add_message(request, messages.ERROR, "Error con el usuario. Comunicarse con administrador")
                    return HttpResponse(status=302)
    
    return render (request, LOGIN_PAGE, context.flatten())

@csrf_exempt
def log_out(request):
    
    logout(request)
        
    messages.add_message(request, messages.SUCCESS, 'Sesión finalizada')

    return redirect("/proyect/")


def index(request):
    
    try:
        result = {}
        
        return render (request, 'menu/includes/base.html', result)
        
    except Exception as e:
        _log.error(str(e))
        return HttpResponse(status=500)
    
    
def crear_cuenta(request):
    
    try:
        _nombre = request.POST['username']
        _password = request.POST['password']
        _email = request.POST['email']
        
        _existe_email = User.objects.filter(email = _email).count()

        if _existe_email.__eq__(1):
            
            return HttpResponse(status=300)
    
        _existe_username = User.objects.filter(username = _nombre).count()

        if _existe_username.__eq__(1):
            
            return HttpResponse(status=301)
                            
        try:
            
            User.objects.create_user(username=_nombre, 
                                    is_active=1,
                                    email=_email,
                                    password=_password)
            
        except Exception as e:
            return HttpResponse(status=500)
        
        return HttpResponse(status=200)
        
    except Exception as e:
        _log.error(f"Error al crear cuenta. {str(e)}")
        return HttpResponse(status=500)
    
@login_required(login_url=LOGIN_PAGE)
def tareas_main(request):
    
    _pagina = 'tareas/tolist_main.html'
    
    try:
        _result = {}
        
        return render (request, _pagina, _result)
        
    except Exception as e:
        _log.error(str(e))
        return HttpResponse(status=500)
    

@login_required(login_url=LOGIN_PAGE)
def cargar_tareas(request):
    
    _pagina = 'tareas/_tabla_tareas.html'
    
    try:
        user = request.user
        
        _lst_tareas = Tareas.objects.filter(id_user = user.pk).order_by('-estado')
        
        _fecha_hoy = datetime.today()
        
        _result = {
            'tareas': _lst_tareas,
            'fecha_hoy': _fecha_hoy
        }
        
        return render (request, _pagina, _result)
        
    except Exception as e:
        _log.error(f"Error al cargar las tareas del usuario. {str(e)}")
        return HttpResponse(status=500)
    
    
@login_required(login_url=LOGIN_PAGE)
def cargar_filtros(request):
    
    _pagina = 'tareas/_inputs.html'
        
    try:
        
        _prioridades = Prioridades.objects.all()
        _categorias = Categorias.objects.all()
        _accion = 'nuevo'

        _result = {
            'accion': _accion,
            'categorias': _categorias,
            'prioridades': _prioridades
        }
        
        return render (request, _pagina, _result)
        
    except Exception as e:
        _log.error(f"Error al cargar filtros. {str(e)}")
        return HttpResponse(status=500)
    
    
@login_required(login_url=LOGIN_PAGE)
def crear_tarea(request):
            
    try:
        _accion = request.POST['accion']
        _descripcion = request.POST['descripcion']
        _prioridad = request.POST['prioridad']
        _categoria = request.POST['categoria']
        _fh_limite = request.POST['fechaLimite']
        _user = request.user
        
        if _accion.__eq__('nuevo'):
    
            _result = tolist_controller.crear_tarea(_descripcion, _prioridad, _categoria, _fh_limite, _user)
            
            if _result.find("Error").__eq__(0):
                
                return HttpResponse(status=500)
            
            else:

                return HttpResponse(status=200)
        
        else:
            
            _pk = request.POST['pk']
            
            _result = tolist_controller.editar_tarea(_pk ,_descripcion, _prioridad, _categoria, _fh_limite)
        
            if _result.find("Error").__eq__(0):
                
                return HttpResponse(status=500)
            
            else:

                return HttpResponse(status=200)
        
    except Exception as e:
        _log.error(f"Error al crear tarea. {str(e)}")
        return HttpResponse(status=500)
    
@login_required(login_url=LOGIN_PAGE)
def eliminar_tarea(request):
        
    try:
        _pk_tarea = request.POST['pk']
        
        _instancia_tarea = Tareas.objects.get(pk = _pk_tarea)
        
        _desc_tarea = _instancia_tarea.descripcion
        
        _instancia_tarea.delete()
        
        _log.info(f"Tarea eliminada con exito. {_desc_tarea}")
        
        return HttpResponse(status=200)
        
    except Exception as e:
        _log.error(f"Error al eliminar la tarea. {str(e)}")
        return HttpResponse(status=500)


@login_required(login_url=LOGIN_PAGE)
def modificar_tarea(request):
    
    _pagina = 'tareas/_inputs.html'
        
    try:
        _pk_tarea = request.POST['pk']
        
        _accion = 'editar'
                
        _prioridades = Prioridades.objects.all()
        _categorias = Categorias.objects.all()
        
        _instancia_tarea = Tareas.objects.get(pk = _pk_tarea)
        
        try:
            
            _fh_str = str(_instancia_tarea.fecha_limite).split(' ')
            _fh_format = _fh_str[0]
            
        except:
            
            _fh_str = None
            _fh_format = None
        
        _result = {
            'accion': _accion,
            'categorias': _categorias,
            'prioridades': _prioridades,
            'pk_prioridad': _instancia_tarea.id_prioridad.pk,
            'pk_categoria': _instancia_tarea.id_categoria.pk,
            'descripcion': _instancia_tarea.descripcion,
            'fecha_limite': _fh_format
        }
        
        return render (request, _pagina, _result)
        
    except Exception as e:
        _log.error(f"Error al intentar modificar la tarea. {str(e)}")
        return HttpResponse(status=500)


@login_required(login_url=LOGIN_PAGE)
def finalizar_tarea(request):
            
    try:
        
        _pk_tarea = request.POST['id_tarea']
        _check = request.POST['check']
    
        _result = tolist_controller.actualizar_estado_tarea(_pk_tarea, _check)
        
        if _result.find("Error").__eq__(0):
            
            return HttpResponse(status=500)
        
        else:

            return HttpResponse(status=200)
        
    except Exception as e:
        _log.error(f"Error al actualizar el estado de la tarea. {str(e)}")
        return HttpResponse(status=500)