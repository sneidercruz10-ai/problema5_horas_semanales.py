# Fase 5 - Evaluación Final POA (Fundamentos de Programación - 213022)
# Problema 5: Cálculo de horas semanales y clasificación de jornada laboral

# Matriz con 4 recursos: [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]
horas_equipo = [
    ["Camila Rojas", 8, 8, 9, 8, 8],
    ["Andrés Torres", 9, 9, 8, 9, 8],
    ["Valeria Gómez", 8, 7, 8, 8, 7],
    ["Mateo Díaz", 10, 8, 9, 8, 8]
]

UMBRAL_HORAS = 40


def evaluar_jornada(fila_recurso):
    """Calcula el total de horas semanales y clasifica la jornada laboral."""
    nombre = fila_recurso[0]
    horas_dias = fila_recurso[1:]
    total_horas = sum(horas_dias)

    if total_horas > UMBRAL_HORAS:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario estándar"

    return nombre, total_horas, clasificacion


def mostrar_reporte(matriz_horas):
    """Imprime el informe de horas semanales y clasificación por recurso."""
    print("=" * 60)
    print("REPORTE SEMANAL DE HORAS Y JORNADA LABORAL")
    print("=" * 60)
    for fila in matriz_horas:
        nombre, total, jornada = evaluar_jornada(fila)
        print(f"Recurso: {nombre:<15} | Total horas: {total:<3} | Jornada: {jornada}")
    print("=" * 60)


if __name__ == "__main__":
    mostrar_reporte(horas_equipo)