from red_bayesiana import RedBayesiana
from motor_inferencia import MotorInferencia

def main():
    print("=== CARGANDO RED BAYESIANA ===")
    red = RedBayesiana()
    red.cargar_estructura("ejemplos/estructura1.txt")
    red.cargar_tablas_probabilidad("ejemplos/tablas1.txt")

    print("\n=== ESTRUCTURA DE LA RED ===")
    red.mostrar_red()

    print("\n=== TABLAS DE PROBABILIDAD ===")
    red.mostrar_tablas()

    motor = MotorInferencia(red)

    print("\n" + "="*50)
    print("║            CONSULTA DE INFERENCIA              ║")
    print("="*50)
    
    # Mostrar variables disponibles
    print("\nVariables disponibles en la red:")
    print("─" * 40)
    for nombre in red.nodos.keys():
        print(f"  • {nombre}")
    print("─" * 40)

    # Solicitar variable a consultar
    while True:
        query = input("\n➤ Ingresa el nombre de la variable a consultar: ").strip()
        if query in red.nodos:
            break
        print("Error: Variable no encontrada en la red. Intenta de nuevo.")

    # Recolectar evidencia
    print("\n" + "─"*50)
    print("│ INGRESO DE EVIDENCIA                           │")
    print("│ • Escribe 'fin' cuando termines               │")
    print("│ • Valores permitidos: True/False              │")
    print("─"*50 + "\n")

    evidencia = {}
    while True:
        var = input("► Variable de evidencia (o 'fin'): ").strip()
        if var.lower() == 'fin':
            break
        if var not in red.nodos:
            print("Error: Variable no encontrada en la red.")
            continue
        if var == query:
            print("Error: No puedes dar evidencia sobre la variable consultada.")
            continue
            
        valor = input(f"  Valor de '{var}' (True/False): ").strip()
        if valor.lower() in ['true', 'false']:
            evidencia[var] = True if valor.lower() == 'true' else False
            print(f"✓ Evidencia registrada: {var} = {evidencia[var]}\n")
        else:
            print("Error: El valor debe ser True o False.\n")

    # Mostrar resultados
    print("\n" + "="*50)
    print("║         RESULTADOS DE LA INFERENCIA           ║")
    print("="*50 + "\n")
    
    resultado = motor.inferencia_por_enumeracion(query, evidencia)
    
    # Formatear la evidencia para mejor legibilidad
    evidencia_str = "∅" if not evidencia else ", ".join(f"{var}={val}" for var, val in evidencia.items())
    
    print(f"Variable consultada: {query}")
    print(f"Evidencia: {evidencia_str}\n")
    print("Distribución de probabilidad:")
    print("─" * 40)
    for val, prob in resultado.items():
        print(f"  P({query} = {val:<5}) = {prob:.4f}")
    print("─" * 40 + "\n")
if __name__ == "__main__":
    main()
