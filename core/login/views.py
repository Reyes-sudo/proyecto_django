from django.shortcuts import redirect
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
import config.settings as settings

class LoginFormView(LoginView):
  #no le ponemos el form_class porque si inspeccionamos el LoginView ya viene con el form_class del AuthenticationForm
  template_name = 'login.html'

  def dispatch(self, request, *args, **kwargs):
    #si ya esta autenticado, lo redirecciono a la vista de category_list
    if request.user.is_authenticated:
      #se lo pongo por si lo quiero cambiar, solo cambio en el settings
      return redirect(settings.LOGIN_REDIRECT_URL)
    #de lo contrario, que entre normal al login
    return super().dispatch(request, *args, **kwargs)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Iniciar sesión'
    return context

class LogoutRedirectView(RedirectView):
  #le digo a donde lo va a redireccionar cuando cierre la sesión
  pattern_name = 'login'

  def dispatch(self, request, *args, **kwargs):
    #como la vista solo redirecciona, entonces en el dispatch aplico el cierre de sesión con la función logout solo pasandole el request
    logout(request)
    return super().dispatch(request, *args, **kwargs)
  # asi esta vista me redirecciona al login y cierra la sesión