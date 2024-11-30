from django.urls import path, include
from . import views

app_name = "user"

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.login_, name="login"),
    path('login_out/', views.login_out, name="login_out"),
    path("chat/", views.chat, name="chat"),
    path("chat/<int:id>/<str:user>/", views.conv, name="chat"),
]