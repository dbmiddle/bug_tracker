from django.urls import path

from tracker import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview),
    path('submitticket/', views.submitticket),
    path('ticket/<int:ticketdetail_id>/', views.ticketdetail, name='ticketdetail'),
    path('ticket/edit/<int:id>/', views.ticketedit),
    path('userdetails/<int:user_id>/', views.userdetails),
    path('ticket/<int:id>/assign', views.assignticket),
    path('ticket/<int:id>/complete', views.completeticket),
    path('ticket/<int:id>/invalid', views.invalidticket)
]
