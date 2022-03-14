from unicodedata import name
from django.urls import path
from .views import *

app_name = 'equipaments'

urlpatterns = [
    path('listar-caixas/', list_boxs, name='listar-caixas'),
    path('cadastrar-caixa/', create_box, name='cadastrar-caixa'),
    path('editar-caixa/<int:id>/',update_box,name="editar-caixa"),
    path('excluir-caixa/<int:id>',delete_box,name="excluir-caixa"),
    path('listar-cabos/', list_cables, name='listar-cabos'),
    path('cadastrar-cabo/', create_cable, name='cadastrar-cabo'),
    path('editar-cabo/<int:id>/',update_cable,name='editar-cabo'),
    path('excluir-cabo/<int:id>',delete_cable,name='excluir-cabo'),
    path('listar-postes/', list_poles, name='listar-postes'),
    path('cadastrar-poste/', create_pole, name='cadastrar-poste'),
    path('editar-poste/<int:id>/',update_pole,name='editar-poste'),
    path('excluir-poste/<int:id>',delete_pole,name='excluir-poste'),
    path('listar-ferragens/', list_steels, name='listar-ferragens'),
    path('cadastrar-ferragem/', create_steel, name='cadastrar-ferragem'),
    path('editar-ferragem/<int:id>/',update_steel,name='editar-ferragem'),
    path('excluir-ferragem/<int:id>',delete_steel,name='excluir-ferragem'),
    path('listar-spliters/', list_spliters, name='listar-spliters'),
    path('cadastrar-spliter/', create_spliter, name='cadastrar-spliter'),
    path('editar-spliter/<int:id>/',update_spliter,name='editar-spliter'),
    path('excluir-spliter/<int:id>',delete_spliter,name='excluir-spliter'),
]