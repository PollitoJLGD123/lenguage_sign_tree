# 🤟 **Sistema de Detección y Transcripción del Lenguaje de Señas Peruana**  

Este proyecto utiliza **Inteligencia Artificial** y **Visión por Computadora** para entrenar un modelo capaz de clasificar todas las letras del abecedario en lenguaje de señas. Implementado con Python y la librería **Mediapipe**, el modelo utiliza el algoritmo **Random Forest (Bosque Aleatorio)**, ideal para tareas de clasificación con múltiples categorías como las letras del abecedario.  

---

## ✨ **Características Principales**  

- Clasificación de todas las letras del abecedario en lenguaje de señas.  
- Entrenamiento utilizando datos personalizados recolectados manualmente.  
- Precisión superior al **90%** en las predicciones.  
- Modelo optimizado para procesamiento en tiempo real.

---

## 📖 **Metodología del Proyecto**  

El desarrollo del proyecto se realizó en **cuatro etapas clave**:  

### 1. **Recolección del Dataset**  
Se creó un dataset propio tomando **200 imágenes de la mano** para cada letra del abecedario. Estas imágenes se organizaron en carpetas individuales, nombradas según la letra correspondiente.  

### 2. **Extracción de Puntos Clave**  
Usamos la librería **Mediapipe** para extraer los puntos clave de las manos desde cada imagen del dataset. Estos puntos se almacenaron en un archivo con extensión `.h5` para su procesamiento.  

### 3. **Entrenamiento del Modelo**  
El algoritmo **Random Forest** fue entrenado utilizando los datos recolectados. El modelo procesó los puntos clave y generó un archivo entrenado con extensión `.joblib`, listo para realizar predicciones.  

### 4. **Pruebas y Validación**  
Se probó el modelo con datos de prueba para evaluar su precisión. Los resultados mostraron una precisión superior al **90%**, demostrando la efectividad del sistema.  

---

## 🔧 **Herramientas y Tecnologías Utilizadas**  

- **Lenguaje**: Python  
- **Librerías**: Mediapipe, Scikit-learn, Joblib  
- **Modelo de IA**: Random Forest  

---

## 🚀 **Cómo Funciona**  

1. **Recaudar Imágenes**: Captura imágenes de la mano representando cada letra del abecedario.  
2. **Recorrer Puntos**: Extrae y almacena puntos clave de las imágenes con Mediapipe.  
3. **Crear Modelo**: Entrena el modelo Random Forest con los datos extraídos.  
4. **Testing**: Usa el modelo entrenado para clasificar señas en tiempo real.  

---

## ❤️ **Notas Finales**  

Este proyecto busca facilitar la comunicación entre personas con discapacidad auditiva y oyentes, promoviendo la inclusión social mediante tecnología accesible y eficiente. ¡Espero que les sea de gran ayuda y les guste mucho! ❤️  

---

## 📫 **Contáctame**  

Si tienes preguntas o comentarios, no dudes en contactarnos:  
- **Email**: joseluisjlgd123@gmail.com
- **GitHub**: https://github.com/PollitoJLGD123/PollitoJLGD123


