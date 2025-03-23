# gestor_resultados.py
import google.generativeai as genai
from typing import Dict, List
from datetime import datetime

class Resultado:
    """
    Evalúa los resultados de un experimento usando Gemini 1.5 Flash.
    
    Atributos:
        experimento (dict): Datos del experimento a evaluar
        receta (dict): Receta asociada con valores aceptables
        parametros_aceptables (dict): Parámetros estructurados de la receta
        evaluacion (dict): Resultado de la evaluación por parámetro
    """
    
    def __init__(self,):
        genai.configure(api_key="AIzaSyD5aQo6cPg-GAkOLwsgGJiUKSCRquZ8CX8")
        self.modelo = genai.GenerativeModel('gemini-1.5-flash')
        self.parametros_aceptables = {}
        self.evaluacion = {}

    def cargar_datos(self, experimento: Dict, receta: Dict):
        """Carga los datos necesarios para la evaluación"""
        self.experimento = experimento
        self.receta = receta
        self._extraer_parametros()
        
    def _extraer_parametros(self):
        """Extrae los parámetros de la receta en formato estructurado"""
        self.parametros_aceptables = {
            param["nombre"]: (param["minimo"], param["maximo"])
            for param in self.receta.get("valores_a_medir", [])
        }
    
    def _analizar_resultado(self) -> Dict:
        """Usa Gemini para extraer valores numéricos del resultado textual"""
        prompt = f"""dado un experimento, te debes encargar de tomar el valor de el campo
            [resultado]. toma en cuenta que los valores no estaran
            todos en el mismo formato y debes extraerlos de manera estructurada. 
            Determina tambien si fue 'satifactorio' o 'no satisfactorio'.
            Extrae solo los valores del resultado del siguiente experimento en formato JSON.
            Texto del resultado:
            {self.experimento['resultado']}
            
            Ejemplo de respuesta válida:
            {{"ph_final": 7.0, "resultado": 92.5}}
            roma en cuenta que el campo "ph_final" es un ejemplo 
            y puede variar el ombre especifico del para metro a evualuar.

            De no poder extraer los valores, regresa un diccionario con la siguiente estructura:
            {{"ph_final": None, "resultado": None}}
        """
        
        try:
            respuesta = self.modelo.generate_content(prompt)
            return eval(respuesta.text.strip().replace('```json', '').replace('```', ''))
        except Exception as e:
            print(f"Error en el análisis: {e}")
            return {}

    def evaluar_resultado(self) -> Dict:
        """Realiza la evaluación completa del experimento"""
        valores = self._analizar_resultado()
        
        for param, (minimo, maximo) in self.parametros_aceptables.items():
            valor = valores.get(param.lower())
            cumplido = minimo <= valor <= maximo if valor else False
            self.evaluacion[param] = {
                "valor": valor,
                "min": minimo,
                "max": maximo,
                "cumplido": cumplido
            }
        
        return {
            "experimento_id": self.experimento["id"],
            "evaluacion": self.evaluacion,
            "exitoso": all(p["cumplido"] for p in self.evaluacion.values())
        }

    def generar_reporte(self) -> str:
        """Genera un reporte legible de la evaluación"""
        reporte = []
        reporte.append(f"\n=== Evaluación Experimento {self.experimento['id']} ===")
        reporte.append(f"Receta: {self.receta['nombre']}")
        reporte.append(f"Fecha: {self.experimento['fecha']}\n")
        
        for param, datos in self.evaluacion.items():
            estado = "✅ CUMPLE" if datos["cumplido"] else "❌ NO CUMPLE"
            reporte.append(
                f"Parámetro: {param.upper()}\n"
                f"• Valor obtenido: {datos['valor']}\n"
                f"• Rango aceptable: [{datos['min']} - {datos['max']}]\n"
                f"• Estado: {estado}\n"
            )
        
        resultado_global = "EXPERIMENTO EXITOSO 🎉" if self.evaluacion["exitoso"] else "EXPERIMENTO FALLIDO ❌"
        reporte.append(f"Resultado global: {resultado_global}")
        
        return "\n".join(reporte)