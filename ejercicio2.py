def mostrar_menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Libros disponibles")
    print("2. Realizar prestamo")
    print("3. Devolver prestamo")
    print("4. Historial de prestamos")
    print("5. Reservar Libros")
    print("6. Salir")

def gestionar_biblioteca():
    stock_maximo = 120
    libros_disponibles = 120
    prestamos_activos = 0
    total_prestamos_realizados = 0

    print("Interfaz del programa")
    print("Bienvenido")
    print("¡Bienvenido al sistema de gestion de prestamos de la biblioteca central!")

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opcion"))
        except:
            print("Por favor, ingrese un numero valido")
            continue
        if opcion == 1:
            print(f"\nCantidad actual de libros libres:{libros_disponibles}")
        elif opcion == 2:
            print("\n --- Realizar Prestamo --- ")
            try:
                cantidad = int (input("Ingrese la cantidad de libros a prestar:"))
                if cantidad <=0:
                    print("Error: la cantidad no puede ser menor o igual a 0.")
                elif cantidad  > libros_disponibles:
                    print(f"Error: no debe superar el stock disponible ({libros_disponibles})")
                else:
                    libros_disponibles-= cantidad
                    prestamos_activos += cantidad
                    total_prestamos_realizados += 1
                    print(f"Prestamo realizado con exito. libros prestados:{cantidad}")
            except:
                print("Error: debe ingresar un numero entero.")
        elif opcion == 3:
            print("\n --- Devolver prestamo ---")
            try:
                cantidad = int(input("Ingrese la cantidad de libros a devolver:"))
                if cantidad <= 0:
                    print("Error: la cantidad debe ser mayor a 0.")
                elif libros_disponibles + cantidad > stock_maximo:
                    print(f"Error: no supere la cantidad maxima de la biblioteca ({stock_maximo} libros.")
                else:
                    libros_disponibles += cantidad
                    prestamos_activos -= cantidad
                    print(f"Devolucion realizada con exito. Libros devueltos: {cantidad}")
            except:
                print("Error : debe ingresar un numero entero")
        elif opcion == 4:
            print("\n--- Historial de prestamos ---")
            print(f"Prestamops activos actualmente:{prestamos_activos}")
            print(f"Total de prestamos realizados en la sesion:{total_prestamos_realizados}")
    
        elif opcion == 5:
            print("\n--- Reservar libros---")
            try:
                cantidad = int(input("Ingrese la cantidad de libros a reservar:"))
                if cantidad <= 0:
                    print("Error: la cantidad a reservar debe ser msyor a 0.")
                elif cantidad > libros_disponibles:
                    print(f"Error: no hay suficiente capacidad disponible. Solo quedan{libros_disponibles} libros.")
                else:
                    libros_disponibles -= cantidad
                    print(f"Reserva realizada con exito. Libros reservados:{cantidad}")
            except:
                print("Error: debe ingresar un numero entero.")

        elif opcion == 6:
            print("\nGracias por utilizar nuestro software, hasta la proxima" )
            break
        else: print("Opcion invalida. Intente nuevamente.")
gestionar_biblioteca()
            print("Opcion invalida. Intente nuevamente.")
gestionar_biblioteca()
