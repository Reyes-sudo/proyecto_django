import os
from django.db import models
from django.forms import model_to_dict
from core.models import BaseModel
from crum import get_current_user
from config.settings import MEDIA_URL, STATIC_URL, STATIC_URL_AZURE

class Categoria(BaseModel):
    nombre = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    descripcion = models.CharField(max_length=500, null=True,blank=True,verbose_name='Descripción')

    #si se auto completa con visual, los campos deben quedar asi, no utilizando ":" sino los "=" (error mio que vi)
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # hasta si necesito algo del request, puedo obtenerlo aqui con crum, y su funcion get_current_request()
        user = get_current_user()
        #si el usuario no esta vacio
        if user is not None:
          #si existe un pk o id, significa que se esta creando el registro, de lo contrario, se esta actualizando el registro
          if not self.pk:
              self.user_creation=user
          else:
              self.user_updated=user
        super(Categoria, self).save()

        
    def __str__(self):
        return f'{self.nombre}'
    
    def toJSON(self):
      #podria crear el diccionario manual pero donde tenga muchos atributos seria mala practica, ya django tiene una funcion para ello
      #puedo pasarle un arreglo en el parametro exclude con el nombre de los campos que no quiera que se retornen
      # puedo excluir valores del diccionario que genera el model_to_dict 
      item = model_to_dict(self, exclude=['user_creation','user_updated'])
      return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Producto(BaseModel):
    nombre = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,verbose_name='Categoria')
    imagen = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True,verbose_name='Imagen')
    stock=models.IntegerField(default=0, verbose_name='Stock')
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2,verbose_name='Precio de venta')

    def toJSON(self):
        item = model_to_dict(self)
        item['full_name']='{} / {}'.format(self.nombre, self.categoria.nombre)
        item['categoria']={"id":self.categoria.id,"nombre":self.categoria.nombre}
        item['imagen']=self.get_image()
        item['precio']=format(self.precio, '.2f')
        return item

    def get_image(self):
        #si existe la imagen, o bueno, si se subio, le retorno la ruta que debe estar en media url, y le junto el self.image que es el nombre de la imagen
        if self.imagen:
            return f'/{MEDIA_URL}{self.imagen}' if not "WEBSITE_HOSTNAME" in os.environ else f'{STATIC_URL_AZURE}/{MEDIA_URL}{self.imagen}'
        #de lo contrario, le retorno una imagen como predeterminada que esta en mis static
        return f'{STATIC_URL}media/img/empty.png' if not "WEBSITE_HOSTNAME" in os.environ else f'{STATIC_URL_AZURE}{STATIC_URL}media/img/empty.png'

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

class Empresa(BaseModel):
  nombre=models.CharField(max_length=100,unique=True,null=False,blank=False,verbose_name="Nombre")

  def __str__(self):
     return self.nombre
  
  def toJSON(self):
    return model_to_dict(self)

  class Meta:
    verbose_name = 'Empresa'
    verbose_name_plural = 'Empresas'

class Sede(BaseModel):
  nombre=models.CharField(max_length=100,unique=True,null=False,blank=False,verbose_name="Nombre")
  empresa=models.ForeignKey(Empresa,null=False,blank=False, on_delete=models.CASCADE,verbose_name="Empresa")

  def __str__(self):
     return self.nombre
  
  def toJSON(self):
    item =model_to_dict(self)
    item["empresa"]={"id":self.empresa.id,"nombre":self.empresa.nombre}
    return item

  class Meta:
    verbose_name = 'Sede'
    verbose_name_plural = 'Sedes'

class Trabajador(BaseModel):
  nombres=models.CharField(max_length=100,null=False,blank=False,verbose_name="Nombres")
  apellidos=models.CharField(max_length=100,null=False,blank=False,verbose_name="Apellidos")
  edad=models.IntegerField(null=False,blank=False,verbose_name="Edad")
  direccion=models.CharField(max_length=200,null=False,blank=False,verbose_name="Dirección")
  correo=models.EmailField(verbose_name="Correo")
  curriculum_vitae=models.CharField(max_length=200,null=False,blank=False,verbose_name="Curriculum Vitae")
  sede=models.ForeignKey(Sede,on_delete=models.CASCADE,null=False,blank=True,verbose_name="Sede")

  def nombres_completos(self):
     return f'{self.nombres} {self.apellidos}'

  def __str__(self):
     return self.nombres_completos()
  
  def toJSON(self):
    item=model_to_dict(self)
    item["sede"]=self.sede.toJSON()
    return item

  class Meta:
    verbose_name = 'Trabajador'
    verbose_name_plural = 'Trabajadores'