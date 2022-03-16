from django.urls import path
from django.contrib import admin
from .views import *

app_name = 'inventory'

urlpatterns = [
    path('admin/', admin.site.urls),

    # Router for CEO
    path('posicionar/ceo/', createPositionCeo.as_view(), name="posicionarceo"), 
    path('editar/ceo/<int:pk>', updatePositionCeo.as_view(), name="editarceo"),
    path('excluir/ceo/<int:pk>', deletePositionCeo.as_view(), name="excluirceo"),
    path('listar/ceos', listPositionCeo.as_view(), name="listarceos"),
    # Router for CTO
    path('posicionar/cto/', createPositionCto.as_view(), name="posicionarcto"), 
    path('editar/cto/<int:pk>', updatePositionCto.as_view(), name="editarcto"),
    path('excluir/cto/<int:pk>', deletePositionCto.as_view(), name="excluircto"),
    path('listar/ctos', listPositionCto.as_view(), name="listarctos"),
    # Router for Pole
    path('posicionar/poste/', createPositionPole.as_view(), name="posicionarposte"), 
    path('editar/poste/<int:pk>', updatePositionPole.as_view(), name="editarposte"),
    path('excluir/poste/<int:pk>', deletePositionPole.as_view(), name="excluirposte"),
    path('listar/postes', listPositionPole.as_view(), name="listarpostes"),
    # Router for Steel
    path('posicionar/ferragem/', createPositionSteel.as_view(), name="posicionarferragem"), 
    path('editar/ferragem/<int:pk>', updatePositionSteel.as_view(), name="editarferragem"),
    path('excluir/ferragem/<int:pk>', deletePositionSteel.as_view(), name="excluirferragem"),
    path('listar/ferragem', listPositionSteel.as_view(), name="listarferragens"),

]