from app.database.base import Base
from app.database.session import engine

# Importar TODOS los modelos
from app.models.user import User
from app.models.product import Product
from app.models.sale import Sale

Base.metadata.create_all(bind=engine)

print("Base de datos creada exitosamente.")