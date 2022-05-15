from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='indexpage'),
    path('allusers/',views.allusers,name='allusers'),
    
    path('addbook/',views.addbook,name='addbook'),
    path('allbook/',views.allbooks,name='allbook'),
    path('updatebook/<str:pk>/',views.updatebook,name='updatebook'),
    path('deletebook/<str:pk>/',views.deletebook,name='deletebook'),
    path('upload/',views.upload,name='upload'),

    path('deleteuser/<str:pk>/',views.deleteuser,name='deleteuser'),   
    path('updateuser/<str:pk>/',views.updateuser,name='updateuser'),    
    path('login/', views.loginuser, name="login"),
    path('logout/',views.logoutuser,name="logout"),
    path('register/',views.registeruser,name="register"),
]

