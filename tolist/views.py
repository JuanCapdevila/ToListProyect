from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

import logging

log = logging.getLogger("admMedical")


# Create your views here.

@csrf_exempt
def log_in(request):
    context = RequestContext(request)
    
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            messages.add_message(request, messages.ERROR, "Por favor complete todos los campos")
            return HttpResponse(status=301)
        else:
            
            try:
                user = User.objects.get(username=username)
            
            except Exception as e:
                log.error(str(e))
                
                messages.add_message(request, messages.ERROR, "Usuario y/o contraseña incorrecta")
                
                return render (request ,'login/login.html', context.flatten())
                return HttpResponse(status=300)
            
            user = authenticate(username=username,password=password)
            
            if user:
                
                if user.is_authenticated:
                    login(request, user)
                
                    user = User.username
                    messages.add_message(request, messages.SUCCESS, "Bienvenido {}".format(user))
                    
                    return HttpResponse(status=200)
                
                else:
                    messages.add_message(request, messages.ERROR, "Error con el usuario. Comunicarse con administrador")
                    return HttpResponse(status=302)
    
    return render (request,'login/login.html', context.flatten())

@csrf_exempt
def log_out(request):
    
    logout(request)
    
    context = RequestContext(request)
    
    messages.add_message(request, messages.SUCCESS, 'Sesión finalizada')

    return HttpResponse(status=200)