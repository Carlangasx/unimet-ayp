from datetime import datetime
import json
import requests
import typing

class Reactivo:
    """ Representa un Reactivo con sus propiedades"""
    def __init__(self, id, nombre, descripcion, costo, categoria, inventario, unidad_medida, conversiones, fecha_caducidad=None, minimo=0):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo      # Valida que no sea negativo (setter)
        self.categoria = categoria
        self.inventario = inventario  # Valida que no sea negativo (setter)
        self.unidad_medida = unidad_medida
        self.conversiones = conversiones
        self.fecha_caducidad = fecha_caducidad
        self.minimo = minimo

    @property
    def costo(self):
        return self._costo

    @costo.setter
    def costo(self, value):
        if value < 0:
            raise ValueError("El costo no puede ser negativo.")
        self._costo = value

# crea un objeto propieda a prtir del eatributo inentario
    @property
    def inventario(self):
        return self._inventario
    
# evita que el invenatrio sea negativo
    @inventario.setter
    def inventario(self, value):
        if value < 0:
            raise ValueError("El inventario no puede ser negativo.")
        self._inventario = value

# convierte el objeto reactivo en un diccionario
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "costo": self.costo,
            "categoria": self.categoria,
            "inventario_disponible": self.inventario,
            "unidad_medida": self.unidad_medida,
            "conversiones_posibles": self.conversiones,
            "fecha_caducidad": self.fecha_caducidad.strftime("%Y-%m-%d") if self.fecha_caducidad else None,
            "minimo_sugerido": self.minimo
        }

    @classmethod
    def from_dict(cls, data:list):
        fecha = data.get("fecha_caducidad")
        return cls(
            id=data["id"],
            nombre=data["nombre"],
            descripcion=data["descripcion"],
            costo=data["costo"],
            categoria=data["categoria"],
            inventario=data["inventario_disponible"],
            unidad_medida=data["unidad_medida"],
            conversiones=data["conversiones_posibles"],
            fecha_caducidad=datetime.strptime(fecha, "%Y-%m-%d") if fecha else None,
            minimo=data.get("minimo_sugerido", 0)
        )

class GestorReactivos:

    """Representa a un operario de laboratorio que se encarga de manejar 
    el area de reactivos
    """
    #devuel euna lista con todos los reactivos agregados
    def __init__(self) -> list[Reactivo]:
        self.reactivos = []

    #añade un Reactivo a la lista de registro
    def agregar_reactivo(self, reactivo:Reactivo):
        if any(r.nombre == reactivo.nombre for r in self.reactivos):
            raise ValueError(f"Ya existe un reactivo con el nombre: {reactivo.nombre}")
        self.reactivos.append(reactivo)
        self._verificar_inventario(reactivo)

    #elimina un reactivo de la lista de registro
    def eliminar_reactivo(self, nombre:str) -> bool:
        reactivo = self.buscar_reactivo(nombre)
        if reactivo:
            self.reactivos.remove(reactivo)
            return True
        return False
    #cambia un atributo de algun reactivo
    def editar_reactivo(self, nombre:str, **kwargs:list[str]):
        reactivo = self.buscar_reactivo(nombre)
        if not reactivo:
            raise ValueError("Reactivo no encontrado.")
        for key, value in kwargs.items():
            if hasattr(reactivo, key):
                reactivo.key = value
            else:
                raise AttributeError(f"Campo {key} no válido.")
        self._verificar_inventario(reactivo)

    #devuelve un objeto Reactiv a partir de su nombre
    def buscar_reactivo(self, nombre:str) -> Reactivo:
        return next((r for r in self.reactivos if r.nombre == nombre), None)

    #devuelve una alerta si hay poco inventario
    def _verificar_inventario(self, reactivo:Reactivo):
        if reactivo.inventario < reactivo.minimo:
            print(f"⚠️ Alerta: {reactivo.nombre} está por debajo del mínimo ({reactivo.minimo}).")

    #carga reactivos a partir de un archivo JSON
    def cargar_desde_json(self, ruta:str):
        try:
            with open(ruta, "r") as f: #abre archivo en modo lectura
                datos = json.load(f)
                for dato in datos:
                    self.agregar_reactivo(Reactivo.from_dict(dato))
            print("Datos cargados desde archivo.")
        except FileNotFoundError:
            print("Archivo no encontrado.")

    #escribe los reactivos en un archivo JSON
    def guardar_en_json(self, ruta):
        with open(ruta, "w") as f:
            json.dump([r.to_dict() for r in self.reactivos], f, indent=4)
        print("Datos guardados en archivo.")

    def cambiar_unidad(self, nombre, nueva_unidad):
        reactivo = self.buscar_reactivo(nombre)
        if not reactivo:
            print("Reactivo no encontrado.")
            return

        antigua_unidad = reactivo.unidad_medida
        factor = None
        for conversion in reactivo.conversiones:
            if conversion["unidad"] == nueva_unidad:
                factor = conversion["factor"]
                break

        if not factor:
            print(f"No existe conversión de {antigua_unidad} a {nueva_unidad}.")
            return

        reactivo.inventario *= factor
        reactivo.unidad_medida = nueva_unidad
        print(f"Unidad de {nombre} cambiada de {antigua_unidad} a {nueva_unidad}.")

