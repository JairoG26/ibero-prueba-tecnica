from backend.domain.entities.tarea import Tarea
from backend.domain.entities.tarea_crear import TareaCrear

class TareaService:
    def __init__(self, tarea_repository):
        self.tarea_repository = tarea_repository

    def obtener_tareas(self):
        return self.tarea_repository.obtener_tareas()

    def obtener_tarea_por_id(self, tarea_id: int):
        return self.tarea_repository.obtener_tarea_por_id(tarea_id)

    def crear_tarea(self, tarea_crear: TareaCrear):
        return self.tarea_repository.crear_tarea(tarea_crear)

    def actualizar_tarea(self, tarea_id: int, tarea_actualizar: TareaCrear):
        return self.tarea_repository.actualizar_tarea(tarea_id, tarea_actualizar)

    def eliminar_tarea(self, tarea_id: int):
        return self.tarea_repository.eliminar_tarea(tarea_id)