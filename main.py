from chessPictures import *
from interpreter import draw

fila1 = square.join(square.negative())
fila1 = fila1.horizontalRepeat(4)

fila2 = square.negative().join(square)
fila2 = fila2.horizontalRepeat(4)

tablero = fila1.under(fila2)
tablero = tablero.verticalRepeat(4)

draw(tablero)