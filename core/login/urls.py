from django.urls import path
from core.login.views import *

urlpatterns = [
    # utilizo la de LoginView
    path('',LoginFormView.as_view(),name='login'),
    # ese next_page es para decirle a donde mandarlo cuando cierre la sesión, si no se lo pongo, me manda a una url por defecto que tiene
    #puedo pasarle el parametro next_page o configurar la variable LOGOUT_REDIRECT_URL en el settings, que va a buscar esa variable como segunda opción si no le paso en next_page, y tercera opción ya la que maneja por defecto
    # path('logout/',LogoutView.as_view(),name='logout'),
    path('logout/',LogoutRedirectView.as_view(),name='logout'),
]