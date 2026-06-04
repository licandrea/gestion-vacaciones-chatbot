empleados = {
    1001: {"nombre": "Andrea", "dias_disponibles": 15},
    1002: {"nombre": "Juan", "dias_disponibles": 10},
    1003: {"nombre": "María", "dias_disponibles": 20}
}

legajo = int(input("Ingrese su legajo: "))
dias_solicitados = int(input("Ingrese la cantidad de días solicitados: "))

if legajo in empleados:
    if dias_solicitados <= empleados[legajo]["dias_disponibles"]:
        print("Solicitud aprobada")
    else:
        print("Solicitud rechazada: no posee días suficientes")
else:
    print("Legajo inexistente")
