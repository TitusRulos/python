#Ejercicio 1.
    #n=str(input("ingresa tu nombre: "))
    #print("Hola", n)

#Ejercicio 2.
    #import math as mt
    #r=float(input("ingrese el radio: "))
    #p=(2*(mt.pi))*r
    #a=(mt.pi)*((r)**2)
    #print("El perímetro es ", p)
    #print("El área es ", a)

#Ejercicio 3.
    #a=float(input("Primer nota: "))
    #b=float(input("Segunda nota: "))
    #c=float(input("Tercera nota: "))
    #d=float(input("Cuarta nota: "))
    #prom=((a+b+c+d)/(4))
    #print(prom)

#Ejercicio 4.
    #cm=float(input("Ingrese longitud: "))
    #IN=cm/2.54
    #print(int(cm), "cm =45", IN,"in"  )

#Ejercicio 5.
    #c1=float(input("Ingrese cateto a: "))
    #c2=float(input("Ingrese cateto b: "))
    #h=(((c1)**2)+((c2)**2))**(1/2)
    #print("La hipotenusa es ",h)

#Ejercicio 6.
    #t=int(input("Hora actual: "))
    #h=int(input("Cantidad de horas: "))
    #tFutura=((t+h)%24)
    #print("En {} horas, el reloj marcara las {}".format(t, tFutura))

#Ejercicio 7.
 #import math as mt
 #num=float(input("Ingrese un número: "))
 #Entera=mt.trunc(num)
 #rta=(abs(num)-Entera)
 #print(round(rta,1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000))

#Ejercicio 8. 
 #nota1=int(input("ingrese nota certamen 1: "))
 #nota2=int(input("ingrese nota certamen 2: "))
 #lab=int(input("ingrese nota laboratorio: "))
 #nota3=((((60-(lab*0.3))*30)/7)-(nota1+nota2))
 #print("Necesita nota", int(nota3), "en el certamen 3")

#Ejercicios 9.
 #palabra1=str(input("palabra 1: "))
 #palabra2=str(input("palabra 2: "))
 #if len(palabra1)>len(palabra2):
 #    dif=(len(palabra1)-(len(palabra2)))
 #    print("la palabra {} tiene {} letras de mas que {}.".format(palabra1, dif, palabra2))
 #elif len(palabra2)>len(palabra1):
 #    dif=(len(palabra2)-(len(palabra1)))
 #    print("la palabra {} tiene {} letras de mas que {}.".format(palabra2, dif, palabra1))
 #else:
 #    print("Las dos palabras tienen el mismo largo")

# Ejercicio 10.  
# import datetime as dt
# def es_bisiesto(año):
#     return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
# def fecha_valida(dia, mes, año):
#     dias_por_mes = {
#         1: 31,
#         2: 29 if es_bisiesto(año) else 28,
#         3: 31, 
#         4: 30,
#         5: 31,
#         6: 30,
#         7: 31, 
#         8: 31,
#         9: 30,
#         10: 31, 
#         11: 30, 
#         12: 31
#     }
#     if mes < 1 or mes > 12:
#         return False
#     if dia < 1 or dia > dias_por_mes[mes]:
#         return False
#     return True
# def calcular_edad(fecha_nacimiento):
#     fecha_actual = dt.datetime.now()
#     edad = fecha_actual.year - fecha_nacimiento.year
#     if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
#         edad -= 1
#     return edad
# def obtener_fecha_de_nacimiento():
#     print("Ingrese su nacimiento")
#     dia = int(input("Día: "))
#     mes = int(input("Mes: "))
#     año = int(input("Año: "))
#     return dt.datetime(año, mes, dia)
# fecha_nacimiento = obtener_fecha_de_nacimiento()
# if fecha_valida(fecha_nacimiento.day, fecha_nacimiento.month, fecha_nacimiento.year):
#     print("La fecha es válida")
#     edad = calcular_edad(fecha_nacimiento)
#     print(f"Su edad es {edad} años.")
# else:
#     print("La fecha no es válida")

#Ejercicio 11.
# numeros=int(input("cantidad de números: "))
# ordenamiento=[]
# for i in range (numeros):
#     num=int(input(f"numero {i+1}: "))
#     ordenamiento.append(num)
# for i in range(len(ordenamiento)):
#     for j in range(i+1, len(ordenamiento)):
#         if ordenamiento[i]>ordenamiento[j]:
#             ordenamiento[j], ordenamiento[i]=ordenamiento[i], ordenamiento[j]
# print(ordenamiento)

#Ejercicio 12.
# estatura, peso, edad= float(input("estatura: ")), float(input("peso: ")), int(input("edad: "))
# indice=(peso/(estatura**2))
# if indice<22 and edad<45:
#     print(f"bajo, indice: {round(indice, 2)}")
# elif indice<22 and edad>=45:
#     print(f"medio, indice {round(indice, 2)}")
# elif indice>=22 and edad<45:
#     print(f"medio, indice {round(indice, 2)}")
# elif indice>=22 and edad>=45:
#     print(f"alto, indice {round(indice, 2)}")

#Ejercicio 13.





           
    






    












