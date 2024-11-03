import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
imagen = cv2.imread('007.jpg')  # Asegúrate de cambiar esta ruta
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)  # Convertir de BGR a RGB

# Aplicar un filtro de desenfoque (blur)
imagen_desenfocada = cv2.GaussianBlur(imagen, (15, 15), 0)

# Mostrar las imágenes originales y desenfocadas
plt.figure(figsize=(12, 6))

# Imagen original
plt.subplot(1, 2, 1)
plt.imshow(imagen)
plt.title('Imagen Original')
plt.axis('off')

# Imagen desenfocada
plt.subplot(1, 2, 2)
plt.imshow(imagen_desenfocada)
plt.title('Imagen Desenfocada')
plt.axis('off')
plt.show()
