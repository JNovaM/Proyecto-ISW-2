from django.shortcuts import render
from django.http import HttpResponse
from Web.models import usuario 

from Web.CRUDs import crudUsuarios
from Web.CRUDs import crudProductos
from Web.CRUDs import crudListaVerificacion
from Web.CRUDs import crudPUL
from Web.CRUDs import crudpreguntasU
from datetime import datetime
from Web.models import listaVerificacion

import threading
ListaSeciones = []




# Esto de encarga de borrar la sesion si el usuario lleva mas de 20 minutos inactivo
def borrarsecion():   
        
        date = datetime.now()
        i=0
        print(str(date.hour)+':'+str(date.minute))
        
        for secion in ListaSeciones:
           
            if secion[2] == date.hour:
                if date.minute-secion[3] >20:
                     
                     ListaSeciones.pop(i)
            elif secion[2] < date.hour:
                if 60-secion[3]+date.minute >20:
                    ListaSeciones.pop(i)
            i=i+1
        







# validacion al intentar acceder
def inicio(request):
    date = datetime.now()
    ip = request.META.get('REMOTE_ADDR')
    paso = False  
    for a in ListaSeciones :
        if a[0] == ip:
            paso = True
            user = a[1]
            a[2] = date.hour
            a[3] = date.minute
            break
    if(paso):
       return DashBoard(request)
    else:
       return render(request, 'MiPaginaWeb/index.html')


# serrar la sesion
def salir(request):
    i=0
    ip = request.META.get('REMOTE_ADDR')
    if(request.method == 'POST'):
      for secion in ListaSeciones:
           if secion[0] == ip:
                ListaSeciones.pop(i)
           i = i+1
    return render(request, 'MiPaginaWeb/index.html')



# Acceder  a la vista del dashboard
def  DashBoard(request):
    borrarsecion()
    date = datetime.now()

    nombre = ''
    passw = ''
    ip = request.META.get('REMOTE_ADDR')
    if(request.method == 'POST'):
    
       nombre =  request.POST.get('name') 
       passw = request.POST.get('passw')
       try:
         useraux = usuario.objects.get(usuario = nombre)
      
         if useraux.password == passw:
              paginaU = 1
              paginaUB = 1

              paginaP = 1
              paginaPB = 1

              paginaR = 1
              paginaRB = 1

              paginaL = 1
              paginaLB = 1
              ListaSeciones.append([ip,nombre,date.hour,date.minute,paginaU,paginaUB,paginaP,paginaPB,paginaR,paginaRB,paginaL,paginaLB,''])

       except Exception as Ex:
           print(Ex)

    
    paso = False
    user = ''
    esAdmin = True
    for a in ListaSeciones :
        if a[0] == ip:
            paso = True
            user = a[1]
            a[2] = date.hour
            a[3] = date.minute
            esAdmin = crudUsuarios.esAdmin(user)
            break
 
    if (paso):
        
        return render(request,'MiPaginaWeb/Dashboard.html',{'nameuser': user, 'esAdmin':esAdmin})
    else:
        alerta = True
        return render(request, 'MiPaginaWeb/index.html',{'alerta':alerta})


# Acceder a la vista de usuarios
def UsuariosWeb(request):
     borrarsecion()
     date = datetime.now()
     Lista = crudUsuarios.ListarUser()
     
     
     ip = request.META.get('REMOTE_ADDR')
     paso = False
     user = ''
     esAdmin = False
     paginaU = 0 
     for a in ListaSeciones :
        if a[0] == ip:
            paso = True
            user = a[1]
            a[2] = date.hour
            a[3] = date.minute
            paginaU = a[4] 
            esAdmin = crudUsuarios.esAdmin(user)
            
            break
 
     if (paso):
        index1 = 20*paginaU
        Lista = Lista[index1-20:index1]
        alerta = False
        return render(request,'MiPaginaWeb/Usuarios.html',{'nameuser': user, 'usuarios': Lista, 'esAdmin':esAdmin,'page':paginaU,'alerta':alerta})
     else:
        return render(request, 'MiPaginaWeb/index.html')

# Acceder a la vista de Productos 
def ProductosWeb(request):
     borrarsecion()
     date = datetime.now()
     Lista = crudProductos.ListarProductos()
    
     ip = request.META.get('REMOTE_ADDR')
     paso = False
     user = ''
     esAdmin = False
     paginaP = 0
     for a in ListaSeciones :
        if a[0] == ip:
            paso = True
            user = a[1]
            a[2] = date.hour
            a[3] = date.minute
            paginaP = a[6]
            esAdmin = crudUsuarios.esAdmin(user)
            break
 
     if (paso):
        index1 = 20*paginaP
        Lista = Lista[index1-20:index1]
        return render(request,'MiPaginaWeb/Productos.html',{'nameuser': user,'esAdmin': esAdmin, 'productos': Lista,'page':paginaP,'alerta':False})
     else:
        return render(request, 'MiPaginaWeb/index.html')


def ReporteWeb(request):
    return '500'


def ListaWeb(request):
     borrarsecion()
     date = datetime.now()
     Lista = crudListaVerificacion.ListarListas()
     Lista1 = crudUsuarios.ListarUser()
     Lista2 = crudProductos.ListarProductos()
     
     ip = request.META.get('REMOTE_ADDR')
     paso = False
     user = ''
     esAdmin = False
     paginaL = 0 
     for a in ListaSeciones :
        if a[0] == ip:
            paso = True
            user = a[1]
            a[2] = date.hour
            a[3] = date.minute
            paginaL = a[10] 
            esAdmin = crudUsuarios.esAdmin(user)
            
            break
     if esAdmin != True & paso:
        Lista = crudListaVerificacion.ListarRev(user)
     if (paso):
        index1 = 20*paginaL
        Lista = Lista[index1-20:index1]
        alerta = False
        return render(request,'MiPaginaWeb/ListaV.html',{'nameuser': user, 'listas': Lista, 'esAdmin':esAdmin,'page':paginaL,'alerta':alerta, 'listU':Lista1, 'listP':Lista2})
     else:
        return render(request, 'MiPaginaWeb/index.html')






"""
CRUDs
"""


def CrearUsuario(request):
    date = datetime.now()
    borrarsecion()
    
    Lista =  crudUsuarios.ListarUser()
   
    
    esAdmin = False
    if request.method == 'POST':

         
         esAdmin = False
         
         if request.POST.get('Categoria') == "Admin":
             esAdmin = True

    ip = request.META.get('REMOTE_ADDR')
    paso = False  
    esAdmin1 = True
    paginaU = 0
    for a in ListaSeciones :
        if a[0] == ip:
            paso = True
            user = a[1]
            a[2] = date.hour
            a[3] = date.minute
            paginaU = a[4]
            esAdmin1 = crudUsuarios.esAdmin(user)
            break
    index1 = 20*paginaU 
    Lista = Lista[index1-20:index1]  
    if (paso & esAdmin1):
        if request.method == 'POST':
            alerta = crudUsuarios.CreateUser(request.POST.get('name'), request.POST.get('passw'), esAdmin)
            Lista = crudUsuarios.ListarUser()
            index1 = 20*paginaU
            Lista = Lista[index1-20:index1]
        else:
            alerta = False

        return render(request,'MiPaginaWeb/Usuarios.html',{'nameuser': user, 'usuarios': Lista, 'esAdmin':esAdmin1,'page':paginaU, 'alerta':alerta,'mensajeerror':"El usuario ya existe" })
    else:
        return render(request, 'MiPaginaWeb/index.html')

    
def eliminarUsers(request):
    date = datetime.now()
    borrarsecion()
    ip = request.META.get('REMOTE_ADDR')
    for a in ListaSeciones :
        if a[0] == ip:
            paso = True
            user = a[1]
            a[2] = date.hour
            a[3] = date.minute
            esAdmin = crudUsuarios.esAdmin(user)
            break
    if request.method == 'POST':
        if(paso & esAdmin):
            for id in request.POST.getlist('listaEliminar[]'):
                 crudUsuarios.EliminarUser(id)
    request.method = 'GET'
    return UsuariosWeb(request)
 

   
def modificarUser(request):
    date = datetime.now()
    borrarsecion()
    if request.method == 'POST':
        esAdminSave = False
        usuarioSave = request.POST.get('usuario')
        passwordSave = request.POST.get('passw')
        if request.POST.get('esAdmin') == 'A':
            esAdminSave = True
        
        id = request.POST.get('id')
        

        ip = request.META.get('REMOTE_ADDR')
        paso = False  
        esAdmin1 = True
        for a in ListaSeciones :
          if a[0] == ip:
             paso = True
             user = a[1]
             a[2] = date.hour
             a[3] = date.minute
             esAdmin1 = crudUsuarios.esAdmin(user)
             break
        if(paso & esAdmin1): 
            crudUsuarios.modificarUser(id,usuarioSave,passwordSave,esAdminSave)
    request.method = 'GET'
    return UsuariosWeb(request)

def  buscarU(request):
    date = datetime.now()
    borrarsecion()
    ip = request.META.get('REMOTE_ADDR')
    paso = False  
    esAdmin1 = True
    for a in ListaSeciones :
          if a[0] == ip:
             paso = True
             user = a[1]
             a[2] = date.hour
             a[3] = date.minute
             paginaUB = a[5]
             esAdmin1 = crudUsuarios.esAdmin(user)
             break
    if (paso & esAdmin1):
        Lista = []
        if request.method == 'POST':
            Lista = crudUsuarios.buscar(request.POST.get('search'))
            print( request.POST.get('search'))
            index1 = 20*paginaUB
            Lista = Lista[index1-20:index1]
        alerta = False
        return render(request,'MiPaginaWeb/Usuarios.html',{'nameuser': user, 'usuarios': Lista, 'esAdmin':esAdmin1,'page':paginaUB,'alerta':alerta})
    else:
        return render(request, 'MiPaginaWeb/index.html')





    







def añadirProducto(request):
    date = datetime.now()
    borrarsecion()
    
    Lista =  crudProductos.ListarProductos()
    terminado = False
    if request.method == 'POST':

         terminado = False
         
         if request.POST.get('terminado') == "terminado":
             terminado = True

    ip = request.META.get('REMOTE_ADDR')
    paso = False  
    esAdmin1 = True
    paginaP = 0
    for a in ListaSeciones :
        if a[0] == ip:
            paso = True
            user = a[1]
            a[2] = date.hour
            a[3] = date.minute
            paginaP = a[6]
            esAdmin1 = crudUsuarios.esAdmin(user)
            break
    index1 = 20*paginaP
    Lista = Lista[index1-20:index1]
    if (paso & esAdmin1):
        alerta = False
        if request.method == 'POST':
            alerta = crudProductos.CreateProducto(request.POST.get('nombreProd'), request.POST.get('versionProd'), request.POST.get('fechaLimite'),request.POST.get('centroOrigen'),terminado,request.POST.get('iteracion'))
            Lista = crudProductos.ListarProductos()
            Lista = Lista[index1-20:index1]
        return render(request,'MiPaginaWeb/Productos.html',{'nameuser': user, 'productos': Lista, 'esAdmin':esAdmin1,'page':paginaP,'alerta':alerta, 'mensajeerror':"El producto ya existe"})
    else:
        return render(request, 'MiPaginaWeb/index.html')

def eliminarProducto(request):
    date = datetime.now()
    borrarsecion()
    ip = request.META.get('REMOTE_ADDR')
    for a in ListaSeciones :
        if a[0] == ip:
            paso = True
            user = a[1]
            a[2] = date.hour
            a[3] = date.minute
            esAdmin = crudUsuarios.esAdmin(user)
            break
    if request.method == 'POST':
        if(paso & esAdmin):
            for id in request.POST.getlist('listaEliminar[]'):
                 crudProductos.EliminarProducto(id)
    request.method = 'GET'
    return ProductosWeb(request)

def modificarProducto(request):
    date = datetime.now()
    borrarsecion()
    if request.method == 'POST':
        estadoSave = False
        nombrePSave = request.POST.get('nombreProducto')
        vercionSave = request.POST.get('vercion')
        FechaFinSave = request.POST.get('FechaFin')

        if request.POST.get('estado') == 'T':
            estadoSave = True
        
        iteracionSave = request.POST.get('iteracion')
        nombPR = request.POST.get('id')
        centro = request.POST.get('centro')
        ip = request.META.get('REMOTE_ADDR')
        paso = False  
        esAdmin1 = True
        for a in ListaSeciones :
          if a[0] == ip:
             paso = True
             user = a[1]
             a[2] = date.hour
             a[3] = date.minute
             esAdmin1 = crudUsuarios.esAdmin(user)
             break
        if(paso & esAdmin1): 
            crudProductos.modificarProducto(nombPR,nombrePSave,vercionSave,FechaFinSave,estadoSave,iteracionSave,centro)
    request.method = 'GET'
    return ProductosWeb(request)


def  buscarP(request):
    date = datetime.now()
    borrarsecion()
    ip = request.META.get('REMOTE_ADDR')
    paso = False  
    esAdmin1 = True
    paginaPB = 0
    for a in ListaSeciones :
          if a[0] == ip:
             paso = True
             user = a[1]
             a[2] = date.hour
             a[3] = date.minute
             paginaPB = a[7]
             esAdmin1 = crudUsuarios.esAdmin(user)
             break
    if (paso & esAdmin1):
        Lista = []
        if request.method == 'POST':
            Lista = crudProductos.buscar(request.POST.get('search'))
           
            index1 = 20*paginaPB
            Lista = Lista[index1-20:index1]
        alerta = False
        return render(request,'MiPaginaWeb/Productos.html',{'nameuser': user,'esAdmin': esAdmin1, 'productos': Lista,'page':paginaPB,'alerta':alerta})
    else:
        return render(request, 'MiPaginaWeb/index.html')






def crearLista(request):
    date = datetime.now()
    borrarsecion()
    Lista1 = crudUsuarios.ListarUser()
    Lista2 = crudProductos.ListarProductos()
    if request.method == 'POST':
      
      Lista = request.POST.get('listaV1').split("\n")
     
      NombreLista = Lista[0].split('undefined')[1]
      ListaP = []
      tipo = Lista[1].split(',')[1]
      Lista = Lista[2:]
    
      for pregunta in Lista:
         dato = []
         if len(pregunta.split(',')) == 1:
            tipo = pregunta 
         else:   
           dato =  pregunta.split(',')
           dato.extend([tipo])
        
           ListaP.append(dato)
      print(ListaP)
      requisito = request.POST.get('requisito')
      ip = request.META.get('REMOTE_ADDR')
      paso = False  
      esAdmin1 = True
      paginaL = 0 
      for a in ListaSeciones :
          if a[0] == ip:
             paso = True
             user = a[1]
             a[2] = date.hour
             a[3] = date.minute
             paginaL = a[10] 
             esAdmin1 = crudUsuarios.esAdmin(user)
             break
      if (paso & esAdmin1):
        alerta = crudListaVerificacion.CreateLista(ListaP,requisito,NombreLista) 
        index1 = 20*paginaL
        Lista = crudListaVerificacion.ListarListas()
        Lista = Lista[index1-20:index1]
       
        return render(request,'MiPaginaWeb/ListaV.html',{'nameuser': user, 'listas': Lista, 'esAdmin':esAdmin1,'page':paginaL,'alerta':alerta, 'listU':Lista1, 'listP':Lista2,'mensajeerror':"La Lista ya existe"})
      else:
        return render(request, 'MiPaginaWeb/index.html')
    else:
        request.method = 'GET'
        return ListaWeb(request)

def eliminarLista(request):
    date = datetime.now()
    borrarsecion()
    ip = request.META.get('REMOTE_ADDR')
    for a in ListaSeciones :
        if a[0] == ip:
            paso = True
            user = a[1]
            a[2] = date.hour
            a[3] = date.minute
            esAdmin = crudUsuarios.esAdmin(user)
            break
    if request.method == 'POST':
        if(paso & esAdmin):
            for id in request.POST.getlist('listaEliminar[]'):
                 crudListaVerificacion.EliminarListaV(id)
    request.method = 'GET'
    return ListaWeb(request)
    

def buscarlv(request):
     borrarsecion()
     date = datetime.now()
     if request.method == 'POST':
         Lista = crudListaVerificacion.buscar(request.POST.get('search'))
     
     Lista1 = crudUsuarios.ListarUser()
     Lista2 = crudProductos.ListarProductos()
     
     ip = request.META.get('REMOTE_ADDR')
     paso = False
     user = ''
     esAdmin = False
     paginaL = 0 
     for a in ListaSeciones :
        if a[0] == ip:
            paso = True
            user = a[1]
            a[2] = date.hour
            a[3] = date.minute
            paginaL = a[10] 
            esAdmin = crudUsuarios.esAdmin(user)
            
            break
 
     if (paso):
        index1 = 20*paginaL
        Lista = Lista[index1-20:index1]
        alerta = False
        return render(request,'MiPaginaWeb/ListaV.html',{'nameuser': user, 'listas': Lista, 'esAdmin':esAdmin,'page':paginaL,'alerta':alerta, 'listU':Lista1, 'listP':Lista2})
     else:
        return render(request, 'MiPaginaWeb/index.html')


def asignarLista(request):
    if request.method == 'POST':
       crudPUL.asignar(request.POST.get('idU'),request.POST.get('idLV'),request.POST.get('idP'))

    request.POST = 'GET'
    return ListaWeb(request)

from Web.CRUDs import crudPreguntas

def PregLV(request):
     
     ip = request.META.get('REMOTE_ADDR')
     borrarsecion()
     date = datetime.now()
     user = ""
     try:
      if request.method == 'POST':
        esAdmin = False
      
        for a in ListaSeciones :
            if a[0] == ip:
               user = a[1]
               a[2] = date.hour
               a[3] = date.minute
               esAdmin = crudUsuarios.esAdmin(user)
               a[12] = request.POST.get('idLV22')
               break   
        if esAdmin:
         Lista = crudPreguntas.ListarPreguntas(request.POST.get('idLV22'))
        else:
         Lista = crudpreguntasU.ListarPreguntas(user,request.POST.get('idLV22'))

      else:
        
        esAdmin = False
        for a in ListaSeciones :
            if a[0] == ip:
             
             user = a[1]
             a[2] = date.hour
             a[3] = date.minute
             esAdmin = crudUsuarios.esAdmin(user)
             if esAdmin:
               Lista = crudPreguntas.ListarPreguntas(a[12])
             else:
               Lista = crudpreguntasU.ListarPreguntas(user,a[12]) 
             break
      return render(request,'MiPaginaWeb/PreguntasLista.html',{'listas': Lista, 'esAdmin':esAdmin,'ultimo': Lista[len(Lista)-1][1]+1})    
     except:
      request.method = 'GET'  
      return ListaWeb(request)



def adicionarPregunta(request):
     ip = request.META.get('REMOTE_ADDR')
     borrarsecion()
     date = datetime.now()
     user = ""
     idLv = ""
     if request.method == "POST":
         for a in ListaSeciones :
            if a[0] == ip:
             
             user = a[1]
             a[2] = date.hour
             a[3] = date.minute
             esAdmin = crudUsuarios.esAdmin(user)
             user = usuario.objects.get(usuario = user)
             idLv = listaVerificacion.objects.get(idLV = a[12])
             break
         no = request.POST.get('No')
         preg = request.POST.get('pregunta')
         crudpreguntasU.crearPreguntaU(user,idLv,no,preg,None,None,True)
     request.method = "GET"
     return  PregLV(request)
    


def eliminarPreg(request):
     ip = request.META.get('REMOTE_ADDR')
     borrarsecion()
     date = datetime.now()
     user = ""
     idLv = ""
     if request.method == "POST":
          for a in ListaSeciones :
            if a[0] == ip:
             
             user = a[1]
             a[2] = date.hour
             a[3] = date.minute
             esAdmin = crudUsuarios.esAdmin(user)
             user = usuario.objects.get(usuario = user)
             idLv = listaVerificacion.objects.get(idLV = a[12])
             crudpreguntasU.eliminarP(user,idLv,request.POST.get('No'))
             break
        
     request.method = "GET"
     return  PregLV(request)