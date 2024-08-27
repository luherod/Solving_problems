import pytest
from list_utils import *

def test_find_one():
    needle=1
    # creamos un caso para cada tipo de situación
    # Situación 1:no hay needle:
    none=[0,0,5,'s']
    # Situación 1: needle está en la primera posición
    beginning=[1, None, 9,6,0,0]
    # Situación 2: needle está en la útima posición
    end=['x','0',1]
    # Situación 3: needle está varias veces
    several=[0,0,3,4,1,3,2,1,3,4]
    #recuerda que find_one(list,needle)
    assert find_one(none, needle)==False
    assert find_one(beginning, needle)
    assert find_one(end, needle)
    assert find_one(several, needle)


def test_find_n():
    # find_n(list, needle, cantidad_de_veces)
    # creamos un caso para cada tipo de situación

    # Situación 1:número de ocurrencias negativo:
    assert find_n([1,2,3,4,5,6],2,-1)==False
    # Situación 2:no está la aguja
    assert find_n([1,2,3,4,5,6],42,2)==False
    # Situación 3: está la aguja pero no el número de veces que debería
    assert find_n([1,2,3,4,5,6],1,2)==False
    # Situación 4: la aguja aparece el número de veces indicado
    assert find_n([1,2,3,2,4,5,6],2,2)
    # Situación 5: la aguja aparece más veces que el número de veces indicado
    assert find_n([1,2,3,4,5,4,6,4,7,4,6],4,2)
    # Situación 6: la aguja no tiene que aparecer ninguna vez y no aparece
    assert find_n([1,2,3,4,5,6],'x',0)

def test_find_streak():
    # Situación 1:número de ocurrencias negativo:
    assert find_streak([1,2,3,4,5],4,-1)==False
    # Situación 2:no está la aguja
    assert find_streak([1,2,3,4,5],42,2)==False
    # Situacion 3: se pide que la aguja aparezca una vez y se cumple
    assert find_streak([1,2,3,4],4,1)
    # Situacion 4: la aguja está el número de veces indicado pero no son veces seguidas
    assert find_streak([1,2,3,1,2],2,2)==False
    # Situación 5: se produce la racha solicitada al final
    assert find_streak([1,2,3,4,5,5,5],5,3)
    # Situación 6: se produce la racha solicitada al principio
    assert find_streak([5,5,5,1,2,3,4],5,3)
    # Situación 7: se produce la racha solicitada en el medio
    assert find_streak([1,2,5,5,5,3,4],5,3)
    # Hay una racha pero menor a la solicitada
    assert find_streak([1,2,3,4,5,5,5],5,4)==False

