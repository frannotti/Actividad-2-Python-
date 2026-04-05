def puntaje_ronda(puntajes_jueces):
    total = 0
    for puntaje in puntajes_jueces.values():
        total += puntaje 
    return total 


def ganador_ronda(scores):
    mejor_nombre = ""
    mejor_puntaje = 0
    for nombre in scores:
        puntaje = puntaje_ronda(scores[nombre])
        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje 
            mejor_nombre = nombre 
    return mejor_nombre, mejor_puntaje


def tabla_posiciones(puntaje_total, rondas_ganadas):
    nombres = list(puntaje_total.keys())
    for i in range(len(nombres)):
        for j in range(i + 1, len(nombres)):
            if puntaje_total[nombres[j]] > puntaje_total[nombres[i]]:
                nombres[i], nombres[j] = nombres[j], nombres[i]
    return nombres 
