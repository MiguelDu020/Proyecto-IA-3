class MotorInferencia:

    def __init__(self, red):
        self.red = red

    def inferencia_por_enumeracion(self, query_var, evidencia):
        vars = list(self.red.nodos.keys())

        def enumerar_ask(X, evidencia):
            Q = {}
            for x in [True, False]:
                evidencia[X] = x
                Q[x] = self.enumerar_all(vars, dict(evidencia))
            total = sum(Q.values())
            for x in Q:
                Q[x] /= total
            return Q

        return enumerar_ask(query_var, evidencia)

    def enumerar_all(self, vars, evidencia, nivel=0):
        # Indentación para mostrar la recursión
        indent = "  " * nivel
        
        # Caso base: no hay más variables
        if not vars:
            return 1.0
            
        # Tomar la primera variable
        Y = vars[0]
        nodo = self.red.nodos[Y]
        
        # Mostrar el estado actual de la evaluación
        print(f"\n{indent}{'─'*40}")
        print(f"{indent}Evaluando variable: {Y}")
        print(f"{indent}Evidencia actual: {evidencia}")
        
        # Caso 1: La variable está en la evidencia
        if Y in evidencia:
            prob = self.probabilidad(Y, evidencia[Y], evidencia)
            print(f"{indent}► {Y} está en evidencia con valor {evidencia[Y]}")
            print(f"{indent}  P({Y}={evidencia[Y]} | padres) = {prob:.4f}")
            
            # Llamada recursiva
            resultado = prob * self.enumerar_all(vars[1:], evidencia, nivel + 1)
            print(f"{indent}Contribución de {Y}: {resultado:.4f}")
            return resultado
            
        # Caso 2: La variable no está en la evidencia
        else:
            print(f"{indent}► {Y} no está en evidencia, sumando sobre valores posibles")
            total = 0
            
            # Iterar sobre posibles valores
            for y in [True, False]:
                evidencia[Y] = y
                prob = self.probabilidad(Y, y, evidencia)
                print(f"\n{indent}  Probando {Y}={y}:")
                print(f"{indent}  P({Y}={y} | padres) = {prob:.4f}")
                
                # Llamada recursiva
                subtotal = prob * self.enumerar_all(vars[1:], dict(evidencia), nivel + 1)
                print(f"{indent}  Subtotal para {Y}={y}: {subtotal:.4f}")
                total += subtotal
            
            print(f"{indent}Total para {Y}: {total:.4f}")
            return total

    def probabilidad(self, var, valor, evidencia):
        nodo = self.red.nodos[var]
        padres = [p.nombre for p in nodo.padres]
        key = tuple(evidencia[p] for p in padres)
        tabla = nodo.tabla_probabilidad
        if valor:
            return tabla[key]
        else:
            return 1 - tabla[key]
