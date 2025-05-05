from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='lista-libros'),
    path('nuevo/', views.agregar_libro, name='agregar-libro'),
    path('<int:pk>/', views.detalle_libro, name='detalle-libro'),
    path('<int:pk>/editar/', views.editar_libro, name='editar-libro'),
    path('<int:pk>/eliminar/', views.eliminar_libro, name='eliminar-libro'),
]
