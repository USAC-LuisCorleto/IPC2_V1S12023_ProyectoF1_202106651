from nodolde import Nodo
import xml.etree.cElementTree as ET
from sala import Sala

class ListaEnlazadaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def add(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def Imprimir(self):
        actual = self.cabeza
        while actual is not None:
            actual.dato.imprimir()
            actual = actual.siguiente

    def editar_salas(self, numero_sala, nuevos_asientos):
        actual = self.cabeza
        while actual is not None:
            if actual.dato.numero_sala == numero_sala:
                actual.dato.capacidad = nuevos_asientos
                self.actualizar_xml()
                break
            actual = actual.siguiente
    
    def eliminar_sala(self, numero_sala):
        actual = self.cabeza
        while actual is not None:
            if actual.dato.numero_sala == numero_sala:
                siguiente_nodo = actual.siguiente
                anterior_nodo = actual.anterior

                if siguiente_nodo:
                    siguiente_nodo.anterior = anterior_nodo
                if anterior_nodo:
                    anterior_nodo.siguiente = siguiente_nodo
                if actual == self.cabeza:
                    self.cabeza = siguiente_nodo
                if actual == self.cola:
                    self.cola = anterior_nodo
                
                self.actualizar_xml()
                break
            actual = actual.siguiente

    def actualizar_xml(self):
        nombre_cine = "Cinepolis"
        
        root = ET.Element("cines")
        cine_element = ET.SubElement(root, "cine")
        nombre_element = ET.SubElement(cine_element, "nombre")
        nombre_element.text = nombre_cine
        salas_element = ET.SubElement(cine_element, "salas")

        actual = self.cabeza
        while actual is not None:
            sala_element = ET.SubElement(salas_element, "sala")
            numero_sala = ET.SubElement(sala_element, "numero")
            numero_sala.text = actual.dato.numero_sala
            capacidad_asientos = ET.SubElement(sala_element, "asientos")
            capacidad_asientos.text = str(actual.dato.capacidad)

            actual = actual.siguiente

        tree = ET.ElementTree(root)
        tree.write("salas.xml")

    def guardar_en_xml(self):
        root = ET.Element("cines")

        actual = self.cabeza
        cine_element = ET.SubElement(root, "cine")
        nombre_element = ET.SubElement(cine_element, "nombre")
        nombre_element.text = actual.dato.nombre_cine
        while actual is not None:
            salas_element = ET.SubElement(cine_element, "salas")

            sala_actual = actual.dato
            while sala_actual is not None:
                sala_element = ET.SubElement(salas_element, "sala")

                numero_element = ET.SubElement(sala_element, "numero")
                numero_element.text = sala_actual.numero_sala

                asientos_element = ET.SubElement(sala_element, "asientos")
                asientos_element.text = str(sala_actual.capacidad)

                sala_actual = None

            actual = actual.siguiente

        tree = ET.ElementTree(root)
        tree.write("salas.xml")

    def cargar_xml(self, archivo):
        tree = ET.parse(archivo)
        root = tree.getroot()

        cine_element = root.find("cine")
        salas_element = cine_element.find("salas")

        if salas_element is not None:
            actual = self.cabeza
            while actual is not None:
                self.eliminar_sala(actual.dato.numero_sala)
                actual = actual.siguiente

            for sala_element in salas_element.findall("sala"):
                numero_sala = sala_element.find("numero").text
                capacidad_asientos = int(sala_element.find("asientos").text)
                
                nueva_sala = Sala(numero_sala, capacidad_asientos)
                self.add(nueva_sala)

            self.actualizar_xml()
            print("--------------------------")
            print("XML Cargado correctamente.")

    def Imprimir_sala(self):
        actual = self.cabeza
        while actual is not None:
            actual.dato.imprimir_sala()
            actual = actual.siguiente