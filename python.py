import functions as f

students = []

breaker = False

while not breaker:

    f.show_menu()

    option = f.get_option()
    
    if option == 1:
        f.add_student(students)
    elif option == 2:
        print("")
    elif option == 3:
        print("")
    elif option == 4:
        print("")
    elif option == 5:
        print("")
    elif option == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        breaker = True
    else:
        print("La opción ingresada no es válida. Intenta nuevamente.")