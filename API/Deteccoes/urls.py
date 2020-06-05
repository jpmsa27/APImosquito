from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detecdados', views.detecdados, name='detecdados'),
    path('dadosjson', views.dadosjson, name='dadosjson'),
    path('oprojeto', views.oprojeto, name='oprojeto'),
    path('github',views.github, name='github')
]