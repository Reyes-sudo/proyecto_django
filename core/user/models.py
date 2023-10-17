import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import model_to_dict
from config.settings import MEDIA_URL, STATIC_URL, STATIC_URL_AZURE
from core.crm.models import Empresa, Sede

class User(AbstractUser):
    email=models.EmailField(unique=True,verbose_name="Email")
    image = models.ImageField(upload_to='users/%Y/%m/',null=True, blank=True, verbose_name="Imagen")
    sede=models.ForeignKey(Sede,on_delete=models.PROTECT,null=True,blank=True)
    empresa=models.ForeignKey(Empresa,on_delete=models.PROTECT,null=True,blank=True)
    
    def get_image(self):
        if self.image:
            return f'/{MEDIA_URL}{self.image}' if not "WEBSITE_HOSTNAME" in os.environ else f'{STATIC_URL_AZURE}/{MEDIA_URL}{self.image}'
        return f'{STATIC_URL}media/img/empty.png' if not "WEBSITE_HOSTNAME" in os.environ else f'{STATIC_URL_AZURE}{STATIC_URL}media/img/empty.png'
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'user_permissions', 'last_login'])
        item['username']=self.username 
        item["image"]=self.get_image()
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['groups']=[group.name for group in self.groups.all()]
        item["sede"]=self.sede.nombre if self.sede else "No aplica"
        item["empresa"]=self.empresa.nombre if self.empresa else "No aplica"
        return item