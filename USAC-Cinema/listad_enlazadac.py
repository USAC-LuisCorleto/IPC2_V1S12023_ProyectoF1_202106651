from nodoldec import Nodo
import xml.etree.cElementTree as ET

class ListaEnlazadaCircularDoble:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None
    
    def add(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.esta_vacia():
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            ultimo = self.cabeza.anterior
            nuevo_nodo.siguiente = self.cabeza
            nuevo_nodo.anterior = ultimo
            self.cabeza.anterior = nuevo_nodo
            ultimo.siguiente = nuevo_nodo
            self.cabeza = nuevo_nodo

    def Imprimir(self):
        if self.esta_vacia():
            print("-------------------")
            print("La lista está vacía")
        else:
            actual = self.cabeza
            while True:
                actual.dato.imprimir()
                actual = actual.siguiente
                if actual == self.cabeza:
                    break

    def guardar_en_xml(self):
        root = ET.Element("categorias")

        # Recorrer las categorías y agregarlas al XML
        categorias = set()
        actual = self.cabeza
        while True:
            categoria = actual.dato.nombre_categoria
            categorias.add(categoria)
            actual = actual.siguiente
            if actual == self.cabeza:
                break

        for categoria in categorias:
            categoria_element = ET.SubElement(root, "categoria")
            nombre_element = ET.SubElement(categoria_element, "nombre")
            nombre_element.text = categoria

            peliculas_element = ET.SubElement(categoria_element, "peliculas")

            actual = self.cabeza
            while True:
                if actual.dato.nombre_categoria == categoria:
                    pelicula_element = ET.SubElement(peliculas_element, "pelicula")

                    titulo_element = ET.SubElement(pelicula_element, "titulo")
                    titulo_element.text = actual.dato.titulo

                    director_element = ET.SubElement(pelicula_element, "director")
                    director_element.text = actual.dato.director

                    anio_element = ET.SubElement(pelicula_element, "anio")
                    anio_element.text = actual.dato.año_pelicula

                    fecha_element = ET.SubElement(pelicula_element, "fecha")
                    fecha_element.text = actual.dato.fecha_funcion

                    hora_element = ET.SubElement(pelicula_element, "hora")
                    hora_element.text = actual.dato.hora_funcion

                actual = actual.siguiente
                if actual == self.cabeza:
                    break

        tree = ET.ElementTree(root)
        tree.write("categorias.xml")

    def editar_categorias_peliculas(self):
        while True:
            print("")
            print("Usted se encuentra en la opción gestionar Categorías y Películas")
            print("Elija una opción")
            print("[1]. Editar Categorías.")
            print("[2]. Editar Películas.")
            print("[3]. Regresar")
            opcion = input()

            if opcion == "1":
                self.editar_categorias()
            elif opcion == "2":
                self.editar_peliculas()
            elif opcion == "3":
                break
            else:
                print("Opción inválida, intente de nuevo.")

    def editar_categorias(self):
        categoria = input("Ingrese el nombre de la categoría a editar: ")
        nueva_categoria = input("Ingrese el nuevo nombre de la categoría: ")

        actual = self.cabeza
        while True:
            if actual.dato.nombre_categoria == categoria:
                actual.dato.nombre_categoria = nueva_categoria
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        self.guardar_en_xml()
        print("Categoría actualizada correctamente")

    def editar_peliculas(self):
        categoria = input("Ingrese el nombre de la categoría a la que pertenece la película: ")
        titulo = input("Ingrese el título de la película a editar: ")

        actual = self.cabeza
        while True:
            if actual.dato.nombre_categoria == categoria and actual.dato.titulo == titulo:
                nuevo_titulo = input("Ingrese el nuevo título de la película: ")
                nuevo_director = input("Ingrese el nuevo nombre del director: ")
                nuevo_anio = input("Ingrese el nuevo año de la película: ")
                nueva_fecha = input("Ingrese la nueva fecha de la función: ")
                nueva_hora = input("Ingrese la nueva hora de la función: ")

                actual.dato.titulo = nuevo_titulo
                actual.dato.director = nuevo_director
                actual.dato.año_pelicula = nuevo_anio
                actual.dato.fecha_funcion = nueva_fecha
                actual.dato.hora_funcion = nueva_hora
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        self.guardar_en_xml()
        print("Película actualizada correctamente")