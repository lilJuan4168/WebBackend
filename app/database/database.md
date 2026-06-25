<p>
aqui se define toda la configuracion de la base de datos.

1. from sqlalchemy.orm import declarative_base
Estás importando una función que pertenece al sistema Declarativo de SQLAlchemy. Este sistema te permite definir cómo serán las tablas de tu base de datos usando clases normales de Python.
2. Base = declarative_base()
Aquí estás ejecutando esa función y guardando el resultado en una variable llamada Base.
Base es ahora una clase herencia (o clase base). A partir de este momento, cualquier clase de Python que tú crees y que herede de Base se convertirá automáticamente en una tabla en tu base de datos.

y en session.py se declara toda la configuracion de conexion de la api
</p>