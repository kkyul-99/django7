from django.urls import path,include
from . import views

app_name='member'
urlpatterns = [
    # html로 리턴
    path('step03/', views.step03, name='step03'),
    
    # JSON으로 리턴: id가 존재하는지 체크
    path('idCheck/', views.idCheck, name='idCheck'),
]
