from django.urls import path
from .views import AccRegisterView

urlpatterns = [
    path('register/', AccRegisterView.as_view(), name='register'),

]
