# modulo2_experimentos.py
import json
from datetime import datetime
import random
import requests

class RecetaBase:
    """
    Representa una receta base para un experimento.
    """
    def __init__(self, id:int, nombre:str, objetivo:str, reactivos_utilizados:list[tuple],
                  procedimiento:str, valores_a_medir:list[dict]):
        self.id = id
        self.nombre = nombre
        self.objetivo = objetivo
        # reactivos_utilizados: lista de tuplas (Reactivo, cantidad_necesaria, unidad_medida)
        self.reactivos_utilizados = reactivos_utilizados  
        # procedimiento: lista de pasos (str)
        self.procedimiento = procedimiento
        # valores_a_medir: lista de dict con llaves: nombre, formula, minimo, maximo
        self.valores_a_medir = valores_a_medir

    @classmethod
    def from_dict(cls, data:dict): ##NOTE - Ver para que gace falta "reactvos_map"
        """
        Crea una receta a partir de un diccionario.
        """
        reactivos_utilizados = []
        for item in data.get("reactivos_utilizados", []):
            reactivo_id = item["reactivo_id"]
            cantidad = item["cantidad_necesaria"]
            unidad = item["unidad_medida"]
            reactivos_utilizados.append((reactivo_id, cantidad, unidad))
        return cls(
            id=data["id"],
            nombre=data["nombre"],
            objetivo=data["objetivo"],
            reactivos_utilizados=reactivos_utilizados,
            procedimiento=data["procedimiento"],
            valores_a_medir=data.get("valores_a_medir", [])
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "objetivo": self.objetivo,
            "reactivos_utilizados": [
                {
                    "reactivo": reactivo.nombre,
                    "cantidad_necesaria": cantidad,
                    "unidad_medida": unidad
                } for reactivo, cantidad, unidad in self.reactivos_utilizados
            ],
            "procedimiento": self.procedimiento,
            "valores_a_medir": self.valores_a_medir
        }

class Experimento:
    """
    Representa un experimento realizado a partir de una receta.
    """
    def __init__(self, id:str, receta_id:str, responsables:list[str], fecha:datetime, costo:float=0, resultado:dict=None):
        self.id = id
        self.receta_id = receta_id             
        self.responsables = responsables  # Lista de nombres (str)
        self.fecha = fecha if isinstance(fecha, datetime) else datetime.strptime(fecha, "%Y-%m-%d")
        self.costo = costo
        # resultado se puede definir como un diccionario con mediciones
        self.resultado = resultado

    def realizar_experimento(self, receta:RecetaBase, reactivos_map:dict):
        """
        Valida que cada reactivo esté disponible y no haya caducado,
        actualiza el inventario y calcula el costo del experimento.
        Además, simula un error aleatorio.
        """

        for reactivo_id, cantidad_necesaria, unidad in receta.reactivos_utilizados:
            reactivo = reactivos_map.get(reactivo_id)
            if not reactivo:
                raise ValueError(f"Reactivo con ID {reactivo_id} no encontrado.")
            # Validar existencia de inventario
            if reactivo.inventario < cantidad_necesaria:
                raise ValueError(f"""Insuficiente inventario de {reactivo.nombre}: 
                                 Necesario {cantidad_necesaria} {unidad}, disponible
                                 {reactivo.inventario} {unidad}.""")
            # Validar fecha de caducidad
            if reactivo.fecha_caducidad and reactivo.fecha_caducidad.date() < datetime.now().date():
                raise ValueError(f"""El reactivo {reactivo.nombre} caducó el 
                                 {reactivo.fecha_caducidad.strftime('%Y-%m-%d')}.""")

        # Procesar cada reactivo, restando el inventario (con error aleatorio) y acumulando costo
        for reactivo_id, cantidad_necesaria, unidad in receta.reactivos_utilizados:
            reactivo = reactivos_map.get(reactivo_id)
            error = random.uniform(0.001, 0.225) 
            cantidad_real = cantidad_necesaria * (1 + error)
            if reactivo.inventario < cantidad_real:
                raise ValueError(f"""Después del error, el inventario de 
                                 {reactivo.nombre} es insuficiente.""")
            reactivo.inventario -= cantidad_real
            self.costo += cantidad_real * reactivo.costo
            self.resultado = {medicion["nombre"]: round(random.uniform(medicion["minimo"], medicion["maximo"]), 2)
                              for medicion in receta.valores_a_medir}

        self.guardar_en_json()

    @classmethod
    def from_dict(cls, data:dict):
        fecha = data.get("fecha")
        return cls(
            id=data["id"],
            receta_id=data["receta_id"],
            responsables=data["personas_responsables"],
            costo=data["costo_asociado"],
            resultado=data["resultado"],
            fecha=datetime.strptime(fecha, "%Y-%m-%d") if fecha else None,
        )

    def guardar_en_json(self, ruta="experimentos.json"):
        """
        Guarda la información del experimento en un archivo JSON.
        """
        data = {
            "id": self.id,
            "receta_id": self.receta_id,
            "responsables": self.responsables,
            "fecha": self.fecha.strftime("%Y-%m-%d"),
            "costo_asociado": round(self.costo, 2),
            "resultado": self.resultado
        }
        try:
            with open(ruta, "r+") as file:
                try:
                    existing = json.load(file)
                except json.JSONDecodeError:
                    existing = []
                existing.append(data)
                file.seek(0)
                json.dump(existing, file, indent=4)
        except FileNotFoundError:
            with open(ruta, "w") as file:
                json.dump([data], file, indent=4)
                
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "receta_id": self.receta_id,
            "responsables": self.responsables,
            "fecha": self.fecha.strftime("%Y-%m-%d"),
            "costo_asociado": round(self.costo, 2),
            "resultado": self.resultado
        }