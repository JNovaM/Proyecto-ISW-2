from Web.models import PUL
from Web.models import listaVerificacion
from Web.models import usuario
from Web.models import producto
from Web.CRUDs import crudpreguntasU
from Web.CRUDs import crudPreguntas




def asignar(idU,idLV,idP):
    idU1 = usuario.objects.get(idU = idU)
    idP1 = producto.objects.get(idP = idP)
    idLV1 = listaVerificacion.objects.get(idLV = idLV)
    try:
       aux =  PUL.objects.get(idU = idU1,idP = idP1, idLV = idLV1).idLV
       return False
    except:
       newASig = PUL(idU = idU1,idP = idP1, idLV = idLV1)
       newASig.save()
       list =  crudPreguntas.ListarPreguntas(idLV)
       for l in list:
        crudpreguntasU.crearPreguntaU(idU1,idLV1,l[1],l[2],l[3],l[4],False)
         

        
       return True


