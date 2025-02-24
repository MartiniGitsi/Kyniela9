from sqlalchemy import Column, DateTime, String, Integer, func
from database import Base  # Import Base from the database module


class Perros(Base):
    __tablename__ = "perros"
    id_perro = Column(Integer, primary_key=True)
    plaquita = Column(String(60), unique=True)
    created_at = Column(DateTime, default=func.now())

    def __rep__(self):
        return f"id_perro: {self.id_perro}, plaquita: {self.plaquita}"
