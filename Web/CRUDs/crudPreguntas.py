
from Web.models import preguntas
from Web.models import listaVerificacion
from datetime import datetime

def Createpregunta(id,No,pregunta1,respuesta,observ,tipo):   
      newLista = preguntas(idLV=id,No = No, preguta = pregunta1,  respuesta = respuesta,  observacion = observ,tipo = tipo)
      newLista.save()
      

def ListarPreguntas(id):
      Lista = []
      select = preguntas.objects.all()
      
      for l in select:
            lV = listaVerificacion.objects.get(idLV = id)
            if l.idLV == lV:
             
              Lista.append([l.idp,l.No,l.preguta,l.respuesta,l.observacion])
      return Lista


      