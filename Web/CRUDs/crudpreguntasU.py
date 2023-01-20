from Web.models import preguntasU
from Web.models import listaVerificacion
from Web.models import usuario




def crearPreguntaU(idu,idlv,no,preg,respu,obser,modif):
     preguntasU( idU =idu, idLV=idlv, No = no, preguta =  preg, respuesta = respu, observacion = obser, modif = modif).save()

def eliminarP(IDU,IDLV,no):
      preguntasU.objects.get( idU = IDU, idLV =IDLV,No = no).delete()

def ListarPreguntas(id,idlv):
      Lista = []
      select = preguntasU.objects.all()
      
      for l in select:
            lV = listaVerificacion.objects.get(idLV = idlv)
            id1 =  usuario.objects.get(usuario = id)
            if l.idLV == lV :
             if l.idU == id1:
               Lista.append([idlv,l.No,l.preguta,l.respuesta,l.observacion,l.modif])
      return Lista


