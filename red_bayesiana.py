import ast


class NodoBayesiano:

    def __init__(self, nombre):
        self.nombre = nombre
        self.padres = []
        self.hijos = []
        self.tabla_probabilidad = {}


class RedBayesiana:

    def __init__(self):
        self.nodos = {}

    def cargar_estructura(self, archivo):
        with open(archivo, 'r') as f:
            for linea in f:
                padre, hijo = linea.strip().split('->')
                padre, hijo = padre.strip(), hijo.strip()
                if padre not in self.nodos:
                    self.nodos[padre] = NodoBayesiano(padre)
                if hijo not in self.nodos:
                    self.nodos[hijo] = NodoBayesiano(hijo)
                self.nodos[hijo].padres.append(self.nodos[padre])
                self.nodos[padre].hijos.append(self.nodos[hijo])

    def cargar_tablas_probabilidad(self, archivo):
        with open(archivo, 'r') as f:
            for linea in f:
                partes = linea.strip().split(':', 1)
                nombre_nodo = partes[0].strip()
                if nombre_nodo not in self.nodos:
                    self.nodos[nombre_nodo] = NodoBayesiano(nombre_nodo)
                self.nodos[nombre_nodo].tabla_probabilidad = ast.literal_eval(
                    partes[1])

    def mostrar_red(self):
        print("\n=== ESTRUCTURA DE LA RED BAYESIANA ===")
        print("Formato: Nodo → [Lista de padres]\n")
        for nombre, nodo in self.nodos.items():
            padres = [p.nombre for p in nodo.padres]
            padres_str = "ninguno" if not padres else ", ".join(padres)
            print(f"• {nombre:<15} → [{padres_str}]")
        print("\n" + "="*35 + "\n")

    def mostrar_tablas(self):
        print("\n=== TABLAS DE PROBABILIDAD ===")
        for nombre, nodo in self.nodos.items():
            print(f"\n► Tabla para: {nombre}")
            print("─" * 40)
            if not nodo.tabla_probabilidad:
                print("  [Tabla vacía]")
            else:
                for condicion, prob in nodo.tabla_probabilidad.items():
                    if condicion == ():
                        # Si no hay condición, muestra tanto True como False
                        print(f"  P({nombre} = True) = {prob:.3f}")
                        print(f"  P({nombre} = False) = {1-prob:.3f}")
                    else:
                        # Si hay condición, muestra solo la probabilidad dada
                        print(f"  P({nombre} = True | dados {condicion}) = {prob:.3f}")
            print("─" * 40)
        print("")
