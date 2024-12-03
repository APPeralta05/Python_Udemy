#1

from datetime import date

mi_fecha = date(1999, 2, 3)

#2

from datetime import date

fecha = date(1999, 2, 3)

#3

from datetime import datetime

# Obtener la hora actual
hora_actual = datetime.now()

# Extraer los minutos
minutos = hora_actual.minute

# Mostrar los minutos
print(minutos)