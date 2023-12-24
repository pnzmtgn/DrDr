from django.urls import path, include
from .views import List, cardio_list, hemato_list
urlpatterns = [
    path('', List_html),
    path('Dermatology/', include('Dermatology.urls')),
    path('Pulmonology/',include('Pulmonology.urls')),
    path('Neurology/',include('Neurology.urls')),
    path('Nephrology/',include('Nephrology.urls')),
    path('Hematology/',hemato_list),
    path('Cardiology/',cardio_list)
]


# urlpatterns = [
#     path('list', list, name='list'),
    
#     path('test-list', test_list, name='test_list'),
#     path('list2', list2, name='list2'),
#     path('<str:code>', detail, name='detail'),
