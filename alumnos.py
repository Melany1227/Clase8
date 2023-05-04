def alumnos():
    alumnos = []
    respuesta = True
    while respuesta:
        alumno = []

        alumno.append(input("ingrese el nombre del alumno: \n"))
        alumno.append(float(input("ingrese la primera nota: \n")))
        alumno.append(float(input("ingrese la segunda nota: \n")))
        alumno.append(float(input("ingrese la cuarta nota: \n")))
        alumno.append(float(input("ingrese la quinta nota: \n")))

        alumnos.append(alumno)

        respuesta = input("Desea ingresar otro alumno?\n ingrese s para si \n ingrese cualquier cosa para no")
        if respuesta == "s":
            respuesta= True
        else:
            respuesta = False

    if len(alumnos) > 0:
        print("listado de la nota de alumnos")
        print("nombre\t nota1\t nota2\t nota3")
        for alumno in alumnos:
            print(alumno[0]+"\t"+str(alumno[1])+"\t\t"+str(alumno[2])+"\t\t"+str(alumno[3]))

    if len(alumnos) > 0:
        print("\nlistado de los promedios de los alumnos")
        print("nombre\n promedio")
        for alumno in alumnos:
            promedio = (alumno[1]+alumno[2]+alumno[3])/3
            print(alumno[0]+"\t"+str(round(promedio,1)) )