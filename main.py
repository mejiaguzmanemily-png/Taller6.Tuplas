
comentarios = []

def registrar_comentario():
    texto = input("Escriba el comentario: ").strip()
    if texto != "":
        comentarios.append(texto)
        print("Comentario registrado.")
    else:
        print("El comentario no puede estar vacio.")

def mostrar_comentarios():
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
    else:
        for i in range(len(comentarios)):
            print(i + 1, comentarios[i])

def buscar_palabra():
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
    else:
        palabra = input("¿Qué palabra desea buscar? ").strip().lower()
        encontrado = False
        for i in range(len(comentarios)):
            if palabra in comentarios[i].lower():
                print(f"Encontrado en el comentario #{i + 1}: {comentarios[i]}")
                encontrado = True
        if not encontrado:
            print("No se encontró esa palabra en ningún comentario.")

def mostrar_cantidad_palabras():
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
    else:
        for i in range(len(comentarios)):
            palabras = comentarios[i].split()
            print(f"Comentario #{i + 1} tiene {len(palabras)} palabras.")

while True:
    print("\n--- MENÚ ---")
    print("1. Registrar un comentario")
    print("2. Mostrar todos los comentarios")
    print("3. Buscar comentarios que contengan una palabra")
    print("4. Mostrar la cantidad de palabras de cada comentario")
    print("5. Salir")
    
    opcion = input("Elija una opción: ")
    
    if opcion == "1":
        registrar_comentario()
    elif opcion == "2":
        mostrar_comentarios()
    elif opcion == "3":
        buscar_palabra()
    elif opcion == "4":
        mostrar_cantidad_palabras()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
         
