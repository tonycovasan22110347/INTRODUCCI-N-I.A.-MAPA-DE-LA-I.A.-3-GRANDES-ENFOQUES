import cv2
import numpy as np

# Inicializar la captura de video desde la cámara (0 para la cámara predeterminada)
cap = cv2.VideoCapture(0)

# Verifica si la captura se ha iniciado correctamente
if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

# Leer el primer fotograma
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    # Calcular la diferencia entre los fotogramas
    diferencia = cv2.absdiff(frame1, frame2)

    # Convertir a escala de grises
    gris = cv2.cvtColor(diferencia, cv2.COLOR_BGR2GRAY)

    # Aplicar un umbral para obtener una imagen binaria
    _, umbral = cv2.threshold(gris, 30, 255, cv2.THRESH_BINARY)

    # Dilatar la imagen umbral para rellenar los agujeros
    umbral = cv2.dilate(umbral, None, iterations=3)

    # Encontrar contornos en la imagen umbral
    contornos, _ = cv2.findContours(umbral, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar contornos en el fotograma original
    for contorno in contornos:
        if cv2.contourArea(contorno) < 1000:  # Filtrar pequeños movimientos
            continue
        x, y, w, h = cv2.boundingRect(contorno)
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Dibuja un rectángulo alrededor del movimiento

    # Mostrar el fotograma con el movimiento detectado
    cv2.imshow("Movimiento Detectado", frame1)

    # Mover a la siguiente iteración
    frame1 = frame2
    ret, frame2 = cap.read()

    # Presionar 'q' para salir del bucle
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
