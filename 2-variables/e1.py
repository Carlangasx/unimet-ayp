import typing

volumen_reservorio: float = 4.445e8
lluvia: float = 5e6
# disminuir la variable de lluvia en un 10% para tener en cuenta el agua de lluvia que circula libremente sobre la superficie de un terreno.
lluvia *= 0.9
# Agregue la variable de lluvia a la variable volumen_reservorio.
volumen_reservorio += lluvia
# Aumentar volumen_reservorio en un 5% para tener en cuenta las aguas pluviales que fluyen en el embalse en los días posteriores a la tormenta.
volumen_reservorio *= 1.05
# Disminuir volumen_reservorio en un 2% para tener en cuenta la evaporación.
volumen_reservorio *= 0.98
# Resta 2.5e5 metros cúbicos de volumen_reservorio para tener en cuenta el agua que se canaliza a regiones áridas.
volumen_reservorio -= 2.5e5
# Imprime el nuevo valor de la variable volumen_reservorio.
print(volumen_reservorio)
