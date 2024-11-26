from django.urls import path
from habitacion_app import views
urlpatterns = [
    path("habitacion", views.inicio_vistaHabitacion, name="habitacion"),
    path("registrarHabitacion/",views.registrarHabitacion,name="registrarHabitacion"),
    path("seleccionarHabitacion/<id_habitacion>",views.seleccionarHabitacion,name="seleccionarHabitacion"),
    path("editarHabitacion/",views.editarHabitacion,name="editarHabitacion"),
    path("borrarHabitacion/<id_habitacion>",views.borrarHabitacion,name="borrarHabitacion")
]