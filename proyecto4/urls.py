from django.contrib import admin
from django.urls import path

from biblioteca import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("libro/crear", views.crear_libro),
    path("libros", views.listar_libros),
    path("libro/modificar/<int:id>", views.modificar_libro),
    path("libro/eliminar/<int:id>", views.eliminar_libro),
]
