import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
imagen = cv2.imread('007.jpg')  # Asegúrate de cambiar esta ruta
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises

# Aplicar el detector de bordes de Canny
bordes = cv2.Canny(imagen_gris, 100, 200)

# Aplicar un umbral para la segmentación
_, segmentacion = cv2.threshold(imagen_gris, 128, 255, cv2.THRESH_BINARY)

# Mostrar las imágenes originales, bordes y segmentadas
plt.figure(figsize=(15, 5))

# Imagen original
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
plt.title('Imagen Original')
plt.axis('off')

# Bordes detectados
plt.subplot(1, 3, 2)
plt.imshow(bordes, cmap='gray')
plt.title('Bordes Detectados')
plt.axis('off')

# Imagen segmentada
plt.subplot(1, 3, 3)
plt.imshow(segmentacion, cmap='gray')
plt.title('Segmentación')
plt.axis('off')

plt.show()
