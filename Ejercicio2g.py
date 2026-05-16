from interpreter import draw
from chessPictures import *


# fila negras
fila1 = (
    rock.negative()
    .join(knight.negative())
    .join(bishop.negative())
    .join(queen.negative())
    .join(king.negative())
    .join(bishop.negative())
    .join(knight.negative())
    .join(rock.negative())
)

# peones negros
fila2 = pawn.negative().horizontalRepeat(8)

# filas vacías
filaV1 = square.join(square.negative()).horizontalRepeat(4)
filaV2 = square.negative().join(square).horizontalRepeat(4)

centro = filaV1.under(filaV2).verticalRepeat(2)

# peones blancos
fila7 = pawn.horizontalRepeat(8)

# fila blancas
fila8 = (
    rock
    .join(knight)
    .join(bishop)
    .join(queen)
    .join(king)
    .join(bishop)
    .join(knight)
    .join(rock)
)

# tablero completo
tablero = (
    fila1
    .under(fila2)
    .under(centro)
    .under(fila7)
    .under(fila8)
)

draw(tablero)
