from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    # path('st/', views.Student_form, name='student'),
    # path('', views.Teacher_form, name='teacher'),
    
    
]