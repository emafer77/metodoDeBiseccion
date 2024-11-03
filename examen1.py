import numpy as np
import matplotlib.pyplot as plt

# Definimos la función a minimizar
def f(x):
    return (x-5)**2 + 50

# Función de bisección para encontrar el mínimo
def biseccion_minimo(a, b, epsilon):
    # Paso 2: Calcula el punto medio y los puntos de prueba
    xm = (a + b) / 2
    L = b - a
    x1 = a + L / 4
    x2 = b - L / 4
    
    # Evaluamos la función en los puntos
    fx1 = f(x1)
    fxm = f(xm)
    fx2 = f(x2)
    
    # Condición de parada
    if abs(L) < epsilon:
        return (a, b)  # Intervalo en el cual se encuentra el mínimo aproximado
    
    # Comparaciones para reducir el intervalo
    if fx1 < fxm:
        return biseccion_minimo(a, xm, epsilon)
    elif fx2 < fxm:
        return biseccion_minimo(xm, b, epsilon)
    else:
        return biseccion_minimo(x1, x2, epsilon)

# Valores iniciales
a = 1
b = 10
epsilon = 0.01

# Ejecución del método
intervalo_minimo = biseccion_minimo(a, b, epsilon)
print("El mínimo de f(x) se encuentra aproximadamente en el intervalo:", intervalo_minimo)

# Gráfica de la función
x_values = np.linspace(-10, 10, 400)  # Rango de valores para x
y_values = f(x_values)  # Valores de la función

# Crear la figura y el eje
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f(x) = (x-5) ^ 2', color='blue')

# Marcar el intervalo mínimo
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(intervalo_minimo[0], color='red', label='Límite Izquierdo', lw=1, ls='--')
plt.axvline(intervalo_minimo[1], color='green', label='Límite Derecho', lw=1, ls='--')

# Títulos y etiquetas
plt.title('Gráfica de la función f(x) y el intervalo de mínimo')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()

# Mostrar la gráfica
# En lugar de plt.show(), usa:
plt.savefig('mi_grafica.png')  # Guarda la gráfica en un archivo PNG

