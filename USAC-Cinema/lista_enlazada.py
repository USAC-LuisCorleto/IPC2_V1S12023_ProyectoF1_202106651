from nodo import Nodo
from usuario import Usuario
import xml.etree.ElementTree as ET

class ListaEnlazadaSimple:
    def __init__(self):
        self.cabeza = None

    def add(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def Imprimir(self):
        actual = self.cabeza
        while actual is not None:
            actual.dato.imprimir()
            actual = actual.siguiente

    def editar_usuario(self, correo, contraseña):
        usuario = self.buscar_usuario(correo, contraseña)
        if usuario is not None:
            print("---------------------")
            print("--Datos del usuario--")
            print(f"Rol: {usuario.rol}")
            print(f"Nombre: {usuario.nombre}")
            print(f"Apellido: {usuario.apellido}")
            print(f"Teléfono: {usuario.telefono}")
            print(f"Correo: {usuario.correo}")
            print(f"Contraseña: {usuario.contraseña}")

            print("----------------------------")
            print("--Ingrese los nuevos datos--")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            telefono = input("Teléfono: ")
            nuevo_correo = input("Correo: ")
            nueva_contraseña = input("Contraseña: ")

            correo_antiguo = usuario.correo

            usuario.rol = "Cliente"
            usuario.nombre = nombre
            usuario.apellido = apellido
            usuario.telefono = telefono
            usuario.correo = nuevo_correo
            usuario.contraseña = nueva_contraseña

            if correo_antiguo != nuevo_correo:
                self.actualizar_correo_usuario_xml(correo_antiguo, usuario)

            self.actualizar_usuario_xml(usuario)

            print("Datos actualizados correctamente.")
            return
        
        print("No se encontró el usuario.")

    def actualizar_correo_usuario_xml(self, correo_antiguo, usuario):
        tree = ET.parse("usuarios.xml")
        root = tree.getroot()

        for usuario_element in root.findall("usuario"):
            correo_elem = usuario_element.find("correo")
            if correo_elem.text == correo_antiguo:
                correo_elem.text = usuario.correo
        
        tree.write("usuarios.xml")

    def actualizar_usuario_xml(self, usuario):
        tree = ET.parse("usuarios.xml")
        root = tree.getroot()

        for usuario_element in root.findall("usuario"):
            correo_elem = usuario_element.find("correo")
            if correo_elem.text == usuario.correo:

                rol_elem = usuario_element.find("rol")
                rol_elem.text = usuario.rol

                nombre_elem = usuario_element.find("nombre")
                nombre_elem.text = usuario.nombre

                apellido_elem = usuario_element.find("apellido")
                apellido_elem.text = usuario.apellido

                telefono_elem = usuario_element.find("telefono")
                telefono_elem.text = usuario.telefono

                contraseña_elem = usuario_element.find("contrasena")
                contraseña_elem.text = usuario.contraseña

                #print("Valores actualizados:")
                #print("Rol:", usuario_element.find("rol").text)
                #print("Nombre:", usuario_element.find("nombre").text)
                #print("Apellido:", usuario_element.find("apellido").text)
                #print("Teléfono:", usuario_element.find("telefono").text)
                #print("Correo:", correo_elem.text)
                #print("Contraseña:", usuario_element.find("contrasena").text)

        tree.write("usuarios.xml")
            
    def eliminar_usuario(self, correo, contraseña):
        usuario = self.buscar_usuario(correo, contraseña)
        if usuario is not None:
            if usuario == self.cabeza:
                self.cabeza = usuario.siguiente
            else:
                anterior = self.cabeza
                actual = anterior.siguiente
                while actual is not None:
                    if actual == usuario:
                        anterior.siguiente = actual.siguiente
                        break
                    anterior = actual
                    actual = actual.siguiente

            tree = ET.parse("usuarios.xml")
            root = tree.getroot()
            for usuario_element in root.findall("usuario"):
                correo_elem = usuario_element.find("correo")
                contraseña_elem = usuario_element.find("contrasena")
                if correo_elem.text == correo and contraseña_elem.text == contraseña:
                    root.remove(usuario_element)
                    break
            tree.write("usuarios.xml")

            print("Usuario eliminado correctamente.")
        else:
            print("No se encontró el usuario.")

    def buscar_usuario(self, correo, contraseña):
        actual = self.cabeza
        while actual is not None:
            if actual.dato.correo == correo and actual.dato.contraseña == contraseña:
                return actual.dato
            actual = actual.siguiente
        return None

    def generar_archivo_XML(self):
        root = ET.Element("usuarios")
        actual = self.cabeza

        while actual is not None:
            usuario_element = ET.SubElement(root, "usuario")

            rol_elem = ET.SubElement(usuario_element, "rol")
            rol_elem.text = actual.dato.rol
            
            nombre_elem = ET.SubElement(usuario_element, "nombre")
            nombre_elem.text = actual.dato.nombre

            apellido_elem = ET.SubElement(usuario_element, "apellido")
            apellido_elem.text = actual.dato.apellido

            telefono_elem = ET.SubElement(usuario_element, "telefono")
            telefono_elem.text = actual.dato.telefono

            correo_elem = ET.SubElement(usuario_element, "correo")
            correo_elem.text = actual.dato.correo

            contraseña_elem = ET.SubElement(usuario_element, "contrasena")
            contraseña_elem.text = actual.dato.contraseña

            actual = actual.siguiente

        tree = ET.ElementTree(root)        
        tree.write("usuarios.xml")
        print("--------------------")
        print("Archivo XML generado")

    def cargar_xml(self, archivo):
        tree = ET.parse(archivo)
        root = tree.getroot()

        self.cabeza = None

        for usuario_element in root.findall("usuario"):
            rol_elem = usuario_element.find("rol").text
            nombre_elem = usuario_element.find("nombre").text
            apellido_elem = usuario_element.find("apellido").text
            telefono_elem = usuario_element.find("telefono").text
            correo_elem = usuario_element.find("correo").text
            contraseña_elem = usuario_element.find("contrasena").text

            nuevo_usuario = Usuario(rol_elem, nombre_elem, apellido_elem, telefono_elem, correo_elem, contraseña_elem)
            self.add(nuevo_usuario)

            self.generar_archivo_XML()
