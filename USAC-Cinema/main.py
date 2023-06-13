from usuario import Usuario
from lista_enlazada import ListaEnlazadaSimple
from pelicula import Película
from listad_enlazadac import ListaEnlazadaCircularDoble

admin = "202106651"
contraseña = "3082203580607"
ListaSimple = ListaEnlazadaSimple()
ListaDobleCircular = ListaEnlazadaCircularDoble()

#Método para el menú
def mostrar_menu():
    print("--------------------------------")
    print("--BIENVENIDO AL MENÚ DE CINEMA--")
    print("Elija una opción")
    print("[1]. Iniciar sesión.")
    print("[2]. Registrarse.")
    print("[3]. Ver listado de películas.")

opcion_valida = False

while True:
    while not opcion_valida:
        mostrar_menu()
        opcion = input()

        #Selección de la opción "Iniciar sesión"
        if opcion=="1":
            print("--------------------------------------------------")
            print("--USTED SE ENCUENTRA EN LA OPCiÓN INICIAR SESIÓN--")
            opcion_valida = True
            print("Ingrese los datos correspondientes")
            print("Usuario: ")
            usuarioIniciarSesion = input()
            print("Contraseña: ")
            contraseñaIniciarSesion = input()

            #Condicional para identificar que es el administrador
            if contraseñaIniciarSesion==contraseña and usuarioIniciarSesion==admin:
                while True:
                    print("---------------------------------------")
                    print("--BIENVENIDO AL MENÚ DE ADMINISTRADOR--")
                    print("Elija una opción")
                    print("[1]. Gestionar usuarios")
                    print("[2]. Gestionar Categorías y películas")
                    print("[3]. Gestionar salas.")
                    print("[4]. Cerrar sesión.")
                    opcion_menuAdmin = input()

                    #Selección de la opción gestionar usuarios
                    if opcion_menuAdmin == "1":
                        while True:
                            print("-----------------------------------------------------")
                            print("Usted se encuentra en la opción 'Gestionar usuarios'.")
                            print("Elija una opción")
                            print("[1]. Editar usuario.")
                            print("[2]. Crear usuario.")
                            print("[3]. Eliminar usuario.")
                            print("[4]. Cargar usuario.")
                            print("[5]. Regresar.")
                            opcion_gestionUsuario = input()

                            #Selección de la opción "Editar usuario"
                            if opcion_gestionUsuario == "1":
                                print("----------------------------")
                                print("Usted va a editar un usuario")
                                print("Ingrese el correo: ")
                                correoEdit = input()
                                print("Ingrese la contraseña: ")
                                contraseñaEdit = input()
                                ListaSimple.editar_usuario(correoEdit, contraseñaEdit)

                            #Selección de la opción "Crear usuario"
                            elif opcion_gestionUsuario == "2":
                                print("---------------------------")
                                print("Usted va a crear un usuario")
                                Rol="Cliente"
                                print("Ingrese su nombre: ")
                                nombre_usuario = input()
                                print("Ingrese su apellido: ")
                                apellido_usuario = input()
                                print("Ingrese su teléfono: ")
                                teléfono_usuario = input()
                                print("Ingrese su correo: ")
                                correo_usuario = input()
                                print("Ingrese una contraseña: ")
                                contraseña_usuario = input()
                                usuario = Usuario(Rol, nombre_usuario, apellido_usuario, teléfono_usuario, correo_usuario, contraseña_usuario)
                                ListaSimple.add(usuario)
                                print("Usuario agregado exitosamaente.")
                                ListaSimple.generar_archivo_XML()
                            
                            #Selección de la opción "Eliminar usuario"
                            elif opcion_gestionUsuario == "3":
                                print("------------------------------")
                                print("Usted va a eliminar un usuario")
                                print("Ingrese el correo: ")
                                correoElim = input()
                                print("Ingrese la contraseña: ")
                                contraseñaElim = input()
                                ListaSimple.eliminar_usuario(correoElim, contraseñaElim)
                            
                            #Selección de la opción "Cargar usuario"
                            elif opcion_gestionUsuario == "4":
                                print("--------------------------------------------------------------------------")
                                print("Usted va a cargar un usuario o usuarios por medio de un archivo XML.")
                                print("Ingrese el nombre del archivo XML tal y como está en su lista de archivos.")
                                nombre_archivo = input()
                                ListaSimple.cargar_xml(nombre_archivo)
                            
                            #Selección de la opción "Regresar al menú administrador"
                            elif opcion_gestionUsuario == "5":
                                print("-----------------------------------")
                                print("Regresando al menú administrador...")
                                break

                    #Selección de la opción "Gestión de Categorías y películas"
                    elif opcion_menuAdmin == "2":
                        print()
                        while True:
                            print("-----------------------------------------------------")
                            print("Usted se encuentra en la opción 'Gestionar Categorías y Películas'.")
                            print("Elija una opción")
                            print("[1]. Editar Categorías y Películas.")
                            print("[2]. Crear Categorías y Películas.")
                            print("[3]. Eliminar Categorías y Películas.")
                            print("[4]. Cargar Categorías y Películas.")
                            print("[5]. Regresar.")
                            opcion_gestionPeliculas = input()

                            #Selección Editar categorías
                            if opcion_gestionPeliculas == "1":
                                ListaDobleCircular.editar_categorias_peliculas()

                            #Selección Crear categorías y películas    
                            if opcion_gestionPeliculas == "2":
                                print("---------------------------------------")
                                print("Usted va a crear Categorías y Películas")
                                print("Ingrese el nombre de la categoría ya existente o cree una nueva: ")
                                nombre_cat = input()
                                print("Ingrese el título de la película: ")
                                titulo_pel = input()
                                print("Ingrese el nombre del director de la película: ")
                                nombre_director = input()
                                print("Ingrese el año en el que fue lanzada la película: ")
                                año_pelicula = input()
                                print("Ingrese la fecha de la función: ")
                                fecha_func = input()
                                print("Ingrese la hora de la función: ")
                                hora_func = input()
                                pelicula = Película(nombre_cat, titulo_pel, nombre_director, año_pelicula, fecha_func, hora_func)
                                ListaDobleCircular.add(pelicula)
                                ListaDobleCircular.guardar_en_xml()
                                print("--------------------------------------------")
                                print("Categoría y Películas añadidas correctamente")
                                ListaDobleCircular.Imprimir()
                                
                            #Selección Eliminar categorías y películas
                            if opcion_gestionPeliculas == "3":
                                print("--------------------------------------------")
                                print("Usted va a eliminar una Categoría o Película")

                    #Selección de la opción "Gestión de Salas"
                    elif opcion_menuAdmin == "3":
                        print()

                    #Selección de la opción "Cerrar sesión"
                    elif opcion_menuAdmin == "4":
                        print("------------------")
                        print("Cerrando sesión...")
                        break
            
            #Función que retorna el usuario ingresado si lo encuentra en alguno de los nodos de la lista.
            usuario_encontrado = ListaSimple.buscar_usuario(usuarioIniciarSesion, contraseñaIniciarSesion)
            if usuario_encontrado is not None:
                print("---------------------------------")
                print("--BIENVENIDO AL MENÚ DE USUARIO--")
                print("Elija una opción")
                print("[1]. Ver listado de películas.")
                print("[2]. Listado de películas favoritas.")
                print("[3]. Comprar boletos.")
                print("[4]. Historial de boletos comprados.")
                print("[5]. Cerrar sesión.")
                opcion_menUsuario = input()

            #Si el usuario no fue encontrado simplemente sale de la condición y debe volver a intentarlo.
            else:
                print("--SU USUARIO NO SE ENCUENTRA REGISTRADO--")
                print("Regresando al menú principal...")
                break
        
        #Selección de la opción "Registrarse"
        elif opcion=="2":
            while  True:
                opcion_valida = True
                Rol = "Cliente"
                print("--USTED SE ENCUENTRA EN LA OPCIÓN REGISTRARSE--")
                print("Ingrese su nombre: ")
                nombre_usuario = input()
                print("Ingrese su apellido: ")
                apellido_usuario = input()
                print("Ingrese su teléfono: ")
                teléfono_usuario = input()
                print("Ingrese su correo: ")
                correo_usuario = input()
                print("Ingrese una contraseña: ")
                contraseña_usuario = input()
                usuario = Usuario(Rol, nombre_usuario, apellido_usuario, teléfono_usuario, correo_usuario, contraseña_usuario)
                ListaSimple.add(usuario)
                print("Usuario registrado correctamente.")
                ListaSimple.Imprimir()

                print("¿Desea registrar otro usuario?")
                print("[1]. Sí")
                print("[2]. No")
                reg = input()
                if reg == "2":
                    ListaSimple.generar_archivo_XML()
                    break
                elif reg == "1":
                    continue

        elif opcion=="3":
            print("--USTED SE ENCUENTRA EN LA OPCIÓN VER LISTADO DE PELÍCULAS--")
            opcion_valida = True

        else:
            print("Opción inválida, vuelva a intentarlo.")
            mostrar_menu()
            opcion = input()
    opcion_valida=False