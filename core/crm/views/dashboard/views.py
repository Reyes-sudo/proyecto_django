from django.db.models.functions import Cast
from datetime import datetime
import calendar

from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.db.models import FloatField
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from core.crm.models import Producto

from random import randint

meses_espanol = {
        1: 'enero',
        2: 'febrero',
        3: 'marzo',
        4: 'abril',
        5: 'mayo',
        6: 'junio',
        7: 'julio',
        8: 'agosto',
        9: 'septiembre',
        10: 'octubre',
        11: 'noviembre',
        12: 'diciembre',
    }

class DashboardView(TemplateView):
    template_name= 'dashboard.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'get_grafico_venta_mes':
                data = {
                    'name': 'Precio de venta',
                    'showInLegend': False,
                    'colorByPoint': True,
                    'data': self.get_grafico_venta_mes()
                }
            elif action == 'get_grafico_producto_venta_mes':
                valoresG=self.get_grafico_producto_venta_mes()
                data = {"chart":{
                    'name': 'Porcentaje',
                    'colorByPoint': True,
                    'data': valoresG[0],
                },
                "mes":meses_espanol[valoresG[1]],
                "anio":valoresG[2]

                    
                }
            elif action == 'get_grafico_online':
                data = {'y': randint(1, 100)}
                print(data)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['panel']='Panel de administrador'
        produ=Producto.objects.filter(stock__lt=6)
        context['alert_produ']={"vali":True if produ.exists() else False,"produ": produ }
        return context