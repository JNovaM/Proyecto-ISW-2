from Web.models import producto
from datetime import datetime





def CreateProducto(nombreProd,versionProd,fechaLimite, centroOrigen, productoRevisado, iteracion):
     try :
         producto.objects.get(nombreProd = nombreProd).nombreProd
         return True
     except:
      date = datetime.now()
     
      fechaCreacion = str(date.year) + "-" + str(date.month) + "-" + str(date.day)
      newProd = producto (nombreProd = nombreProd, versionProd = versionProd, fechaCreacion = fechaCreacion, fechaLimite = fechaLimite,  centroOrigen =  centroOrigen,productoRevisado = productoRevisado,iteracion=iteracion)
      newProd.save()
      return False


def EliminarProducto(id):
    try:
      delete = producto.objects.get(idP = id)
      delete.delete()
      return True
    except:
      return False

def ListarProductos():
   Lista = []
   select =  producto.objects.all()
   for prod in select:
        Lista.append([prod.nombreProd,prod.versionProd,prod.fechaCreacion,prod.fechaLimite,prod.centroOrigen,prod.idP])
   return Lista

   
def modificarProducto(nombPR,nombreP,vercion,fechaFin,estado,iteracion,centro):
    try:
      producto1 = producto.objects.get(nombreProd = nombPR)
      producto1.nombreProd = nombreP
      producto1.versionProd = vercion
      producto1.fechaLimite = fechaFin
      producto1.productoRevisado = estado
      producto1.iteracion = iteracion
      producto1.centroOrigen = centro
      producto1.save()
      return True
    except:
      return False


def buscar(text):
   Lista = []
   select =  producto.objects.all()
   for prod in select:
       paso = False
       if text.lower() in  str(prod.nombreProd).lower():
          paso = True
       elif text.lower() in str(prod.centroOrigen).lower():
          paso = True
       elif text.lower() in str(prod.iteracion).lower():
          paso = True
       if paso:     
          Lista.append([prod.nombreProd,prod.versionProd,prod.fechaCreacion,prod.fechaLimite,prod.centroOrigen,prod.idP])
   return Lista