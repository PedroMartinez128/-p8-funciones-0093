# ==============================================================================
# EJEMPLOS DE FUNCIONES EN PYTHON (Sintaxis y Tipos)
# Pedro Martinez 0093
# ==============================================================================

# --- EJEMPLO 1: Función Básica sin Parámetros ---
# Demuestra la sintaxis fundamental: uso de 'def', dos puntos (:) e indentación.
def saludar():
    print("¡Hola! Bienvenido al aprendizaje de funciones en Python.")


# --- EJEMPLO 2: Función con Parámetros y Sin Retorno ---
# Recibe entradas (parámetros) para personalizar la ejecución.
def saludar_usuario(nombre):
    mensaje = f"Hola, {nombre}. ¡Mucho gusto!"
    print(mensaje)


# --- EJEMPLO 3: Función con Parámetros y Retorno de Valor (return) ---
# Procesa datos de entrada y devuelve un resultado mediante la palabra clave 'return'.
def calcular_suma(a, b):
    resultado = a + b
    return resultado


# --- EJEMPLO 4: Función con Argumentos por Defecto (Opcionales) ---
# Permite definir parámetros predeterminados si no se especifican al llamar a la función.
def calcular_potencia(base, exponente=2):
    return base ** exponente


# --- EJEMPLO 5: Combinación de Funciones Definidas con Funciones Incorporadas (Built-in) ---
# Utiliza funciones nativas de Python como len(), sum(), min() y max() dentro de una función propia.
def analizar_numeros(lista_numeros):
    total_elementos = len(lista_numeros)  # Built-in len()
    suma_total = sum(lista_numeros)        # Built-in sum()
    valor_minimo = min(lista_numeros)      # Built-in min()
    valor_maximo = max(lista_numeros)      # Built-in max()
    
    promedio = suma_total / total_elementos
    
    return {
        "cantidad": total_elementos,
        "suma": suma_total,
        "promedio": promedio,
        "minimo": valor_minimo,
        "maximo": valor_maximo
    }


# ==============================================================================
# EJECUCIÓN Y PRUEBA DE LOS 5 EJEMPLOS
# ==============================================================================

if __name__ == "__main__":
    print("--- Ejemplo 1 ---")
    saludar()

    print("\n--- Ejemplo 2 ---")
    saludar_usuario("Mariano")

    print("\n--- Ejemplo 3 ---")
    suma_res = calcular_suma(15, 25)
    print(f"El resultado de la suma es: {suma_res}")

    print("\n--- Ejemplo 4 ---")
    cuadrado = calcular_potencia(5)       # Usa el exponente por defecto (2)
    cubo = calcular_potencia(5, 3)        # Define un exponente explícito (3)
    print(f"5 al cuadrado: {cuadrado}")
    print(f"5 al cubo: {cubo}")

    print("\n--- Ejemplo 5 ---")
    datos = [10, 20, 30, 40, 50]
    res_analisis = analizar_numeros(datos)
    print(f"Análisis de la lista {datos}:")
    for clave, valor in res_analisis.items():
        print(f"  - {clave.capitalize()}: {valor}")

print("Pedro Martinez 0093")