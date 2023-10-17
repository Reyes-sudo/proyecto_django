from core.user.models import User

user=User(username="yoiner")
user.set_password("YoyoDR.2003")
user.is_superuser=True
user.is_staff=True
user.is_active=True
user.save()
print("Usuario creado: ",user)