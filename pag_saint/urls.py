from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("burgers/", views.burgers, name="burgers"),
    path("contacto/", views.contacto, name="contacto"),
    path("reservas/", views.reservas, name = "reservas"),
]