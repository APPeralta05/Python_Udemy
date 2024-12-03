##1

from pathlib import Path

# Obtener el directorio base del usuario
ruta_base = Path.home()

# Imprimir la ruta base para verificar
print(ruta_base)

##2

from pathlib import Path

ruta = Path("Curso Python","Día 6","practicas_path.py")

##3

from pathlib import Path

ruta = Path(Path.home(), "Curso Python","Día 6","practicas_path.py")
