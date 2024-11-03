import cv2
import numpy as np
import matplotlib.pyplot as plt

def calcular_glcm(imagen, distancias, angulos):
    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Normalizar la imagen
    imagen_normalizada = cv2.normalize(imagen_gris, None, 0, 255, cv2.NORM_MINMAX)
    
    # Calcular GLCM para cada distancia y ángulo
    glcm = np.zeros((256, 256), dtype=np.float32)
    for distancia in distancias:
        for angulo in angulos:
            # Calcular la GLCM
            for i in range(imagen_normalizada.shape[0] - distancia):
                for j in range(imagen_normalizada.shape[1] - distancia):
                    x = imagen_normalizada[i, j]
                    y = imagen_normalizada[i + distancia, j + distancia]
                    glcm[x, y] += 1

            # Normalizar la GLCM
            glcm = glcm / np.sum(glcm)
    
    return glcm

def mostrar_sombra(imagen):
    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Aplicar un umbral para detectar sombras
    _, sombras = cv2.threshold(imagen_gris, 50, 255, cv2.THRESH_BINARY_INV)

    return sombras

# Cargar la imagen
imagen = cv2.imread('007.jpg')  # Cambia esta ruta por la tuya

# Calcular GLCM
distancias = [1]  # Distancia para calcular GLCM
angulos = [0]  # Ángulo para calcular GLCM
glcm = calcular_glcm(imagen, distancias, angulos)

# Mostrar GLCM
plt.imshow(glcm, cmap='gray')
plt.title('Matriz de Co-Ocurrencia de Niveles de Gris (GLCM)')
plt.axis('off')
plt.show()

# Mostrar sombras
sombras = mostrar_sombra(imagen)

# Mostrar la imagen original y la imagen de sombras
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(sombras, cmap='gray')
plt.title('Sombras Detectadas')
plt.axis('off')

plt.show()
