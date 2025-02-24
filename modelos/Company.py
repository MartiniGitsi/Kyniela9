from sqlalchemy import Column, DateTime, String, Integer, func
from database import Base  # Import Base from the database module


class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True)
    created_at = Column(DateTime, default=func.now())
    inspired_at = Column(DateTime, default=func.now())

    def __rep__(self):
        return f"id: {self.id}, name: {self.name}"
