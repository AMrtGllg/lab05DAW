from interpreter import draw
from chessPictures import *

fila_sup = knight.join(knight.negative())
fila_inf = knight.negative().join(knight)

figura_a = fila_sup.under(fila_inf)

draw(figura_a)