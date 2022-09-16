from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('add-contact/', views.addContact, name="add-contact"),
    path('profile/<int:pk>/', views.contactProfile, name='profile'),
    path('edit/<int:pk>/', views.editProfile, name="edit"),
    path('delete/<int:pk>/', views.deleteProfile, name="delete"),
]
