from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()
metadata = Base.metadata
