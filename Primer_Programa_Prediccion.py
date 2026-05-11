#pregunta al usuario la calificacion y la guarda en la variable cali
cali = int(input("Escribe tu calificacion para saber si aprovaste o reprobaste"))
#el if pregunta si cali es mayor o menor a 7 y escribe el mensaje correspondiente de la calificacion-+
if cali >= 7:
    print("Aprobaste")
else:
    print("Reprobaste")