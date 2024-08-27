from settings import BOARD_LENGTH, VICTORY_STRIKE
from list_utils import find_streak

class LinearBoard():
    """
    Clase que representa un tablero de una sola columna
    x es un jugador
    o es otro jugador
    None es un espacio vacío
    """
    @classmethod
    def fromList(cls,list):
        board=cls()
        board._column=list
        return board


    def __init__(self):
        """
        una lista de None
        """
        self._column=[None for i in range(BOARD_LENGTH)]
    
    def add(self,char):
        """
        Juega en la primera posicion disponible
        Las llamadas a add cuando  el tablero esté lleno no harán nada
        """
        # Comprobamos si el tablero está lleno para poder añadir una ficha
        if not self.is_full():
        
            # buscamos la primera posicion libre (None)
            i=self._column.index(None)

            #lo sustituimos pr char
            self._column[i]=char

    def is_full(self):
        return self._column[-1]!=None
        
    def is_victory(self,char):
        return find_streak(self._column, char, VICTORY_STRIKE)
    
    def is_tie(self,char1,char2):
        """
        No hay victoria ni de char1 ni de char2
        """
        return (self.is_victory('x')==False) and (self.is_victory('o')==False)