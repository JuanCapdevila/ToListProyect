import logging

from django.http import HttpResponse

from tolist.models import *

_log = logging.getLogger("admMedical")

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
        
        _resultado = "Tarea creada con exito"
            
    except Exception as e:
        _log.error(f"Error al crear tarea. {str(e)}")
        _resultado = f"Error al crear tarea. {str(e)}"
        return _resultado

    return _resultado