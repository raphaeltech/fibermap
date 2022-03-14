from django.conf import settings
from django.urls import path 
from .views import  *
from django.conf.urls.static import static


app_name = "users"


urlpatterns = [
   	# Login, Register, Forgot password, Logout
    path('login/', LoginView, name="login_url"),
    path('register/',RegisterView, name="register_url"),
    path('forgot-password/',ForgotPasswordView, name="forgot_password_url"),
    path('logout/',LogoutView, name="logout_url"),

    path('charts/',ChartsView, name="charts_url"),

    path('tables/',TablesView, name="tables_url"),

    path('buttons/',ButtonsView, name="buttons_url"),

    path('cards/',CardsView, name="cards_url"),

	path('page_not_found/',PageNotFoundView, name="page_not_found_url"),    

	path('blank/',BlankView, name="blank_page_url"),    

	# Utilities
	path('colors/',ColorsView, name="colors_url"),    

	path('borders/',BordersView, name="borders_url"),    

	path('animations/',AnimationsView, name="animations_url"),    

	path('others/',OthersView, name="others_url"),


    # Fibermap em uso

    path('mapaHome/',mapHomeView, name="mapHome"), 
    path('cadastrar-usuario/', registerUser, name="cadastrar-usuario"),
    path('lista-de-usuarios/',lisUsers,name="lista-de-usuarios"),
    path('editar-usuario/<int:id>/',updateUser,name="editar-usuario"),
    #path('cadastrar-tipos-de-usuarios/',registerTypeUser,name="cadastrar-tipos-de-usuarios"),
    #path('cadastrar-empresa/',registerCompany,name="cadastrar-empresa"),  

]

