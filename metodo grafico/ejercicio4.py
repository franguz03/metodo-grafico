import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString

#Ecuaciones e intervalos (Para tabular)
x = np.arange(-5, 10, 1)
y = np.arange(-12, 16, 1)
ejex= 0*y
ejey=0*x
y1 = 3-(2*x)
y2=0.5-(0*x)
y3=x

#Identificadores para las líneas
primera_linea = LineString(np.column_stack((x, y1)))
segunda_linea = LineString(np.column_stack((x, y2)))
tercera_linea = LineString(np.column_stack((x, y3)))
cuarta_linea = LineString(np.column_stack((ejex, y)))
quinta_linea = LineString(np.column_stack((x, ejey)))

#Graficando las líneas
plt.plot(x, y1, '-', linewidth=2, color='b')
plt.plot(x, y2, '-', linewidth=2, color='r')
plt.plot(x, y3, '-', linewidth=2, color='m')
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

plt.plot(*primera_interseccion.xy, 'o', color='k')
plt.plot(*segunda_interseccion.xy, 'o', color='k')
plt.plot(*tercera_interseccion.xy, 'o', color='k')

plt.show()