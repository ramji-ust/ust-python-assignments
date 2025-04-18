from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('info/', views.info, name='info'),  # Add a URL pattern for the info page
    path('index/', views.index, name='index'),
    path('check_age/', views.check_age, name='check_age'),
    path('fruit_list/', views.fruit_list, name='fruit_list'),
    path('input', views.input_form, name='input'), # 127.0.0.1:8000/input
    path('result', views.result, name='result'), # 127.0.0.1:8000/result
    path('converter', views.currency_converter, name='currency_converter'),
    path('timer/', views.timer_view, name='timer'),
    
]  
