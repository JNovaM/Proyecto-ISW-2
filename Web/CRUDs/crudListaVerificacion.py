from Web.models import listaVerificacion
from datetime import datetime
from Web.CRUDs import crudPreguntas
from Web.models import PUL
from Web.models import usuario



def CreateLista(preguntas, requisito, nombre):
     try :
         listaVerificacion.objects.get(nombreLV = nombre).nombreLV
         return True
     except:
      date = datetime.now()
     
      fechaCreacion = str(date.year) + "-" + str(date.month) + "-" + str(date.day)
      newLista = listaVerificacion( nombreLV = nombre, fechaCreacion = fechaCreacion, requisitoCalidad = requisito)
      newLista.save()
      
      for pregunta in preguntas:
         idlv = listaVerificacion.objects.get(nombreLV = nombre)
        
         No = int(pregunta[0].split('.')[0])
         pregunta1 = pregunta[1]
         respuesta = pregunta[2]
         observ = pregunta[3]
         tipo = pregunta[4]
         crudPreguntas.Createpregunta(idlv,No,pregunta1,respuesta,observ,tipo)
      return False


def EliminarListaV(id):
    try:
      delete = listaVerificacion.objects.get(idLV = id)
      delete.delete()
      return True
    except:
      return False

def ListarListas():
   Lista = []
   select =  listaVerificacion.objects.all()
   for lista in select:
        Lista.append([lista.idLV,lista.nombreLV,lista.requisitoCalidad])
   return Lista

def ListarRev(user):
   Lista = []
   select =  listaVerificacion.objects.all()
   idUR =usuario.objects.get(usuario = user)
   for lista in select:
      try:
        rev = PUL.objects.get(idU = idUR ,idLV = lista.idLV).idLV
        Lista.append([lista.idLV,lista.nombreLV,lista.requisitoCalidad])
      except:
         print('nada')
   return Lista


def buscar(text):
   Lista = []
   select =  listaVerificacion.objects.all()
   for lista in select:
       paso = False
       if text.lower() in  str(lista.nombreLV).lower():
          paso = True
       elif text.lower() in str(lista.requisitoCalidad).lower():
          paso = True
     
       if paso:     
          Lista.append([lista.idLV,lista.nombreLV,lista.requisitoCalidad])
   return Lista