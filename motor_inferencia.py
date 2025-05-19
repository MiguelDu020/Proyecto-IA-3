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

    def enumerar_all(self, vars, evidencia):
        if not vars:
            return 1.0
        Y = vars[0]
        nodo = self.red.nodos[Y]
        if Y in evidencia:
            prob = self.probabilidad(Y, evidencia[Y], evidencia)
            print(
                f"Evaluando {Y}={evidencia[Y]} con evidencia {evidencia} → P={prob}"
            )
            return prob * self.enumerar_all(vars[1:], evidencia)
        else:
            total = 0
            for y in [True, False]:
                evidencia[Y] = y
                prob = self.probabilidad(Y, y, evidencia)
                subtotal = prob * self.enumerar_all(vars[1:], dict(evidencia))
                print(
                    f"Evaluando {Y}={y} con evidencia {evidencia} → P={subtotal}"
                )
                total += subtotal
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
