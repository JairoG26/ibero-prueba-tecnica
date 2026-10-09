import Image from "next/image";
import api from "./api/server";
import {useState, useEffect} from "react";

const Table = () => {
  const [tareas, setTareas] = useState<any[]>([]);

  useEffect(() => {
    const fetchTareas = async () => {
      try {
        const response = await api.get("/tarea");
        setTareas(response.data);
      } catch (error) {
        console.error("Error fetching tareas:", error);
      }
    };

    fetchTareas();
  }, []);

  return (
    <div className="w-full">
      {tareas.length === 0 ? (
        <p className="text-zinc-600 dark:text-zinc-300">Cargando tareas...</p>
      ) : (
        <table className="w-full border-collapse text-left text-sm text-zinc-700 dark:text-zinc-200">
          <thead>
            <tr className="border-b border-zinc-200 dark:border-zinc-800">
              <th className="py-2 pr-4">ID</th>
              <th className="py-2 pr-4">Título</th>
              <th className="py-2 pr-4">Descripción</th>
              <th className="py-2 pr-4">Completada</th>WWWW
            </tr>
          </thead>
          <tbody>
            {tareas.map((tarea: any) => (
              <tr key={tarea.id} className="border-b border-zinc-100 dark:border-zinc-900">
                <td className="py-2 pr-4">{tarea.id}</td>
                <td className="py-2 pr-4">{tarea.titulo ?? "Sin título"}</td>
                <td className="py-2 pr-4">{tarea.descripcion ?? "Sin descripción"}</td>
                <td className="py-2 pr-4">{tarea.completada ? "Sí" : "No"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default function Home() {
  return (
    <div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex flex-1 w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">
        <div className="flex flex-col items-center justify-center w-full">
          <Table />
        </div>
      </main>
    </div>
  );
}
