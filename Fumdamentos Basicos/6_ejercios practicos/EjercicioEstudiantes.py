#Sistema de Gestión de Estudiantes
# Crear un sistema que:
# - Permita registrar estudiantes con nombre y notas
# - Calcule promedio por estudiante
# - Muestre estadísticas del curso
# - Guarde y cargue datos en un archivo

import json
import os
from statistics import mean

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.notas = []
        
    def agregar_nota(self, nota):
        if 0 <= nota <= 100:
            self.notas.append(nota)
            return True
        return False
        
    def calcular_promedio(self):
        return mean(self.notas) if self.notas else 0
        
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "notas": self.notas
        }
        
    @classmethod
    def from_dict(cls, data):
        estudiante = cls(data["nombre"], data["edad"])
        estudiante.notas = data["notas"]
        return estudiante

class SistemaGestion:
    def __init__(self):
        self.estudiantes = {}
        self.archivo = "estudiantes.json"
        self.cargar_datos()
        
    def cargar_datos(self):
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r') as f:
                    data = json.load(f)
                    self.estudiantes = {
                        nombre: Estudiante.from_dict(datos)
                        for nombre, datos in data.items()
                    }
        except:
            self.estudiantes = {}
            
    def guardar_datos(self):
        with open(self.archivo, 'w') as f:
            json.dump({
                nombre: estudiante.to_dict()
                for nombre, estudiante in self.estudiantes.items()
            }, f, indent=4)
            
    def agregar_estudiante(self, nombre, edad):
        if nombre not in self.estudiantes:
            self.estudiantes[nombre] = Estudiante(nombre, edad)
            self.guardar_datos()
            return True
        return False
        
    def agregar_nota(self, nombre, nota):
        if nombre in self.estudiantes:
            if self.estudiantes[nombre].agregar_nota(nota):
                self.guardar_datos()
                return True
        return False
        
    def mostrar_estadisticas(self):
        if not self.estudiantes:
            return "No hay estudiantes registrados"
            
        resultado = "\nESTADÍSTICAS DEL CURSO:\n"
        promedios = []
        
        for nombre, estudiante in self.estudiantes.items():
            promedio = estudiante.calcular_promedio()
            promedios.append(promedio)
            resultado += f"\n{nombre}:"
            resultado += f"\n  Edad: {estudiante.edad}"
            resultado += f"\n  Notas: {estudiante.notas}"
            resultado += f"\n  Promedio: {promedio:.2f}\n"
            
        if promedios:
            resultado += f"\nPromedio del curso: {mean(promedios):.2f}"
            resultado += f"\nMejor promedio: {max(promedios):.2f}"
            resultado += f"\nPeor promedio: {min(promedios):.2f}"
            
        return resultado

def main():
    sistema = SistemaGestion()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== SISTEMA DE GESTIÓN DE ESTUDIANTES ===")
        print("\n1. Agregar estudiante")
        print("2. Agregar nota")
        print("3. Ver estadísticas")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == "1":
            nombre = input("\nNombre del estudiante: ")
            try:
                edad = int(input("Edad del estudiante: "))
                if sistema.agregar_estudiante(nombre, edad):
                    print("\nEstudiante agregado con éxito")
                else:
                    print("\nEl estudiante ya existe")
            except ValueError:
                print("\nPor favor, ingrese una edad válida")
                
        elif opcion == "2":
            nombre = input("\nNombre del estudiante: ")
            try:
                nota = float(input("Nota (0-100): "))
                if sistema.agregar_nota(nombre, nota):
                    print("\nNota agregada con éxito")
                else:
                    print("\nEstudiante no encontrado o nota inválida")
            except ValueError:
                print("\nPor favor, ingrese una nota válida")
                
        elif opcion == "3":
            print(sistema.mostrar_estadisticas())
            
        elif opcion == "4":
            print("\n¡Hasta luego!")
            break
            
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()