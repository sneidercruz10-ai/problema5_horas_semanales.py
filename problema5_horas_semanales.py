# Problema 5: Calculo de horas semanales de un equipo

empleados = [
    ["Camila Rojas", [8, 9, 8, 8, 8]],
    ["Andres Torres", [9, 8, 9, 9, 8]],
    ["Valeria Gomez", [8, 7, 8, 8, 7]],
    ["Mateo Diaz", [8, 9, 9, 8, 9]]
]

def calcular_horas(horas_dias):
    total = 0
    for h in horas_dias:
        total = total + h
    return total

def tipo_jornada(total_horas):
    if total_horas > 40:
        return "Sobretiempo"
    else:
        return "Horario estandar"

print("--- Reporte semanal de horas ---")
for persona in empleados:
    nombre = persona[0]
    horas = persona[1]
    total = calcular_horas(horas)
    jornada = tipo_jornada(total)
    print(nombre, "| Total horas:", total, "| Jornada:", jornada)
