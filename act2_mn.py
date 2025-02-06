#   Codigo que implementa un esquema numerico 
#   para determinar la aproximacion de Leibniz     
#
#     Autor: Mendez Cervra Gilbert Alexander
#            mendezgilbert222304@outlok.com
#           versión: 1.01 05/02/2025

import numpy as np  # Se importa la librería NumPy para manejar valores matemáticos.
import matplotlib.pyplot as plt  # Se importa Matplotlib para graficar.

def leibniz_pi(n):

    #Calcular la aproximación de pi usando la serie de Leibiz.
    return 4 * sum((-1)**k / (2*k + 1) for k in range(n))

#Valor real de pi
true_pi = np.pi
# Lista de valores de N (cantidad de términos en la serie)
N_values = [10, 100, 1000, 10000]
# Listas para almacenar los errores calculados
errors_abs = []  # Lista para el error absoluto
errors_rel = []  # Lista para el error relativo
errors_cua = []  # Lista para el error cuadrático
# Bucle para calcular errores en diferentes valores de N
for N in N_values:
    approx_pi = leibniz_pi(N)  # Se calcula pi con N términos
    error_abs = abs(true_pi - approx_pi)  # Error absoluto 
    error_rel = error_abs / true_pi  # Error relativo 
    error_cua = error_abs**2  # Error cuadrático 
    
    # Se almacenan los errores en sus respectivas listas
    errors_abs.append(error_abs)
    errors_rel.append(error_rel)
    errors_cua.append(error_cua)

    # Se imprime el resultado de la iteración
    print(f"N={N}: Error absoluto={error_abs}, Error relativo={error_rel}, Error cuadrático={error_cua}")

# Creación de la gráfica
plt.figure()  # Se crea una nueva figura para la gráfica

# Se grafican los errores en función de N
plt.plot(N_values, errors_abs, label='Error absoluto', marker='o')  # Grafica del error absoluto
plt.plot(N_values, errors_rel, label='Error relativo', marker='s')  # Grafica del error relativo
plt.plot(N_values, errors_cua, label='Error cuadrático', marker='^')  # Grafica del error cuadrático

# Se establece escala logarítmica en los ejes para mejor visualización
plt.xscale('log')  # Escala logarítmica en el eje X (N)
plt.yscale('log')  # Escala logarítmica en el eje Y (Errores)

# Etiquetas y título del gráfico
plt.xlabel('N')  # Etiqueta del eje X
plt.ylabel('Error')  # Etiqueta del eje Y
plt.legend()  # Muestra la leyenda de cada curva
plt.title('Errores en la aproximación de pi')  # Título de la gráfica

# Se muestra la gráfica
plt.show()