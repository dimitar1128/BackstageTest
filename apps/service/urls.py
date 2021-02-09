from django.urls import path
from .views import *
from .controllers import *

urlpatterns = [
    path('difference', get_diff, name='get-diff'),
]