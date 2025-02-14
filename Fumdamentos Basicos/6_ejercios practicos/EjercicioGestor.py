#Gestor de Lista de Tareas
# Crear un gestor de tareas que:
# - Permita añadir tareas
# - Marcar tareas como completadas
# - Eliminar tareas
# - Mostrar todas las tareas


import json
import os
from datetime import datetime

class GestorTareas:
    def __init__(self):
        self.tareas = []
        self.archivo = "tareas.json"
        self.cargar_tareas()

    def cargar_tareas(self):
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r') as f:
                    self.tareas = json.load(f)
        except:
            self.tareas = []

    def guardar_tareas(self):
        with open(self.archivo, 'w') as f:
            json.dump(self.tareas, f, indent=4)

    def agregar_tarea(self, descripcion):
        tarea = {
            "id": len(self.tareas) + 1,
            "descripcion": descripcion,
            "completada": False,
            "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tareas.append(tarea)
        self.guardar_tareas()

    def marcar_completada(self, id_tarea):
        for tarea in self.tareas:
            if tarea["id"] == id_tarea:
                tarea["completada"] = True
                self.guardar_tareas()
                return True
        return False

    def eliminar_tarea(self, id_tarea):
        for tarea in self.tareas:
            if tarea["id"] == id_tarea:
                self.tareas.remove(tarea)
                self.guardar_tareas()
                return True
        return False

    def mostrar_tareas(self):
        if not self.tareas:
            return "No hay tareas registradas"
        
        resultado = "\nLISTA DE TAREAS:\n"
        for tarea in self.tareas:
            estado = "✓" if tarea["completada"] else "✗"
            resultado += f"\n{tarea['id']}. [{estado}] {tarea['descripcion']}"
            resultado += f"\n   Creada: {tarea['fecha_creacion']}"
        return resultado

def main():
    gestor = GestorTareas()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== GESTOR DE TAREAS ===")
        print("\n1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Eliminar tarea")
        print("4. Mostrar tareas")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción (1-5): ")
        
        if opcion == "1":
            descripcion = input("\nIngrese la descripción de la tarea: ")
            gestor.agregar_tarea(descripcion)
            print("\nTarea agregada con éxito")
            
        elif opcion == "2":
            print(gestor.mostrar_tareas())
            try:
                id_tarea = int(input("\nIngrese el ID de la tarea a completar: "))
                if gestor.marcar_completada(id_tarea):
                    print("\nTarea marcada como completada")
                else:
                    print("\nTarea no encontrada")
            except ValueError:
                print("\nPor favor, ingrese un ID válido")
                
        elif opcion == "3":
            print(gestor.mostrar_tareas())
            try:
                id_tarea = int(input("\nIngrese el ID de la tarea a eliminar: "))
                if gestor.eliminar_tarea(id_tarea):
                    print("\nTarea eliminada con éxito")
                else:
                    print("\nTarea no encontrada")
            except ValueError:
                print("\nPor favor, ingrese un ID válido")
                
        elif opcion == "4":
            print(gestor.mostrar_tareas())
            
        elif opcion == "5":
            print("\n¡Hasta luego!")
            break
            
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()