import pytest

from square_board import *
from linear_board import *

def test_empty_board():
    board=SquareBoard()
    
    assert board.is_full()==False
    assert board.is_victory('o')==False
    assert board.is_victory('x')==False
    
def test_vertical_victory():
    vertical=SquareBoard.fromList([['o','x','x','x'],
                                  [None,None,None,None],
                                  [None,None,None,None],
                                  [None,None,None,None]])
    assert vertical.is_victory('x')
    assert vertical.is_victory('o')==False

def test_horizontal_victory():
    horizontal=SquareBoard.fromList([['x',None,None,None,None],
                                     ['x','o',None,None,None],
                                     ['x','o',None,None,None],
                                     ['x','o',None,None,None]])
    assert horizontal.is_victory('x')

def test_sinking_victory():
    sinking=SquareBoard.fromList([['x','o','x','o'],
                                  ['x','x','o',None],
                                  ['o','o',None,None],
                                  ['o','x',None,None],
                                  ['x',None,None,None]])
    assert sinking.is_victory('o')
    assert sinking.is_victory('x')==False

def test_rising_victory():
    rising=SquareBoard.fromList([['x','o',None,None],
                                 ['o','x',None,None],
                                 ['x','o','x','o'],
                                 ['x','o','o','x'],
                                 ['o','x','o',None]])
    assert rising.is_victory('x')
    assert rising.is_victory('o')==False