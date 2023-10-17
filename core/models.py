# creo este archivvo, porque mis modelos tendran los mismos valores, entonces lo creo aqui para que también lo hereden
from django.conf import settings
from django.db import models

class BaseModel(models.Model):
    # como tengo el usuario personalizado, si voy a realizar una relación, lo hago con ese modelo llamando la variable de la configuración
    # aveces hay problemas con el nombre de la tabla al utilizar el AUTH_USER para la relacion, asi que le puedo poner el nombre, y lo pongo de esa forma para que cambie segun la clase y no haya problema al poner uno repetido
    user_creation = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='%(app_label)s_%(class)s_creation')

    user_updated = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='%(app_label)s_%(class)s_updated')

    date_creation = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    #le pongo valores nulos porque al inicio no va a tener ningun valor y es para que no moleste en las migraciones

    class Meta:
        #le pongo este valor para decirle que no se ponga en la base de datos, sino que sera una clase para implementar en mis modelos
        abstract = True