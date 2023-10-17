from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.crm.mixins import ValidatePermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from core.crm.forms import SedeForm
from core.crm.models import Sede


class SedeListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Sede
    template_name = 'sede/list.html'
    permission_required = 'crm.view_sede'
    
    def post(self, request, *args, **kwargs):
        data={}
        try:
            action=request.POST['action']
            if action =='searchdata':
                data=[]
                for i in Sede.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] ='Ha ocurrido un error'
        except Exception as e:
            data={}
            data['error']=str (e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Sedes'
        context['create_url'] = reverse_lazy('crm:sede_create')
        context['list_url'] = reverse_lazy('crm:sede_list')
        context['entity'] = 'Sedes'
        return context


class SedeCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Sede
    form_class = SedeForm
    template_name = 'sede/create.html'
    success_url = reverse_lazy('crm:sede_list')
    permission_required = 'crm.add_sede'
    url_redirect = success_url

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data={}
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una Sede'
        context['entity'] = 'Sedes'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class SedeUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Sede
    form_class = SedeForm
    template_name = 'sede/create.html'
    success_url = reverse_lazy('crm:sede_list')
    permission_required = 'crm.change_sede'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data={}
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de una Sede'
        context['entity'] = 'Sedes'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class SedeDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Sede
    template_name = 'sede/delete.html'
    success_url = reverse_lazy('crm:sede_list')
    permission_required = 'crm.delete_sede'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una Sede'
        context['entity'] = 'Sedes'
        context['list_url'] = self.success_url
        return context
