from app.database.base import Base
from app.database.session import engine

# Importar TODOS los modelos
from app.models.user import User
from app.models.products import Product
from app.models.sales import Sale

Base.metadata.create_all(bind=engine)

print("Base de datos creada exitosamente.")