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
        for nombre, nodo in self.nodos.items():
            padres = [p.nombre for p in nodo.padres]
            print(f"Nodo {nombre} tiene como padres: {padres}")

    def mostrar_tablas(self):
        for nombre, nodo in self.nodos.items():
            print(
                f"Tabla de probabilidad de {nombre}: {nodo.tabla_probabilidad}"
            )
