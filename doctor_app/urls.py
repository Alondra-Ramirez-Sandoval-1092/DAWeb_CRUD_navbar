from django.urls import path
from doctor_app import views
urlpatterns = [
    path("doctor", views.inicio_vistaDoctor, name="doctor"),
    path("registrarDoctor/",views.registrarDoctor,name="registrarDoctor"),
    path("seleccionarDoctor/<id_doctor>",views.seleccionarDoctor,name="seleccionarDoctor"),
    path("editarDoctor/",views.editarDoctor,name="editarDoctor"),
    path("borrarDoctor/<id_doctor>",views.borrarDoctor,name="borrarDoctor")
]