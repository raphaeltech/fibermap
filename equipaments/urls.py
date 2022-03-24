from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'equipaments'

urlpatterns = [
    path('admin/', admin.site.urls),

    # Router for Boxs
    path('cadastrar/caixa/', createBox.as_view(), name="cadastrarcaixa"), 
    path('editar/caixa/<int:pk>', updateBox.as_view(), name="editarcaixa"),
    path('excluir/caixa/<int:pk>', deleteBox.as_view(), name="excluircaixa"),
    path('listar/caixas', listBox.as_view(), name="listarcaixas"),
    # Router for Cables
    path('cadastrar/cabo/', createCable.as_view(), name="cadastrarcabo"), 
    path('editar/cabo/<int:pk>', updateCable.as_view(), name="editarcabo"),
    path('excluir/cabo/<int:pk>', deleteCable.as_view(), name="excluircabo"),
    path('listar/cabos/', listCable.as_view(), name="listarcabos"),
    # Router for Polse
    path('cadastrar/poste/', createPole.as_view(), name="cadastrarposte"), 
    path('editar/poste/<int:pk>', updatePole.as_view(), name="editarposte"),
    path('excluir/poste/<int:pk>', deletePole.as_view(), name="excluirposte"),
    path('listar/poste/', listPole.as_view(), name="listarpostes"),
    # Router for Steels
    path('cadastrar/ferragem/', createSteel.as_view(), name="cadastrarferragem"), 
    path('editar/ferragem/<int:pk>', updateSteel.as_view(), name="editarferragem"),
    path('excluir/ferragem/<int:pk>', deleteSteel.as_view(), name="excluirferragem"),
    path('listar/ferragens/', listSteel.as_view(), name="listarferragens"),
    # Router for Spliters
    path('cadastrar/spliter/', createSpliter.as_view(), name="cadastrarspliter"), 
    path('editar/spliter/<int:pk>', updateSplite.as_view(), name="editarspliter"),
    path('excluir/spliter/<int:pk>', deleteSpliter.as_view(), name="excluirspliter"),
    path('listar/spliters/', listSpliter.as_view(), name="listarspliters"),

]