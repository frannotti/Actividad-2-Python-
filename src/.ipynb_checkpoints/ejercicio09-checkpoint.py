def eliminar(lista):
    for alumno in lista.copy():
        if alumno["name"] is None or alumno["name"].strip() == "":
            lista.remove(alumno)
        elif alumno["grade"] is None or alumno["grade"].strip() == "" or not alumno["grade"].isdigit():
            lista.remove(alumno)
            
    # normalizo nombres y estatus         
    for alumno in lista:
        alumno["name"] = alumno["name"].strip().title()
        alumno["status"] = alumno["status"].strip().title()
        alumno["grade"] = int(alumno["grade"])
   # elimino duplicados 
    mejores = {}
    for alumno in lista:
        nombre = alumno["name"]
        if nombre not in mejores or alumno["grade"] > mejores[nombre]["grade"]:
            mejores[nombre] = alumno 

    # ordenar alfabeticamente 
    ordenados = sorted(mejores.keys())
    nueva = []
    for nombre in ordenados:
        nueva.append(mejores[nombre])
    return nueva