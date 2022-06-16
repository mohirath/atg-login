from django.urls import path
from .views import home, profile,main, RegisterView

urlpatterns = [
    path('', main, name='main'),
    path('home/', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
]
