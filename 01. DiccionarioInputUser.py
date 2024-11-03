print("\n¡Hola! Comprobaremos tus datos.\n")

# Se solicitan datos al usuario:
Nombre = input("Ingrese su nombre: ")
Edad = int(input("Ingresa tu edad: "))
Dic1 = {}

# Estructura lógica:
if Edad >= 18:
    
    print("\n¡Puedes guardar tus datos!\n")
    Dic1['Nombre'] = Nombre
    Dic1['Edad'] = Edad
    Cargo = input("¿Cuál es tu cargo?: ").lower()
    Dic1['Cargo'] = Cargo

    # Condicional en caso de ser Jefe:
    if Cargo == "jefe":
        Empl = int(input("¿Cuántos empleados tienes a cargo?: "))
        Dic1['Empleados'] = Empl
        print(f"\nTus datos son: {Dic1}\n") 
# Si es menor de edad, no se muestra el diccionario:
else:
    print("\n¡No podemos mostrar lista! Eres menor de edad.\n") 