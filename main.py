
comentarios = []

def showMenu():
    print(f""" Bienvenido al menú de comentarios
        1. Registrar un comentario.
        2. Mostrar todos los comentarios registrados.
        3. Buscar comentarios que contengan una palabra indicada.
        4. Mostrar la cantidad de palabras de cada comentario.
        5. Contar cuántas veces aparece una palabra en un comentario seleccionado.
        6. Mostrar un resumen del comentario seleccionado: número de caracteres, número de
        palabras y número de apariciones de la palabra buscada.
        0. Salir.""")

    selectOption()

def selectOption():

    option = int(input("Seleccione una opción: "))
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    elif option == 4:
        option4()
    elif option == 5:
        option5()
    elif option == 6:
        option6()  
    else: print("Finalizando programa.")

def returnMenu():
    goBackMenu = input("Presioa [Enter] para volver al menú principal")
    showMenu()

def option1():
    while True:
        texto = input("Escriba el comentario: ").strip()
        if texto != "":
            comentarios.append(texto)
            print("Comentario registrado.")
        else:
            print("El comentario no puede estar vacío.")

        reTry = input("¿Deseas poner otro comentario? s/n").lower()

        if not "s" in reTry:
            returnMenu()
            break

def option2():
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
    else:
        for i in range(len(comentarios)):
            print(i + 1, comentarios[i])

    returnMenu()

def option3():
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

        returnMenu()

def option4():
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
    else:
        for i in range(len(comentarios)):
            palabras = comentarios[i].split()
            print(f"Comentario #{i + 1} tiene {len(palabras)} palabras.")

    returnMenu()


def option5():
    while True:
        count = 0
        index = int(input("¿Que indicie? ")) - 1
        search = input("Escribe la palabra que deseas consultar: ").strip().lower()
        words = comentarios[index].lower()

        if len(comentarios) == 0:
            print("No hay comentarios registrados.")

        if search in comentarios:

            print(f"Se ha encontrado la palabra {search} un total de {words.count(search)} veces")
        else: print("Esta palabra no ha sido encontrada.")

        reTry = input("¿Desea buscar una palabra nuevamente? s/n").lower()

        if not "s" in reTry:
            returnMenu()
            break

def option6():
    global words, index 
    select = int(input("Seleccione un comentario (indice) ")) - 1
    print(f"""RESUMEN
    Comentario {comentarios[select]}
    Cracteres {len(comentarios[select])}""")

showMenu()
         
