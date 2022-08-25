from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('usuario', views.usuario, name='usuario'),
    path('reserva', views.reserva, name='reserva'),

    path('crear/usuario', views.crear_usuario, name='crear_usuario'),
    path('crear/reserva', views.crear_reserva, name='crear_reserva'),
    path('editar/reserva/<int:id>', views.editar_reserva, name='editar_reserva'),
    path('editar/usuario/<int:id>', views.editar_usuario, name='editar_usuario'),
    path('solicitud/reservas', views.reservas_solicitadas, name='reservas_solicitadas'),
    path('eliminaru/<int:id1>', views.eliminaru, name = 'eliminaru'),
    path('eliminarr/<int:id2>', views.eliminarr, name = 'eliminarr'),
]