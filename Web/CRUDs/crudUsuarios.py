from Web.models import usuario
from datetime import datetime





def CreateUser(user,passw,esAdmin):
     try :
         usuario.objects.get(usuario = user).usuario
         return True
     except:
         date = datetime.now()
     
         fechaCreacion = str(date.year) + "-" + str(date.month) + "-" + str(date.day)
         newUser = usuario(usuario= user,password = passw, fechaCreacion = fechaCreacion, esAdmin = esAdmin)
         newUser.save()
         return False
     
          

def EliminarUser(id):
     try:

       delete = usuario.objects.get(idU = id)
       delete.delete()
       return True
     except:
       return False

def ListarUser():
   Lista = []
   select =  usuario.objects.all()
   for user in select:
        Lista.append([user.usuario,user.correo,user.edad,user.fechaCreacion,user.esAdmin,user.idU])
   return Lista

def esAdmin(user):
     return usuario.objects.get(usuario = user).esAdmin
    
def modificarUser(id,user,passw,esAdmin):
     try:   
       usuario1 =usuario.objects.get(usuario = id)
       usuario1.usuario = user
       usuario1.password = passw
       usuario1.esAdmin = esAdmin
       usuario1.save()
       return True
     except:
      return False



def buscar(text):
   Lista = []
   select =  usuario.objects.all()
   for user in select:
       paso = False
       if text in  str(user.nombreUser):
          paso = True
       elif text in str(user.usuario):
          paso = True
       elif text in str(user.apellidos):
          paso = True
       if paso:     
          Lista.append([user.usuario,user.correo,user.edad,user.fechaCreacion,user.esAdmin,user.idU])
   return Lista



