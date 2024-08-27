def find_one(list,needle):
    """
    Devuelve True si encuentra una o más ocurrencias de needle en list
    """
    return find_n(list, needle, 1)


def find_n(list, needle, n):
    """
    Devuelve True si hay n o más ocurrencias de needle
    False si hay menos o si n<1
    """
    # Si n>0
    if n>=0:
        # Inicializamos el índice y el contador
        index=0
        count=0
        # Mientras no hayamos encontrado al elemento n veces o no hayamos terminado la lista...
        while count <n and index<len(list):
            # Si lo encontramos actualizamos el contador
            if needle==list[index]:
                count+=1
            # Avanzamos al siguiente elemento
            index+=1
        # Devolvemos el resultado de comparar el contador con n
        return count>=n
    else:
        return False


def find_streak(list, needle, n):
    """
    Devuelve True cuando enccuentra una racha (si en list hay n o más needles seguidos)
    False para todo lo demás
    """
    # Si n>=0
    if n>=0:
        # Inicializo el indice el contador y el indicador de racha
        index=0
        count=0
        streak=False
        # Mientras no haya encontrado n seguidos y la lista no se haya acabado...
        while count<n and index<len(list):
            # Si lo encuentro, activo el indicador de rachas y actualizo el contador
            if list[index]==needle:
                count+=1
                streak=True
            # Si no lo encuentro, desactivo el indicador de racha y pongo a 0 el contador
            else:
                count=0
                streak=False
            # Avanzo al siguiente elemento
            index+=1
        # Devolvemos el resultado de comparar el contador con n SI Y SOLO SI estamos en racha
        return count>=n and streak
    else: 
        return False