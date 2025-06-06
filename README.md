# Proyecto de Inferencia por Enumeración con Redes Bayesianas

Este proyecto implementa un sistema de inferencia probabilística utilizando **Redes Bayesianas**. Permite modelar relaciones causales entre variables mediante una estructura de nodos y probabilidades condicionales. El motor realiza inferencias usando el algoritmo de **enumeración completa**, como se vio en clase de Inteligencia Artificial.

---

## Estructura de Archivos

```plaintext
motor_inferencia/
├── main.py                   # Interfaz interactiva por consola
├── red_bayesiana.py          # Modelo y estructura de la red bayesiana
├── motor_inferencia.py       # Motor de inferencia por enumeración
├── estructura.txt            # Relaciones entre nodos de la red
├── tablas.txt                # Tablas de probabilidad condicional (CPTs)
└── README.md                 # Documentación del proyecto
```

---

## Funcionamiento General del Sistema

1. **Carga la red bayesiana** desde archivos de texto:
   - `estructura.txt`: especifica la dirección de las dependencias entre variables (nodos).
   - `tablas.txt`: contiene las tablas de probabilidad condicional (en formato de diccionario Python).

2. **Visualiza la red** y sus tablas de probabilidad.

3. **Solicita una consulta** al usuario:
   - Variable objetivo.
   - Evidencia conocida.

4. **Ejecuta inferencia por enumeración**:
   - Calcula la distribución de probabilidad condicional de la variable objetivo dado el conjunto de evidencia.

5. **Muestra el resultado** y la traza del cálculo para validación.

---

## Estructura de la Red

Ejemplo del archivo `estructura.txt`:

```plaintext
Rain -> Maintenance
Rain -> Train
Maintenance -> Train
Train -> Appointment
```

Esto representa las relaciones:
- La lluvia afecta el mantenimiento y el tren.
- El mantenimiento también afecta al tren.
- El tren afecta si se llega o no a la reunión (`Appointment`).

---

## Tablas de Probabilidad

Ejemplo del archivo `tablas.txt`:

```python
Rain: {(): 0.2}
Maintenance: {(True,): 0.8, (False,): 0.4}
Train: {(True, True): 0.3, (True, False): 0.5, (False, True): 0.6, (False, False): 0.7}
Appointment: {(True,): 0.4, (False,): 0.9}
```

- Las claves representan combinaciones de los valores de los nodos padres.
- Los valores representan la probabilidad de que el nodo esté en estado `True` dado esa combinación.

---

## Ejemplo de Consulta 

**¿Cuál es la probabilidad de fallar a la reunión cuando el tren está retrasado en un día sin mantenimiento y lluvia ligera? **

### Entrada esperada en consola:

```
Ingresa el nombre de la variable que deseas consultar: Appointment
Variable de evidencia (o 'fin'): Rain
Valor de 'Rain' (True/False): True
Variable de evidencia (o 'fin'): Maintenance
Valor de 'Maintenance' (True/False): True
Variable de evidencia (o 'fin'): Train
Valor de 'Train' (True/False): True
Variable de evidencia (o 'fin'): fin
```

### Salida esperada:

```
P(Appointment = True) dado {'Rain': True, 'Maintenance': True, 'Train': True} → 0.4000
P(Appointment = False) dado {'Rain': True, 'Maintenance': True, 'Train': True} → 0.6000

Esto significa:
Hay 40% de probabilidad de que la persona falle a la reunión.
Hay 60% de probabilidad de que llegue a la reunión.
```

---

## Ejemplos Adicionales

El proyecto incluye varios ejemplos de redes bayesianas para practicar:

### 1. Red Original (Appointment)
```bash
python main.py estructura.txt tablas.txt
```
Red que modela la probabilidad de llegar a una cita basada en lluvia, mantenimiento y estado del tren.

### 2. Red Simple (Estado de Ánimo)
```bash
python main.py estructura2.txt tablas2.txt
```
Red que modela cómo el clima y el ejercicio afectan el estado de ánimo.
Variables: Clima, Ejercicio, Mood

Ejemplo de consulta:
```
Variable a consultar: Mood
Variable de evidencia (o 'fin'): Clima
Valor de 'Clima' (True/False): True
Variable de evidencia (o 'fin'): Ejercicio
Valor de 'Ejercicio' (True/False): True
Variable de evidencia (o 'fin'): fin
```

### 3. Red de Rendimiento Académico
```bash
python main.py estructura3.txt tablas3.txt
```
Red que modela el rendimiento académico basado en múltiples factores.
Variables: Estres, Descanso, Concentracion, Calificacion, Energia, Estudio

Ejemplo de consulta:
```
Variable a consultar: Calificacion
Variable de evidencia (o 'fin'): Estres
Valor de 'Estres' (True/False): True
Variable de evidencia (o 'fin'): Descanso
Valor de 'Descanso' (True/False): False
Variable de evidencia (o 'fin'): Estudio
Valor de 'Estudio' (True/False): False
Variable de evidencia (o 'fin'): fin
```

### 4. Red de Preparación de Cena
```bash
python main.py estructura4.txt tablas4.txt
```
Red compleja que modela el éxito de una cena familiar.
Variables: DiaFestivo, FinDeSemana, Invitados, Presupuesto, Ingredientes, TiempoDisponible, Preparacion, Experiencia, ExitoCena

Ejemplo de consulta:
```
Variable a consultar: DiaFestivo
Variable de evidencia (o 'fin'): ExitoCena
Valor de 'ExitoCena' (True/False): True
Variable de evidencia (o 'fin'): Experiencia
Valor de 'Experiencia' (True/False): True
Variable de evidencia (o 'fin'): TiempoDisponible
Valor de 'TiempoDisponible' (True/False): True
Variable de evidencia (o 'fin'): FinDeSemana
Valor de 'FinDeSemana' (True/False): False
Variable de evidencia (o 'fin'): Preparacion
Valor de 'Preparacion' (True/False): False
Variable de evidencia (o 'fin'): fin
```

Cada red proporciona un ejemplo diferente de uso del sistema de inferencia por enumeración, con distintos niveles de complejidad y diferentes dominios de aplicación.

---

## Explicación del Código 

### `main.py`

Este archivo es el punto de entrada del programa. Aquí se realiza lo siguiente:

- Se crea una instancia de la red bayesiana (`RedBayesiana`).
- Se cargan los archivos `estructura.txt` y `tablas.txt`.
- Se muestran por consola la estructura y las tablas de la red.
- Se solicita al usuario:
  - La variable que desea consultar (por ejemplo: `Appointment`).
  - La evidencia conocida (por ejemplo: `Rain = True`).
- Llama al motor de inferencia para obtener las probabilidades condicionales y las muestra al usuario.

> Es el archivo que debe ejecutarse con: `python main.py`

---

### `red_bayesiana.py`

Contiene dos clases fundamentales:

#### `NodoBayesiano`
- Representa un nodo en la red (una variable).
- Almacena:
  - Su nombre.
  - Lista de padres.
  - Lista de hijos.
  - Su tabla de probabilidad condicional (`tabla_probabilidad`).

#### `RedBayesiana`
- Gestiona todos los nodos y sus relaciones.
- Métodos principales:
  - `cargar_estructura(archivo)`: lee el archivo de relaciones (estructura de la red).
  - `cargar_tablas_probabilidad(archivo)`: carga los valores de probabilidad condicional desde archivo.
  - `mostrar_red()`: imprime los nodos y sus padres.
  - `mostrar_tablas()`: imprime las tablas de probabilidad de cada nodo.

> Este archivo se encarga de construir la red a partir de archivos de texto.

---

### `motor_inferencia.py`

Contiene la clase principal del motor de inferencia:

#### `MotorInferencia`
- Realiza inferencia probabilística por enumeración.
- Métodos principales:
  - `inferencia_por_enumeracion(query_var, evidencia)`: devuelve la distribución de probabilidades de la variable consultada.
  - `enumerar_all(vars, evidencia)`: recursivamente evalúa todas las combinaciones posibles de variables no observadas.
  - `probabilidad(var, valor, evidencia)`: consulta la probabilidad de un nodo en base a su tabla y la evidencia.

> Este archivo contiene el corazón del razonamiento probabilístico en el sistema.

