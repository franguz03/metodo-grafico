import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString

#Ecuaciones e intervalos (Para tabular)
x = np.arange(-20, 80, 10)
y = np.arange(-20, 150, 10)
ejex= 0*y
ejey=0*x
y4=23+(0*y)
y1 = 65-x
y2=125-(2.5*x)
y3=20+(0*x)


#Identificadores para las líneas
primera_linea = LineString(np.column_stack((x, y1)))
segunda_linea = LineString(np.column_stack((x, y2)))
tercera_linea = LineString(np.column_stack((y4, y)))
cuarta_linea = LineString(np.column_stack((ejex, y)))
quinta_linea = LineString(np.column_stack((x, ejey)))

#Graficando las líneas
plt.plot(x, y1, '-', linewidth=2, color='b')
plt.plot(x, y2, '-', linewidth=2, color='g')
plt.plot(y4, y, '-', linewidth=2, color='r')
plt.plot(x, y3, '-', linewidth=2, color='c')

plt.plot(ejex, y, '-', linewidth=2, color='k')
plt.plot(x, ejey, '-', linewidth=2, color='k')

#Configuraciones adicionales del gráfico
plt.grid()
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.title('Método Gráfico')

primera_interseccion = segunda_linea.intersection(primera_linea)
segunda_interseccion = tercera_linea.intersection(primera_linea)


print("intersecciones")
print('interseccion 1: {} '.format(primera_interseccion))
print('interseccion 2: {} '.format(segunda_interseccion))



xi1m, yi1m = primera_interseccion.xy
xi2m, yi2m = segunda_interseccion.xy




xi1 = np.float64(np.array(xi1m))
xi2 = np.float64(np.array(xi2m))


yi1 = np.float64(np.array(yi1m))
yi2 = np.float64(np.array(yi2m))


#Evaluando la función objetivo en cada vértice
FOi1 = (xi1 * 120) + (yi1 * 200)
FOi2 = (xi2 * 120) + (yi2 * 200)



print('\n funcion objetivo: P = 4x+6y')
print('Función objetivo en la intersección 1: {} '.format(FOi1))
print('Función objetivo en la intersección 2: {} '.format(FOi2))




plt.plot(*primera_interseccion.xy, 'o', color='k')
plt.plot(*segunda_interseccion.xy, 'o', color='k')



plt.show()