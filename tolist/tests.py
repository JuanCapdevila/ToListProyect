from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

class ModeloTareaTestCase(TestCase):

    #Creamos data para el test case
    def setUp(self):
        self.user = User.objects.create_user(username='usertest', email='usertest@test.com', password='testpassword')
        self.prioridad = Prioridades.objects.create(descripcion='Alta')
        self.categoria = Categorias.objects.create(descripcion='Trabajo')
        self.tarea = Tareas.objects.create(descripcion='Hacer un test case', id_user=self.user, id_prioridad=self.prioridad, id_categoria=self.categoria)

    #Prueba de la tarea creada
    def test_tarea_creada(self):
        tarea = self.tarea
        self.assertTrue(isinstance(tarea, Tareas))
        self.assertEqual(tarea.__str__(), tarea.descripcion)

    #Prueba para editar una tarea
    def test_tarea_editar(self):
        tarea = self.tarea
        tarea.descripcion = 'Tarea editada'
        tarea.estado = 2
        tarea.save()
        updated_tarea = Tareas.objects.get(id=tarea.id)
        self.assertEqual(updated_tarea.descripcion, 'Tarea editada')
        self.assertEqual(updated_tarea.estado, 2)
    
    #Prueba para eliminar una tarea
    def test_tarea_eliminar(self):
        tarea = self.tarea
        tarea.delete()
        with self.assertRaises(Tareas.DoesNotExist):
            Tareas.objects.get(id=tarea.id)

