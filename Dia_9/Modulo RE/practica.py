import re

texto = 'Si necesitas ayuda llama al (658)-5989977 las 24 horas al servicio de ayuda' 


patron = 'ayuda'

busqueda = re.search(patron, texto)
busqueda2 = re.findall(patron, texto)

print(busqueda.span())
print(busqueda.start())
print(busqueda.end())
print(busqueda2.span())
print(busqueda2.start())
print(busqueda2.end())