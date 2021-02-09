from django.urls import path
from .views import *
from .controllers import *

urlpatterns = [
    path('', HomeView.as_view(), name='home-view'),
    path('difference', get_diff, name='get-diff'),
]