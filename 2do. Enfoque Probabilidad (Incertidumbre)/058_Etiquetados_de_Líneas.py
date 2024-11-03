import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
imagen = cv2.imread('007.jpg')
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar un filtro de Canny para detectar bordes
bordes = cv2.Canny(imagen_gris, 50, 150, apertureSize=3)

# Detectar líneas usando la Transformada de Hough
lineas = cv2.HoughLinesP(bordes, 1, np.pi / 180, threshold=100, minLineLength=30, maxLineGap=10)

# Crear una copia de la imagen original para dibujar las líneas
imagen_lineas = np.copy(imagen)

# Etiquetar las líneas encontradas
if lineas is not None:
    for i, linea in enumerate(lineas):
        x1, y1, x2, y2 = linea[0]
        cv2.line(imagen_lineas, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Dibuja la línea en verde
        # Etiquetar la línea
        cv2.putText(imagen_lineas, f'Línea {i + 1}', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

plt.figure(figsize=(10, 6))
plt.imshow(cv2.cvtColor(imagen_lineas, cv2.COLOR_BGR2RGB))
plt.title('Etiquetado de Líneas')
plt.axis('off')
plt.show()
