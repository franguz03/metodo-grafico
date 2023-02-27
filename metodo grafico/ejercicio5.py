import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString

#Ecuaciones e intervalos (Para tabular)
x = np.arange(-30, 50, 10)
y = np.arange(-12, 50, 10)
ejex= 0*y
ejey=0*x
y1 = 20-((2/3)*x)

#Identificadores para las líneas
primera_linea = LineString(np.column_stack((x, y1)))
segunda_linea = LineString(np.column_stack((ejex, y)))
tercera_linea = LineString(np.column_stack((x, ejey)))

#Graficando las líneas
plt.plot(x, y1, '-', linewidth=2, color='b')
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
print("funcion 20-2/3x)")
print('interseccion eje y: {} '.format(primera_interseccion))
print('interseccion eje x: {} '.format(segunda_interseccion))

plt.plot(*primera_interseccion.xy, 'o', color='k')
plt.plot(*segunda_interseccion.xy, 'o', color='k')

plt.show()