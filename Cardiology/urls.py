from django.urls import path
from .views import List, List_html

urlpatterns = [
    path('', Cardio_List)
]