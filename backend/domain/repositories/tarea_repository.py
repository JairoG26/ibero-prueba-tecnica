from abc import ABC, abstractmethod
from typing import List, Optional
from backend.domain.entities.tarea import Tarea
from backend.domain.entities.tarea_crear import TareaCrear

class TareaRepository(ABC):
    @abstractmethod
    def obtener_tareas(self) -> List[Tarea]:
        pass

    @abstractmethod
    def obtener_tarea_por_id(self, tarea_id: int) -> Optional[Tarea]:
        pass

    @abstractmethod
    def crear_tarea(self, tarea_crear: TareaCrear) -> Tarea:
        pass

    @abstractmethod
    def actualizar_tarea(self, tarea_id: int, tarea_actualizar: TareaCrear) -> Optional[Tarea]:
        pass

    @abstractmethod
    def eliminar_tarea(self, tarea_id: int) -> bool:
        pass