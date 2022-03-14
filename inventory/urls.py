from django.urls import path
from .views import *

app_name = 'inventory'

urlpatterns = [
    # Router for CEO
    path('listar-ceos/',list_ceo,name='listar-ceos'),
    path('posicionar-ceo/',position_ceo,name="posicionar-ceo"),
    path('editar-ceo/<int:id>/',update_ceo,name='editar-ceo'),
    path('excluir-ceo/<int:id>/',delete_ceo,name='excluir-ceo'),
    # Router for CTO
    path('listar-ctos/',list_cto,name='listar-ctos'),
    path('posicionar-cto/',position_cto,name="posicionar-cto"),
    path('editar-cto/<int:id>/',update_cto,name='editar-cto'),
    path('excluir-cto/<int:id>/',delete_cto,name='excluir-cto'),
    # Router for Steel
    path('listar-ferragens/',list_steel,name='listar-ferragens'),
    path('posicionar-ferragem/',position_steel,name="posicionar-ferragem"),
    path('editar-position-ferragem/<int:id>/',update_steel,name='editar-position-ferragem'),
    path('excluir-position-ferragem/<int:id>/',delete_steel,name='excluir-position-ferragem'),
    # Router for Pole
    path('listar-postes/',list_pole,name='listar-postes'),
    path('posicionar-poste/',position_pole,name="posicionar-poste"),
    path('editar-position-poste/<int:id>/',update_pole,name='editar-position-poste'),
    path('excluir-position-poste/<int:id>/',delete_pole,name='excluir-position-poste'),

]