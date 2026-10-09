from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

class TareaModel(declarative_base()):
    __tablename__ = "tarea"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    completada = Column(Boolean, default=False)
