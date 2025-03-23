# modulo4_indicadores.py
import json
import matplotlib.pyplot as plt

class IndicadoresGestion:
    """
    Métodos para generar estadísticas sobre el uso del laboratorio.
    Estas funciones pueden incluir:
      - Investigadores más activos.
      - Experimento más/menos realizado.
      - Reactivos con mayor rotación.
      - Experimentos no realizados por falta de reactivos.
      - Reactivos con mayor vencimiento.
      - Número de experimentos fallidos por falta de reactivos.
      - Graficar estadísticas
    """

    @staticmethod
    def investigadores_mas_activos(experimentos):
        """
        :para experimentos: lista de experimentos (cada uno con 'responsables')
        :return: Lista de investigadores ordenados por cantidad de participaciones.
        """
        conteo = {}
        for exp in experimentos:
            for persona in exp.responsables:
                conteo[persona] = conteo.get(persona, 0) + 1
        # Ordenar de mayor a menor
        return sorted(conteo.items(), key=lambda x: x[1], reverse=True)#NOTE - verificar funcion de lambda

    @staticmethod
    def experimento_mas_menos_hecho(experimentos):
        """
        :param experimentos: lista de experimentos (se asume que se puede agrupar por receta)
        :return: Tuple (receta_mas_hecha, receta_menos_hecha)
        """
        conteo = {}
        for exp in experimentos:
            nombre_receta = exp.receta.nombre #NOTE - las recetas estan por id, no por objeto
            conteo[nombre_receta] = conteo.get(nombre_receta, 0) + 1
        receta_mas_hecha = max(conteo.items(), key=lambda x: x[1])
        receta_menos_hecha = min(conteo.items(), key=lambda x: x[1])
        return receta_mas_hecha, receta_menos_hecha

    @staticmethod
    def reactivos_alta_rotacion(gestor_reactivos, umbral):
        """
        :param gestor_reactivos: objeto GestorReactivos con la lista de reactivos.
        :param umbral: valor de cantidad para considerar alta rotación.
        :return: Lista de reactivos con inventario por debajo del umbral.
        """
        return [r for r in gestor_reactivos.reactivos if r.inventario < umbral]

    @staticmethod
    def graficar_indicadores(datos, titulo="Indicadores de Gestión", archivo="indicadores.png"):
        """
        Grafica datos de indicadores.
        :param datos: dict con claves y valores numéricos.
        """
        claves = list(datos.keys())
        valores = list(datos.values())
        plt.figure(figsize=(8, 5))
        plt.bar(claves, valores, color="orchid")
        plt.xlabel("Indicador")
        plt.ylabel("Valor")
        plt.title(titulo)
        plt.tight_layout()
        plt.savefig(archivo)
        plt.close()