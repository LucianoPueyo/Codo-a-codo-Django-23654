def get_int():
    ingreso_correcto = False
    cantidad = 0
    

    while not ingreso_correcto:
        user_input = input('Ingrese un número entero: ')
        cantidad = cantidad + 1
        try:
            valor = int(user_input)
        except ValueError:
            print('No es un entero válido. Intente nuevamente!')
        else:
            ingreso_correcto = True

        

    return valor


print(f"Número ingresado: {get_int()}")




