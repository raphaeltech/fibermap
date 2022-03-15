from django.conf import settings
from django.urls import path 
from .views import  *
from django.conf.urls.static import static


from django.contrib.auth import views as auth_views


app_name = "users"


urlpatterns = [
   	# Login, Register, Forgot password, Logout
    path('login/', auth_views.LoginView.as_view(
        template_name = 'login.html'
    ), name="login"),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Fibermap em uso
    path('mapaHome/',mapHomeView, name="mapHome"), 
    path('cadastrar-usuario/', registerUser, name="cadastrar-usuario"),
    path('lista-de-usuarios/',lisUsers,name="lista-de-usuarios"),
    path('editar-usuario/<int:id>/',updateUser,name="editar-usuario"),
    #path('cadastrar-tipos-de-usuarios/',registerTypeUser,name="cadastrar-tipos-de-usuarios"),
    #path('cadastrar-empresa/',registerCompany,name="cadastrar-empresa"),  

]

