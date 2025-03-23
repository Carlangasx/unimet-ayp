from modulos.gestor_reactivos import GestorReactivos, Reactivo
from modulos.gestor_experimentos import Experimento, RecetaBase
from modulos.resultados import Resultado
from modulos.indicadores import IndicadoresGestion
from datetime import datetime
import json
import requests

class Laboratorio:
    def __init__(self):
        self.gestor_reactivos = GestorReactivos()
        self.experimentos = []
        self.recetas = []
        self.cargar_datos_iniciales()

    def cargar_datos_iniciales(self):
        """Define el estado inicial del sistema a traves de la api"""
        url_base = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/'
        endpoints = ['reactivos.json','experimentos.json','recetas.json']
        for i in endpoints:
            try:
                url = url_base + i
                response = requests.get(url)
                response.raise_for_status()
                datos = response.json() #parsing a JSON
                for dato in datos:
                    match i:
                        case 'reactivos.json':
                            self.gestor_reactivos.agregar_reactivo(Reactivo.from_dict(dato))
                        case 'recetas.json':
                            self.recetas.append(RecetaBase.from_dict(dato))
                        case 'experimentos.json':
                            self.experimentos.append(Experimento.from_dict(dato))

                print("Datos cargados desde la API.")   
            except Exception as e: #informe sobre errores durante la carga
                print(f"Error al cargar desde API: {e}")

    def run(self):
        """Inicia el sistema de navegación principal"""
        while True:
            print("\n=== MENÚ PRINCIPAL ===")
            print("1. Gestión de reactivos")
            print("2. Gestion de experimentos")
            print("3. Evaluar resultados")
            print("4. Indicadores de gestión")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.menu_reactivos()
            elif opcion == "2":
                self.menu_experimentos()
            elif opcion == "3":
                self.menu_resultados()
            elif opcion == "4":
                self.menu_indicadores()
            elif opcion == "5":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def menu_reactivos(self):
        """Submenú para gestión de reactivos"""
        while True:
            print("\n--- GESTIÓN DE REACTIVOS ---")
            print("1. Listar reactivos")
            print("2. Agregar reactivo")
            print("3. Editar reactivo")
            print("4. Cargar desde JSON") ##NOTE - Modificar para cargar desde api tambien
            print("5. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.listar_reactivos()
            elif opcion == "2":
                self.agregar_reactivo()
            elif opcion == "3":
                self.editar_reactivo()
            elif opcion == "4":
                archivo = input("Ingrese ruta del archivo JSON: ")
                self.gestor_reactivos.cargar_desde_json(archivo)
            elif opcion == "5":
                break
            else:
                print("Opción inválida.")

    def menu_experimentos(self):
        """Submenú para experimentos"""
        while True:
            print("\n--- EXPERIMENTOS ---")
            print("1. Listar experimentos disponibles")
            print("2. Realizar experimento")
            print("3. Eliminar experimento")
            print("4. Modificar experimento") #NOTE - Agregar opcion para modificar experimento
            print("5. Volver al menú principal")#NOTE - agregar la opcion de eliminar experimento
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.listar_recetas()
            elif opcion == "2":
                self.realizar_experimento()
            elif opcion == "3":
                self.eliminar_experimento()
            elif opcion == "4":
                self.modificar_experimento()
            elif opcion == "5":
                break
            else:
                print("Opción inválida.")

    def menu_resultados(self):
        """Submenú para evaluación de resultados"""
        while True:
            print("\n--- EVALUACIÓN DE RESULTADOS ---")
            print("1. Evaluar experimento reciente") 
            print("2. Generar gráfico de resultados")
            print("3. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.evaluar_experimento()
            elif opcion == "2":
                id_exp = input("ID del experimento: ")
                self.generar_grafico(id_exp)
            elif opcion == "3":
                break
            else:
                print("Opción inválida.")

    def menu_indicadores(self):
        """Submenú para indicadores de gestión"""
        while True:
            print("\n--- INDICADORES DE GESTIÓN ---")
            print("1. Investigadores más activos")
            print("2. Reactivos con baja rotación") #NOTE - AGregar reactivos con alta rotacion
            print("3. Generar reporte gráfico")
            print("4. Volver al menú principal") #NOTE - Agregar experiento mas hecho y menos echo
            #NOTE - Reactivos qeu mas se vencen
            #NOTE - Cuantas veces no se logro hacer un experimento po falta de reactivos
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.mostrar_investigadores_activos()
            elif opcion == "2":
                umbral = float(input("Umbral de inventario: "))
                self.mostrar_reactivos_baja_rotacion(umbral)
            elif opcion == "3":
                self.generar_reporte_grafico()
            elif opcion == "4":
                break
            else:
                print("Opción inválida.")

    # Métodos de operaciones concretas
    def listar_reactivos(self):
        """Muestra todos los reactivos registrados"""
        print("\nInventario de reactivos:")
        for i, reactivo in enumerate(self.gestor_reactivos.reactivos, 1):
            caducidad = reactivo.fecha_caducidad.strftime("%Y-%m-%d") if reactivo.fecha_caducidad else "N/A"
            print(f"{i}. {reactivo.nombre} | Inventario: {reactivo.inventario} {reactivo.unidad_medida} | Caducidad: {caducidad}")

    def agregar_reactivo(self):
        """Recoge datos para crear un nuevo reactivo"""
        try:
            nombre = input("Nombre del reactivo: ")
            inventario = float(input("Inventario inicial: "))
            unidad = input("Unidad de medida: ")
            nuevo_reactivo = Reactivo(
                id=len(self.gestor_reactivos.reactivos)+1,
                nombre=nombre,
                descripcion=input("Descripción: "),
                costo=float(input("Costo por unidad: ")),
                categoria=input("Categoría: "),
                inventario=inventario,
                unidad_medida=unidad,
                conversiones=[],
                fecha_caducidad=input("Fecha caducidad (YYYY-MM-DD): ") or None
            )
            self.gestor_reactivos.agregar_reactivo(nuevo_reactivo)
            print("¡Reactivo agregado!")
        except Exception as e:
            print(f"Error: {e}")

    def editar_reactivo(self):
        """Modifica un reactivo existente"""
        nombre = input("Nombre del reactivo a editar: ")
        try:
            campo = input("Campo a modificar (inventario/costo/unidad): ")
            valor = input("Nuevo valor: ")
            self.gestor_reactivos.editar_reactivo(nombre, **{campo: valor})
            print("¡Reactivo actualizado!")
        except Exception as e:
            print(f"Error: {e}")

    def listar_recetas(self):
        """Muestra las recetas disponibles"""
        print("\nRecetas disponibles:")
        for i, receta in enumerate(self.recetas, 1):
            print(f"{i}. {receta.nombre} - {receta.objetivo}")

    def realizar_experimento(self):
        """Guía al usuario para ejecutar un experimento"""
        try:
            if not self.recetas:
                print("No hay recetas disponibles. Cargue recetas primero.")
                return
            
            self.listar_recetas()
            seleccion = int(input("Seleccione una receta: "))-1
            receta = self.recetas[seleccion]
            receta_id = receta.id
            reactivos = {r.id: r for r in self.gestor_reactivos.reactivos}
            
            check_id_exp = self.experimentos[-1].id if self.experimentos else 0
            id_exp = check_id_exp + 1
            responsables = input("Responsables (separados por coma): ").split(",")
            
            experimento = Experimento(
                id=id_exp,
                receta_id=receta_id,
                responsables=responsables,
                fecha=datetime.now()
            )
            
            experimento.realizar_experimento(self.recetas[seleccion], reactivos)
            self.experimentos.append(experimento)
            #NOTE - ver donde se usa esta funcion self.evaluar_resultado()
            print(f"¡Experimento {self.recetas[seleccion].nombre} realizado con éxito!")
        
        except Exception as e:
            print(f"Error durante el experimento: {e}")

    def evaluar_experimento(self):
        """Evalúa los resultados del último experimento usando Gemini"""
        if not self.experimentos:
            print("No hay experimentos registrados.")
            return
        
        try:
            # Obtener datos necesarios
            exp = self.experimentos[-1].to_dict()
            receta = next(r for r in self.recetas if r.id == exp["receta_id"]).to_dict()
            
            # Configurar evaluador
            evaluador = Resultado()
            evaluador.cargar_datos(exp, receta)
            resultado = evaluador.evaluar_resultado()
            
            # Mostrar reporte
            print(evaluador.generar_reporte())
            
        except Exception as e:
            print(f"Error en la evaluación: {e}")
    
    def eliminar_experimento(self):
        """Elimina un experimento del historial y del archivo JSON"""
        try:
            with open('experimentos.json', 'r') as file:
                datos = json.load(file)
            
            self.listar_experimentos()
            seleccion = int(input("Seleccione el experimento a eliminar: ")) - 1
            if seleccion < 0 or seleccion >= len(datos):
                print("Selección inválida.")
                return
            
            experimento_a_eliminar = datos.pop(seleccion)
            with open('experimentos.json', 'w') as file:
                json.dump(datos, file, indent=4)
            
            print(f"Experimento {experimento_a_eliminar['id']} eliminado con éxito.")
        except Exception as e:
            print(f"Error al eliminar el experimento: {e}")

    def listar_experimentos(self):
        """Muestra todos los experimentos registrados desde el archivo JSON local"""
        try:
            with open('experimentos.json', 'r') as file:
                datos = json.load(file)
            
            print("\nHistorial de experimentos:")
            for i, experimento in enumerate(datos, 1):
                receta_nombre = next((receta.nombre for receta in self.recetas if receta.id == experimento['receta_id']), "Desconocida")
                fecha = experimento['fecha']
                print(f"{i}. Receta: {receta_nombre} - Fecha: {fecha}")
        except Exception as e:
            print(f"Error al listar experimentos: {e}")

    def modificar_experimento(self):
        """Modifica un experimento existente"""
        try:
            with open('experimentos.json', 'r') as file:
                datos = json.load(file)
            if not datos:
                print("No hay experimentos registrados.")
                return
            
            self.listar_experimentos()
            seleccion = int(input("Seleccione el experimento a modificar: ")) - 1
            if seleccion < 0 or seleccion >= len(datos):
                print("Selección inválida.")
                return
            
            experimento = datos[seleccion]
            campos = {
                "1": "responsables",
                "2": "costo_asociado",
                "3": "resultado"
            }
            
            print("\n--- Modificar Experimento ---")
            for key, value in campos.items():
                print(f"{key}. {value.replace('_', ' ').capitalize()}")
            print("4. Terminar modificación")
            
            while True:
                opcion = input("Seleccione el campo a modificar: ")
                
                if opcion in campos:
                    nuevo_valor = input(f"Nuevo valor para {campos[opcion].replace('_', ' ')}: ")
                    if campos[opcion] == "responsables":
                        nuevo_valor = nuevo_valor.split(",")
                    elif campos[opcion] == "costo_asociado":
                        nuevo_valor = float(nuevo_valor)
                    elif campos[opcion] == "resultado":
                        pass
                    experimento[campos[opcion]] = nuevo_valor
                elif opcion == "4":
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")
            
            datos[seleccion] = experimento
            with open('experimentos.json', 'w') as file:
                json.dump(datos, file, indent=4)
            print("¡Experimento modificado con éxito!")
        except Exception as e:
            print(f"Error al modificar el experimento: {e}")

    def generar_reporte_grafico(self):
        """Genera gráficos de indicadores"""
        datos = {
            "Reactivos bajos": len(IndicadoresGestion.reactivos_alta_rotacion(self.gestor_reactivos, 50)),
            "Experimentos exitosos": sum(1 for e in self.experimentos if ResultadoExperimento(e, {}).es_exitoso()),
            "Total experimentos": len(self.experimentos)
        }
        IndicadoresGestion.graficar_indicadores(datos)
        
        print("Reporte generado: indicadores.png")

if __name__ == "__main__":
    lab = Laboratorio()
    lab.run()