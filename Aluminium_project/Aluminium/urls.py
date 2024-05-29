from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login),
    path('register/',views.registerpage),
    path('homepage/<int:id>/',views.homepage),
    path('pending/',views.pending),
    path('approve/<int:id>/',views.approve),
    path('editpage/',views.editpage),
    path('edit/<int:id>',views.edit),
    path('delete/<int:id>',views.delete),
    path('approved/',views.approvedlist),
    path('adminlogin/',views.adminlogin),
    path('',views.enter),
    path('profile/<int:id>',views.profile)
]