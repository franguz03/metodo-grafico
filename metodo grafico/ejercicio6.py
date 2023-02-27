import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString

#Ecuaciones e intervalos (Para tabular)
x = np.arange(-20, 180, 10)
y = np.arange(-20, 200, 10)
ejex= 0*y
ejey=0*x
y1 = 180-(2*x)
y2=80-(x/2)
y3=100-x

#Identificadores para las líneas
primera_linea = LineString(np.column_stack((x, y1)))
segunda_linea = LineString(np.column_stack((x, y2)))
tercera_linea = LineString(np.column_stack((x, y3)))
cuarta_linea = LineString(np.column_stack((ejex, y)))
quinta_linea = LineString(np.column_stack((x, ejey)))

#Graficando las líneas
plt.plot(x, y1, '-', linewidth=2, color='b')
plt.plot(x, y2, '-', linewidth=2, color='g')
plt.plot(x, y3, '-', linewidth=2, color='r')
plt.plot(ejex, y, '-', linewidth=2, color='k')
plt.plot(x, ejey, '-', linewidth=2, color='k')

#Configuraciones adicionales del gráfico
plt.grid()
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.title('Método Gráfico')

primera_interseccion = segunda_linea.intersection(cuarta_linea)
segunda_interseccion = tercera_linea.intersection(primera_linea)
tercera_interseccion = segunda_linea.intersection(tercera_linea)
cuarta_interseccion = quinta_linea.intersection(primera_linea)
quinta_interseccion = quinta_linea.intersection(cuarta_linea)

print("intersecciones")
print('interseccion 1: {} '.format(primera_interseccion))
print('interseccion 2: {} '.format(segunda_interseccion))
print('interseccion 3: {} '.format(tercera_interseccion))
print('interseccion 4: {} '.format(cuarta_interseccion))
print('interseccion 5: {} '.format(quinta_interseccion))

xi1m, yi1m = primera_interseccion.xy
xi2m, yi2m = segunda_interseccion.xy
xi3m, yi3m = tercera_interseccion.xy
xi4m, yi4m = cuarta_interseccion.xy
xi5m, yi5m = quinta_interseccion.xy


xi1 = np.float64(np.array(xi1m))
xi2 = np.float64(np.array(xi2m))
xi3 = np.float64(np.array(xi3m))
xi4 = np.float64(np.array(xi4m))
xi5 = np.float64(np.array(xi5m))
yi1 = np.float64(np.array(yi1m))
yi2 = np.float64(np.array(yi2m))
yi3 = np.float64(np.array(yi3m))
yi4 = np.float64(np.array(yi4m))
yi5 = np.float64(np.array(yi5m))

#Evaluando la función objetivo en cada vértice
FOi1 = (xi1 * 4) + (yi1 * 6)
FOi2 = (xi2 * 4) + (yi2 * 6)
FOi3 = (xi3 * 4) + (yi3 * 6)
FOi4 = (xi4 * 4) + (yi4 * 6)
FOi5 = (xi5* 4) + (yi5 * 6)

print('\n funcion objetivo: P = 4x+6y')
print('Función objetivo en la intersección 1: {} '.format(FOi1))
print('Función objetivo en la intersección 2: {} '.format(FOi2))
print('Función objetivo en la intersección 3: {} '.format(FOi3))
print('Función objetivo en la intersección 4: {} '.format(FOi4))
print('Función objetivo en la intersección 5: {} '.format(FOi5))


plt.plot(*primera_interseccion.xy, 'o', color='k')
plt.plot(*segunda_interseccion.xy, 'o', color='k')
plt.plot(*tercera_interseccion.xy, 'o', color='k')
plt.plot(*cuarta_interseccion.xy, 'o', color='k')
plt.plot(*quinta_interseccion.xy, 'o', color='k')

plt.show()