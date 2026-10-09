from backend.domain.entities.tarea import Tarea
from backend.domain.entities.tarea_crear import TareaCrear
from backend.infrastructure.database.db_connection import DatabaseConnection
from backend.infrastructure.repositories.tarea_repository_impl import TareaRepositoryImpl
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

db_url = "mysql+pymysql://root:12345@localhost/jairo_garavito"

tarea_repository: TareaRepositoryImpl = TareaRepositoryImpl(db_connection=DatabaseConnection(db_url=db_url))

@router.get("/tareas", response_model=list[Tarea])
def obtener_tareas():
    return tarea_repository.obtener_tareas()

@router.get("/tareas/{tarea_id}", response_model=Tarea)
def obtener_tarea_por_id(tarea_id: int):
    tarea = tarea_repository.obtener_tarea_por_id(tarea_id)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@router.post("/tareas", response_model=Tarea)
def crear_tarea(tarea_crear: TareaCrear):
    return tarea_repository.crear_tarea(tarea_crear)

@router.put("/tareas/{tarea_id}", response_model=Tarea)
def actualizar_tarea(tarea_id: int, tarea_actualizar: TareaCrear):
    tarea = tarea_repository.actualizar_tarea(tarea_id, tarea_actualizar)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@router.delete("/tareas/{tarea_id}", response_model=dict)
def eliminar_tarea(tarea_id: int):
    exito = tarea_repository.eliminar_tarea(tarea_id)
    if not exito:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"mensaje": "Tarea eliminada exitosamente"}