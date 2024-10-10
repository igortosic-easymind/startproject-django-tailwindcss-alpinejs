from django.urls import path

from . import views

urlpatterns = [
    path("clients", views.get_clients, name="clients"),
    path("clients/add", views.add_client, name="client"),
    path("clients/<int:pk>/", views.view_client, name="client_view"),
    path("clients/edit/<int:pk>/", views.update_client, name="update_client"),
    path("clients/delete/<int:pk>/", views.delete_client, name="delete_client"),
]
