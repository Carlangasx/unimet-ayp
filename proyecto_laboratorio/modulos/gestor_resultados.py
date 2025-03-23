# modulo3_resultados.py
import json
from datetime import datetime
import matplotlib.pyplot as plt
import google.generativeai as genai
from typing import Dict

class Resultado:
    """
    Evalúa resultados de experimentos usando Gemini Flash 1.5 para análisis de texto.
    """
    
    def __init__(self, api_key: str):
        genai.configure(api_key="AIzaSyD5aQo6cPg-GAkOLwsgGJiUKSCRquZ8CX8")
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.parametros_aceptables = {}
        
        
    def cargar_parametros(self, receta):
        """Carga los parámetros aceptables de la receta"""
        for i in receta.valores_a_medir:
            self.parametros_aceptables = {"nombre" : i["nombre"],
                                          "valores" : (i["minimo"], i["maximo"])}
    
    def _analizar_con_gemini(self, texto: str) -> Dict:
        """Envía el texto a Gemini para extracción estructurada"""
        prompt = f"""dado un experimento, te debes encargar de tomar el valor de el campo
            [resultado]. toma en cuenta que los valores no estaran
            todos en el mismo formato y debes extraerlos de manera estructurada. 
            Determina tambien si fue 'satifactorio' o 'no satisfactorio'.
            Extrae solo los valores del resultado del siguiente experimento en formato JSON.
            Texto: "{texto}"
            Ejemplo de respuesta: {{"nombre": "ph_final", "valor": 7.0, "resultado": "Satisfactorio"}}
        """
        
        try:
            response = self.model.generate_content(prompt)
            return eval(response.text.replace('```json', '').replace('```', '').strip())
        except Exception as e:
            print(f"Error en análisis: {e}")
            return {}

    def evaluar_experimento(self, experimento: Experimento) -> Dict:
        """Evalúa un experimento completo"""
        if not self.parametros_aceptables:
            raise ValueError("Primero debe cargar una receta")
            
        # Extraer valores con Gemini
        valores = self._analizar_con_gemini(experimento["resultado"])

        # Validar parámetros
        reporte = {}
        for nombre, (minimo, maximo) in self.parametros_aceptables.items():
            conclusion = valores.get("resultado")
            reporte["param"] = {
                "nombre": nombre,
                "min": minimo,
                "max": maximo,
                "conclusion": conclusion
            }
        
        return {
            "experimento_id": experimento["id"],
            "parametros": reporte,
            "exitoso": all(p["Satisfactorio"] for p in reporte.values()),
        }