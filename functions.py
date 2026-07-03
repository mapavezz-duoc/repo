def show_menu():
    print("====== Menú Principal ======")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Actualizar estados")
    print("5. Mostrar estudiante")
    print("6. Salir")
    print("============================")
    print("")

def get_option():
    try:
        option = int(input("Ingresa una opción (1-6): "))
    except ValueError:
        print("El valor ingresado no es válido")
    
    return option

def add_student(students):

    name = input("Ingresa el nombre del estudiante: ")
    if not valid_name(name):
        print("El nombre ingresado no es válido. El nombre no puede estar vacío ni ser solo espacios en blanco.")
        return
    
    age = input("Ingresa la edad del estudiante: ")
    if not valid_age(age):
        print("La edad ingresada no es válida. La edad debe ser un número entero mayor que 0.")
        return
    
    grade = input("Ingresa la nota del estudiante: ")
    if not valid_grade(grade):
        print("La nota ingresada no es válida. La nota debe ser un número decimal entre 1.0 y 7.0.")
        return

    students.append(create_student(name, age, grade))
    print("Estudiante agregado correctamente.")


def create_student(name, age, grade):
    return {
        "nombre": name,
        "edad": age,
        "nota": grade,
        "aprobado": False
    }

def valid_name(name):
    if name.strip() == "":
        return False
    return True

def valid_age(age):
    try:
        if int(age) < 0:
            return False
        return True
    except ValueError:
        return False

def valid_grade(grade):
    try:
        if not (1.0 <= float(grade) <= 7.0):
            return False
        return True
    except ValueError:
        return False 
    
