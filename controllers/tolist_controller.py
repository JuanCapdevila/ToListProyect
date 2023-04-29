import logging

from django.http import HttpResponse

from tolist.models import *

_log = logging.getLogger("tolist")

def crear_tarea(_descripcion, _prioridad, _categoria, _fh_limite, _user):
    
    _resultado = None
    
    try:
          
        #Obtenemos las instancias
        try:
            
            _inst_prioridad = Prioridades.objects.get(pk = _prioridad)
            
        except Exception as e:
            _log.error(f"Error al obtener la instancia de prioridad en crear tarea. {str(e)}")
            _resultado = f"Error al obtener la instancia de prioridad en crear tarea. {str(e)}"
            return _resultado

        try:
            
            _inst_categoria = Categorias.objects.get(pk = _categoria)
            
        except Exception as e:
            _log.error(f"Error al obtener la instancia de categoria en crear tarea. {str(e)}")
            _resultado = f"Error al obtener la instancia de categoria en crear tarea. {str(e)}"
            return _resultado
        
        if _fh_limite.__eq__(''):
            _fh_limite = None
        
        Tareas.objects.create(descripcion = _descripcion,
                                id_prioridad = _inst_prioridad,
                                id_categoria = _inst_categoria,
                                fecha_limite = _fh_limite,
                                id_user = _user)
        
        _log.info(f"Tarea creada con exito. {_descripcion}")
        _resultado = "Tarea creada con exito"
            
    except Exception as e:
        _log.error(f"Error al crear tarea. {str(e)}")
        _resultado = f"Error al crear tarea. {str(e)}"
        return _resultado

    return _resultado


def editar_tarea(_pk, _descripcion, _prioridad, _categoria, _fh_limite):
    
    _resultado = None
    
    try:
          
        #Obtenemos la instancia a editar
        try:
            
            _instancia_tarea = Tareas.objects.get(pk = _pk)
            
        except Exception as e:
            _log.error(f"Error al obtener la instancia de tarea en modificar tarea. {str(e)}")
            _resultado = f"Error al obtener la instancia de tarea en modificar tarea. {str(e)}"
            return _resultado
        
        if _fh_limite.__eq__(''):
            _fh_limite = None
            
        #Obtenemos las instancias
        try:
            
            _inst_prioridad = Prioridades.objects.get(pk = _prioridad)
            
        except Exception as e:
            _log.error(f"Error al obtener la instancia de prioridad en modificar tarea. {str(e)}")
            _resultado = f"Error al obtener la instancia de prioridad en modificar tarea. {str(e)}"
            return _resultado

        try:
            
            _inst_categoria = Categorias.objects.get(pk = _categoria)
            
        except Exception as e:
            _log.error(f"Error al obtener la instancia de categoria en modificar tarea. {str(e)}")
            _resultado = f"Error al obtener la instancia de categoria en modificar tarea. {str(e)}"
            return _resultado
            
        _instancia_tarea.descripcion = _descripcion
        _instancia_tarea.id_prioridad = _inst_prioridad
        _instancia_tarea.id_categoria = _inst_categoria
        _instancia_tarea.fecha_limite =  _fh_limite
        _instancia_tarea.save()
        
        _log.info(f"Tarea modificada con exito. {_descripcion}")
        _resultado = "Modificacion realizada correctamente"
            
    except Exception as e:
        _log.error(f"Error al modificar la tarea. {str(e)}")
        _resultado = f"Error al modificar la tarea. {str(e)}"
        return _resultado

    return _resultado


def actualizar_estado_tarea(_pk_tarea, _check):
    
    _resultado = None
    
    try:
          
        #Obtenemos la instancia a actualizar
        try:
            
            _instancia_tarea = Tareas.objects.get(pk = _pk_tarea)
            
        except Exception as e:
            _log.error(f"Error al obtener la instancia de tarea en actualizar tarea. {str(e)}")
            _resultado = f"Error al obtener la instancia de tarea en actualizar tarea. {str(e)}"
            return _resultado
        
        if int(_check).__eq__(1):
            
            _instancia_tarea.estado = 0
            
        else:
            
            _instancia_tarea.estado = 1
        

        _instancia_tarea.save()
    
        _log.info(f"Tarea actualizada con exito. {_instancia_tarea.descripcion}, Estado:{_instancia_tarea.estado}") 
        _resultado = "Tarea actualizada con exito"
            
    except Exception as e:
        _log.error(f"Error al actualizar tarea. {str(e)}")
        _resultado = f"Error al actualizar tarea. {str(e)}"
        return _resultado

    return _resultado