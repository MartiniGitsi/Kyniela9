from sqlalchemy import Column, DateTime, String, Integer, func
from database import Base  # Import Base from the database module


class Gatos(Base):
    __tablename__ = "gatos"
    id_gato = Column(Integer, primary_key=True)
    maullido = Column(String(60), unique=True)
    created_at = Column(DateTime, default=func.now())

    def __rep__(self):
        return f"id_gato: {self.id_gato}, plaqmaullidouita: {self.maullido}"
