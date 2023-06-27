
def prueba(lst, result=False):
    # Variables
    number_list = []
    number_2_list = []
    operator_list = []
    result_list = []
    delimiter_list = []
    delimiter = '-'
    # position_list = [0, 0, 0]
    pos_1 = 0
    pos_3 = 0

    # valida si la lista tiene mas de 5 elementos
    if len(lst) > 5:
        return "Error: Too many problems."    
        
    # iterar la lista pasada como parametro
    for var in lst:
        add = var.find(' ') + 1
        x = var.partition(' ' + var[add] + ' ')
        y = var.partition('' + var[add:])
        num1, ope, num2 = x
        new_oper = ope.strip()
        cont1 = len(num1)
        cont2 = len(num2)
       
        # Valida si la cadena tiene alguna cadena o letra
        try:
            temp_number = []
            temp_signo = [' * ', ' / ']
            temp_number.append(int(num1))
            temp_number.append(int(num2))

            # Valida los operadores permitidos solo son '+' or '-'
            if ope in temp_signo:
                return "Error: Operator must be '+' or '-'. "
            
            # Valida si los numeros no son mayores a 4 digitos
            if len(num1) > 4 or len(num2) > 4:
                return "Error: Numbers cannot be more than four digits."

        except ValueError:
            return "Error: Numbers must only contain."
        
        # Valida la justificacion y union entre el signo y el 2 numero
        if (cont2 == 4 and cont1 == 4) or (cont2 == 4 and cont1 == 3) or (cont2 == 4 and cont1 == 2) or (cont2 == 4 and cont1 == 1) or (cont2 == 3 and cont1 == 3) or (cont2 == 3 and cont1 == 2) or (cont2 == 3 and cont1 == 1) or (cont2 == 2 and cont1 == 2) or (cont2 == 2 and cont1 == 1) or (cont2 == 1 and cont1 == 1):
            new_var = new_oper + ' ' + num2
        elif (cont2 == 3 and cont1 == 4) or (cont2 == 2 and cont1 == 3) or (cont2 == 1 and cont1 == 2):
            new_var = new_oper + '  ' + num2
        elif (cont2 == 2 and cont1 == 4) or (cont2 == 1 and cont1 == 3):
            new_var = new_oper + '   ' + num2
        elif cont2 == 1 and cont1 == 4:
            new_var = new_oper + '    ' + num2

        # calcula la cantidad de '-' para trazar la linea de la operacion
        if cont1 == 4 or cont2 == 4:
            d1 = delimiter * 6
            delimiter_list.append(d1)
        elif cont1 == 3 or cont2 == 3:
            d1 = delimiter * 5
            delimiter_list.append(d1)
        elif cont1 == 2 or cont2 == 2:
            d1 = delimiter * 4
            delimiter_list.append(d1)
        elif cont1 == 1 or cont2 == 1:
            d1 = delimiter * 3
            delimiter_list.append(d1)

        #Valida posicion
        if cont1 == 4 or cont2 == 4:
            pos_1 = 6
            pos_3 = pos_1
        elif cont1 == 3 or cont2 == 3:
            pos_1 = 5
            pos_3 = pos_1
        elif cont1 == 2 or cont2 == 2:
            pos_1 = 4
            pos_3 = pos_1
        elif cont1 == cont2:
            pos_1 = 3
            pos_3 = pos_1
        
        # agrega los valores filtrados en las listas vacias
        number_list.append(num1.rjust(pos_1))
        number_2_list.append(num2)
        operator_list.append(new_var)

        # Valida si es suma o resta, realiza la operacion y la guarda en la lista
        if ope == ' + ':
            suma = int(num1) + int(num2)
            result_list.append(str(suma).rjust(pos_3))

        elif ope == ' - ':
            resta = int(num1) - int(num2)
            result_list.append(str(resta).rjust(pos_3))

    # Convierte las listas en cadenas, separadas x 4 espacios
    Value_top       = '    '.join(number_list)
    Value_final     = '    '.join(result_list)
    value_delimiter = '    '.join(delimiter_list)
    value_bottom    = '    '.join(operator_list)
  
    # Concatena el resultado 
    if result == True:
        variable = Value_top + '\n' +  value_bottom + '\n' + value_delimiter + '\n' + Value_final + '\n'
    else:
        variable = Value_top + '\n' +  value_bottom + '\n' + value_delimiter + '\n'
    
    return variable


print(prueba(["1 + 6", "3 - 17", "4 + 130", "4 + 1675"], True))
print(prueba(["12 + 6", "43 - 17", "74 + 130", "74 + 2341"], True))
print(prueba(["123 + 6", "123 - 17", "123 + 130", "123 + 1987"], True))
print(prueba(["1234 + 6", "3456 - 17", "7890 + 130", "4444 + 1234"], True))

print(prueba(["1 + 6", "32 - 1", "423 + 3", "4654 + 1"], True))
print(prueba(["3 + 62", "43 - 17", "374 + 30", "7445 + 41"], True))
print(prueba(["1 + 675", "23 - 717", "123 + 130", "1236 + 987"], True))
print(prueba(["4 + 6234", "56 - 2117", "7890 + 1530", "4444 + 1234"], True))