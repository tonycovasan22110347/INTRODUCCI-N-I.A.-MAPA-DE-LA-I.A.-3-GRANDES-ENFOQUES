import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Generamos un conjunto de datos en forma de media luna
X, y = make_moons(n_samples=300, noise=0.2, random_state=42)

# Dividimos el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creamos un clasificador SVM con kernel RBF
svm_model = SVC(kernel='rbf', gamma='scale')
svm_model.fit(X_train, y_train)

# Realizamos predicciones
predicciones = svm_model.predict(X_test)

# Visualizamos los resultados
plt.figure(figsize=(8, 6))
plt.scatter(X_test[:, 0], X_test[:, 1], c=predicciones, cmap='viridis', edgecolor='k', s=50)
plt.title('Clasificación usando SVM con Kernel RBF')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.show()

# Evaluamos el modelo
accuracy = svm_model.score(X_test, y_test)
print(f'Precisión del modelo: {accuracy:.2f}')
