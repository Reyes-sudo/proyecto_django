from django.contrib import admin
from core.crm.models import *

# Registrar los modelos en el admin para que aparezcan en el administrador de django
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Sede)
admin.site.register(Trabajador)
admin.site.register(Empresa)