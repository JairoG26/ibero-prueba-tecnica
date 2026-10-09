from backend.domain.entities.tarea import Tarea
from backend.domain.entities.tarea_crear import TareaCrear
from backend.application.service.tarea_service import TareaService
from backend.infrastructure.database.models import TareaModel
from backend.infrastructure.database.db_connection import DatabaseConnection
import os

db_url = "mysql+pymysql://root:12345@localhost/jairo_garavito"

class TareaRepositoryImpl(TareaService):

    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection

    def obtener_tareas(self):
        with self.db_connection.get_session() as session:
            tareas_model = session.query(TareaModel).all()
            return [Tarea(id=tarea.id, titulo=tarea.titulo, descripcion=tarea.descripcion, completada=tarea.completada) for tarea in tareas_model]

    def obtener_tarea_por_id(self, tarea_id: int):
        with self.db_connection.get_session() as session:
            tarea_model = session.query(TareaModel).filter(TareaModel.id == tarea_id).first()
            if tarea_model:
                return Tarea(id=tarea_model.id, titulo=tarea_model.titulo, descripcion=tarea_model.descripcion, completada=tarea_model.completada)
            return None

    def crear_tarea(self, tarea_crear: TareaCrear):
        with self.db_connection.get_session() as session:
            nueva_tarea = TareaModel(titulo=tarea_crear.titulo, descripcion=tarea_crear.descripcion, completada=tarea_crear.completada)
            session.add(nueva_tarea)
            session.commit()
            session.refresh(nueva_tarea)
            return Tarea(id=nueva_tarea.id, titulo=nueva_tarea.titulo, descripcion=nueva_tarea.descripcion, completada=nueva_tarea.completada)

    def actualizar_tarea(self, tarea_id: int, tarea_actualizar: TareaCrear):
        with self.db_connection.get_session() as session:
            tarea_model = session.query(TareaModel).filter(TareaModel.id == tarea_id).first()
            if tarea_model:
                tarea_model.titulo = tarea_actualizar.titulo
                tarea_model.descripcion = tarea_actualizar.descripcion
                tarea_model.completada = tarea_actualizar.completada
                session.commit()
                return Tarea(id=tarea_model.id, titulo=tarea_model.titulo, descripcion=tarea_model.descripcion, completada=tarea_model.completada)
            return None

    def eliminar_tarea(self, tarea_id: int):
        with self.db_connection.get_session() as session:
            tarea_model = session.query(TareaModel).filter(TareaModel.id == tarea_id).first()
            if tarea_model:
                session.delete(tarea_model)
                session.commit()
                return True
            return False