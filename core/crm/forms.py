from django.forms import ModelForm,Select,TextInput, Textarea,NumberInput,EmailInput

from core.crm.models import Categoria, Producto, Sede, Trabajador,Empresa

class CategoriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #for form in self.visible_fields():
            #form.field.widget.attrs['class']= 'form-control'
            #form.field.widget.attrs['autocomplete']= 'off'
        self.fields['nombre'].widget.attrs['autofocus']= True


    class Meta:
        model=Categoria
        fields='__all__'
        widgets={
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'placeholder': 'Ingrese una descripción',
                    'rows':3,
                    'cols':3
                }
            )
        }
        exclude=['user_creation','user_updated']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class ProductoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
        }
        exclude=['user_creation','user_updated']
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class TrabajadorForm(ModelForm):
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['nombres'].widget.attrs['autofocus']= True

  class Meta:
    model=Trabajador
    fields="__all__"
    widgets={
        "nombres":TextInput(attrs={
            "placeholder":"Ingrese los nombres"
        }),
        "apellidos":TextInput(attrs={
            "placeholder":"Ingrese los apellidos"
        }),
        "edad":NumberInput(attrs={
            "placeholder":"Ingrese la edad"
        }),
        "direccion":TextInput(attrs={
            "placeholder":"Ingrese la dirección"
        }),
        "correo":EmailInput(attrs={
            "placeholder":"Ingrese el correo electrónico"
        }),
        "curriculum_vitae":TextInput(attrs={
            "placeholder":"Ingrese el curriculum vitae"
        })
    }
    exclude=['user_creation','user_updated']

  def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
class EmpresaForm(ModelForm):
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['nombre'].widget.attrs['autofocus']= True

    class Meta:
        model=Empresa
        widgets={
            "nombre":TextInput(
                attrs={"placeholder":"Ingrese el nombre"}
            )
        }
        fields="__all__"
        exclude=['user_creation','user_updated']
    
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    

class SedeForm(ModelForm):
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['nombre'].widget.attrs['autofocus']= True

    class Meta:
        model=Sede
        widgets={
            "nombre":TextInput(
                attrs={"placeholder":"Ingrese el nombre"}
            )
        }
        fields="__all__"
        exclude=['user_creation','user_updated']
    
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data