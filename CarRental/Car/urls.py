from django.urls import path
from .import views

urlpatterns = [
    path("AddCar",views.AddCar,name="AddCar"),
    path("CarViewMerchant",views.CarViewMerchant,name="CarViewMerchant"),
    path("DeleteCar/<int:pk>",views.DeleteCar,name="DeleteCar"),
    path("UpdateCar/<int:pk>",views.UpdateCar,name="UpdateCar"),
    path("ViewCar/<int:pk>",views.ViewCar,name="ViewCar")
]
