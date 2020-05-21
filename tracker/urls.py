from django.urls import path

from tracker import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview),
    path('submitticket/', views.submitticket),
]
