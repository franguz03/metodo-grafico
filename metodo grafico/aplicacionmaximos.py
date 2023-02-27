import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString

#Ecuaciones e intervalos (Para tabular)
x = np.arange(-10, 50, 10)
y = np.arange(-10, 50, 10)
ejex= 0*y
ejey=0*x
xsx=2+(0*x)
y1 = 10-(x/2)
y2=1-(x*0)
y3=y

#Identificadores para las líneas
primera_linea = LineString(np.column_stack((x, y1)))
segunda_linea = LineString(np.column_stack((x, y2)))
tercera_linea = LineString(np.column_stack((xsx, y3)))
cuarta_linea = LineString(np.column_stack((ejex, y)))
quinta_linea = LineString(np.column_stack((x, ejey)))

#Graficando las líneas
plt.plot(x, y1, '-', linewidth=2, color='b')
plt.plot(x, y2, '-', linewidth=2, color='g')
plt.plot(xsx, y3, '-', linewidth=2, color='r')
plt.plot(ejex, y, '-', linewidth=2, color='k')
plt.plot(x, ejey, '-', linewidth=2, color='k')

#Configuraciones adicionales del gráfico
plt.grid()
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.title('Método Gráfico')

primera_interseccion = segunda_linea.intersection(primera_linea)
segunda_interseccion = tercera_linea.intersection(primera_linea)
tercera_interseccion = segunda_linea.intersection(tercera_linea)


print("intersecciones")
print('interseccion 1: {} '.format(primera_interseccion))
print('interseccion 2: {} '.format(segunda_interseccion))
print('interseccion 3: {} '.format(tercera_interseccion))


xi1m, yi1m = primera_interseccion.xy
xi2m, yi2m = segunda_interseccion.xy
xi3m, yi3m = tercera_interseccion.xy



xi1 = np.float64(np.array(xi1m))
xi2 = np.float64(np.array(xi2m))
xi3 = np.float64(np.array(xi3m))

yi1 = np.float64(np.array(yi1m))
yi2 = np.float64(np.array(yi2m))
yi3 = np.float64(np.array(yi3m))


#Evaluando la función objetivo en cada vértice
FOi1 = (xi1 * 20) + (yi1 * 45)
FOi2 = (xi2 * 20) + (yi2 * 45)
FOi3 = (xi3 * 20) + (yi3 * 45)


print('\n funcion objetivo: P = 4x+6y')
print('Función objetivo en la intersección 1: {} '.format(FOi1))
print('Función objetivo en la intersección 2: {} '.format(FOi2))
print('Función objetivo en la intersección 3: {} '.format(FOi3))



plt.plot(*primera_interseccion.xy, 'o', color='k')
plt.plot(*segunda_interseccion.xy, 'o', color='k')
plt.plot(*tercera_interseccion.xy, 'o', color='k')


plt.show()