from django.urls import include, path
from account.views import register, login_view

urlpatterns = [
    path('register/',  register, name="register"),
    path('login/',  login_view, name="login")
]