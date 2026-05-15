from interpreter import draw
from chessPictures import *

fila_sup = knight.join(knight.negative())
fila_inf = knight.negative().verticalMirror().join(knight.verticalMirror())

figura_b = fila_sup.under(fila_inf)

draw(figura_b)