from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.register_view),
    path('login/', views.login_view, name='loginpage')
    
]
