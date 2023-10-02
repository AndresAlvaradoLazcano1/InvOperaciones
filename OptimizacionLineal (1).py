import numpy as np
from scipy.optimize import linprog
print("Bienvenido, eliga una opción segun lo que necesite: \n")
print("Eliga una opción segun lo necesite")
principalMenu = int(input("Menú Principal: \n 1- Maximizar función por simlex \n 2- Minimizar función por simplex \n 0- Salir \n"))

while principalMenu != 0:
    if principalMenu == 1:
        #Validacion de datos para la introduccion de la cantidad de variables por parte del usuario 
        while True:
            try:
                num_variables = int(input("Introduce el numero de variables: "))
                convertir_variables = int(num_variables)
                break
            except ValueError:
                print("Por favor ingrese una cantidad valida de variables \n")
        FO = []
        #Validacion y solicitud de datos para la introduccion de la funcion objetivo por parte del usuario     
        for i in range(num_variables):
            while True:
                try:
                    coef = float(input(f"Introduce el coeficiente de la variable x{i + 1} de la funcion objetivo: "))
                    FO.append(-coef) 
                    convertir_coeficientes = float(FO[i])
                    break
                except ValueError:
                    print("Por favor ingrese correctamente los coeficientes de la funcion objetivo: \n")
        #Validacion y solicitud de datos para la introduccion del numero de restricciones
        while True:
            try:
                num_restricciones = int(input("Introduce el numero de restricciones: "))
                convertir_restricciones = int(num_restricciones)
                break
            except ValueError:
                print("Por favor ingrese una cantidad valida de restricciones \n")
        resLeft = []
        #Validacion y solicitud de datos para la introduccion de las restricciones del problema (lado izquierdo)
        for i in range(num_restricciones):
            restriccion = []
            while True:
                try:
                    for j in range(num_variables):
                        coef = float(input(f"Introduce el coeficiente de x{j + 1} en la restricción {i + 1}: "))
                        restriccion.append(coef)
                    resLeft.append(restriccion)
                    break
                except ValueError:
                    print("Por favor ingrese los elementos de manera correcta")
        resRight = []
        #Validacion y solicitud de datos para la introduccion de las restricciones del problema (lado derecho ; resultados)
        for i in range(num_restricciones):
            while True:
                try:
                    lado_derecho = float(input(f"Introduce el lado derecho de la restricción {i + 1}: "))
                    resRight.append(lado_derecho)
                    convertirRestriccionesDerecho = float(resRight[i])
                    break
                except ValueError:
                    print("Por favor ingrese el elemento de manera correcta \n")
    #Definir los limites de las variables en no negativas
        varLim = [(0, None)] * num_variables
    #Usando el modulo scipy.optimize para resolver el problema
        maxResultado = linprog(FO, A_ub=resLeft, b_ub=resRight, bounds=varLim, method='highs')
    #Imprimir resultados
        print("\n RESULTADO FINAL DE LA MAXIMIZACION: \n")
        print("El valor optimo es: ", -maxResultado.fun) 
        print("El valor de las variables de decision son: \n")
        for i, val in enumerate(maxResultado.x):
            print(f"x{i + 1} = {val}")
              
    elif principalMenu == 2:
        while True:
            try:
                num_variables = int(input("Introduce el numero de variables: "))
                convertir_variables = int(num_variables)
                break
            except ValueError:
                print("Por favor ingrese una cantidad valida de variables \n")
        FO = []
        #Validacion y solicitud de datos para la introduccion de la funcion objetivo por parte del usuario     
        for i in range(num_variables):
            while True:
                try:
                    coef = float(input(f"Introduce el coeficiente de la variable x{i + 1} de la funcion objetivo: "))
                    FO.append(coef) 
                    convertir_coeficientes = float(FO[i])
                    break
                except ValueError:
                    print("Por favor ingrese correctamente los coeficientes de la funcion objetivo: \n")
        #Validacion y solicitud de datos para la introduccion del numero de restricciones
        while True:
            try:
                num_restricciones = int(input("Introduce el numero de restricciones: "))
                convertir_restricciones = int(num_restricciones)
                break
            except ValueError:
                print("Por favor ingrese una cantidad valida de restricciones \n")
        resLeft = []
        #Validacion y solicitud de datos para la introduccion de las restricciones del problema (lado izquierdo)
        for i in range(num_restricciones):
            restriccion = []
            while True:
                try:
                    for j in range(num_variables):
                        coef = float(input(f"Introduce el coeficiente de x{j + 1} en la restricción {i + 1}: "))
                        restriccion.append(coef)
                    resLeft.append(restriccion)
                    break
                except ValueError:
                    print("Por favor ingrese los elementos de manera correcta")
        resRight = []
        #Validacion y solicitud de datos para la introduccion de las restricciones del problema (lado derecho ; resultados)
        for i in range(num_restricciones):
            while True:
                try:
                    lado_derecho = float(input(f"Introduce el lado derecho de la restricción {i + 1}: "))
                    resRight.append(lado_derecho)
                    convertirRestriccionesDerecho = float(resRight[i])
                    break
                except ValueError:
                    print("Por favor ingrese el elemento de manera correcta \n")
    #Definir los limites de las variables en no negativas
        varLim = [(0, None)] * num_variables
    #Usando el modulo scipy.optimize para resolver el problema
        minResultado = linprog(FO, A_ub=resLeft, b_ub=resRight, bounds=varLim, method='highs')
    #Imprimir resultados
        print("\n RESULTADO FINAL DE LA MINIMIZACION: \n")
        print("El valor optimo es: ", minResultado.fun) 
        print("El valor de las variables de decision son: \n")
        for i, val in enumerate(minResultado.x):
            print(f"x{i + 1} = {val}")    
    else:
        print("Esta opcion no es valida, elige una opcion correcta \n")
    principalMenu = int(input("Menú Principal: \n 1- Maximizar función por simlex \n 2- Minimizar función por simplex \n 0- Salir \n"))
