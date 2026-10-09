from pydantic import BaseModel, Field

class TareaCrear(BaseModel):
    titulo: str = Field(..., description="Título de la tarea")
    descripcion: str = Field(..., description="Descripción detallada de la tarea")
    completada: bool = Field(default=False, description="Estado de finalización de la tarea")
