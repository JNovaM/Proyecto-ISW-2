from django.test import TestCase
from Web.CRUDs import crudUsuarios
from Web.CRUDs import crudProductos

class usuarioTestCase(TestCase):
    
       
    def setUp(self):
        crudUsuarios.CreateUser("pedrorfg","123123123123",True)
        crudUsuarios.CreateUser("pablofg","123123123123",True)
        crudUsuarios.CreateUser("ernestofg","123123123123",False)
        crudProductos.CreateProducto("Todus","1.1.2","2022-12-29","Centro de Tecnologías Interactivas",False,1)
        crudProductos.CreateProducto("Apklis","1.3.2","2023-1-21","Centro de Tecnologías Interactivas",False,1)
        crudProductos.CreateProducto("Viajando","1.1.2","2023-1-24","Centro de Tecnologías Interactivas",False,1)


        pass
    def tearDown(self):
        
        pass    

    def test_usuario_Listar(self):
        object = crudUsuarios.ListarUser() 
        
        self.assertIsNotNone(object)

    def test_usuario_guardar_nuevo_noExiste(self):
        object = crudUsuarios.CreateUser("alejandrofg","123123123123",True) 
        
        self.assertFalse(object)
        



    def test_usuario_Eliminia_Usuario(self):
        object = crudUsuarios.EliminarUser(1)

        self.assertEqual(object,True)

    def test_usuario_modificar(self):
        object = crudUsuarios.modificarUser("pablofg","joserfg","123123123",True) 
        
        self.assertTrue(object)

    def test_usuario_esAdmin(self):
        object = crudUsuarios.esAdmin("pablofg")
        self.assertTrue(object)
    def test_usuario_noEsAdmin(self):
        object = crudUsuarios.esAdmin("ernestofg")
        self.assertFalse(object)



    def test_producto_Listar(self):
        object = crudProductos.ListarProductos()
        
        self.assertIsNotNone(object)

    def test_producto_guardar_nuevo_noExiste(self):
        object = crudProductos.CreateProducto("Transfermovil","0.1.2","2022-12-29","Centro de Tecnologías Interactivas",False,1)
        
        self.assertFalse(object)



    def test_uproducto_Eliminia(self):
        object =  crudProductos.EliminarProducto(1)

        self.assertEqual(object,True)

    def test_producto_modificar(self):
        object = crudProductos.modificarProducto("Apklis","Apklis","1.2.2","2023-1-24",False,1,"Centro de Tecnologías Interactivas")
        
        self.assertTrue(object)

    
    def test_producto_Listar_busqueda(self):
        object = crudProductos.buscar("Apklis")
        
        self.assertIsNotNone(object)
    
    def test_usuario_Listar_busqueda(self):
        object = crudUsuarios.buscar("pedrofg")
        
        self.assertIsNotNone(object)