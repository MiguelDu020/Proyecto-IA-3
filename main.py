from red_bayesiana import RedBayesiana
from motor_inferencia import MotorInferencia

def main():
    print("=== CARGANDO RED BAYESIANA ===")
    red = RedBayesiana()
    red.cargar_estructura("estructura.txt")
    red.cargar_tablas_probabilidad("tablas.txt")

    print("\n=== ESTRUCTURA DE LA RED ===")
    red.mostrar_red()

    print("\n=== TABLAS DE PROBABILIDAD ===")
    red.mostrar_tablas()

    motor = MotorInferencia(red)

    print("\n=== CONSULTA DE INFERENCIA ===")
    query = input("Ingresa el nombre de la variable que deseas consultar: ")

    evidencia = {}
    print("Ingresa la evidencia conocida (escribe 'fin' para terminar)")
    while True:
        var = input("Variable de evidencia (o 'fin'): ").strip()
        if var.lower() == 'fin':
            break
        valor = input(f"Valor de '{var}' (True/False): ").strip()
        if valor.lower() in ['true', 'false']:
            evidencia[var] = True if valor.lower() == 'true' else False
        else:
            print("Valor inválido. Debe ser True o False.")

    print("\n=== INFERENCIA POR ENUMERACIÓN ===")
    resultado = motor.inferencia_por_enumeracion(query, evidencia)
    print("\n")
    for val, prob in resultado.items():
        print(f"P({query} = {val}) dado {evidencia} → {prob:.4f}")

        print("\n")
if __name__ == "__main__":
    main()
