# T4.2 Calidad de Software

T4.2 Calidad de Software
A01105695
José Luis Lorenzo Augusto Galíndez Vences


# Actividad 4.2 - Ejercicios de Programación con Estándares Industriales

Este repositorio contiene la solución a tres problemas de programación desarrollados en **Python**, siguiendo estrictamente el estándar de codificación **PEP-8** y validados mediante **PyLint**.

## 🎯 Objetivos
* Explicar la importancia del estilo de codificación en sistemas de software.
* Reconocer atributos de estándares de codificación útiles para identificar errores.
* Identificar estándares industriales (PEP-8) y el uso de herramientas de análisis estático (PyLint).

## 📂 Contenido del Repositorio

1. CARPETA P1

    **`computeStatistics.py`**: Calcula media, mediana, moda, varianza y desviación estándar a partir de un archivo de datos, los archivos de programación

3. CARPETA P2

    **`convertNumbers.py`**: Convierte una lista de números enteros a sus equivalentes en sistemas Binario y Hexadecimal.

3. CARPETA P3 

    **`wordCount.py`**: Identifica palabras distintas y contabiliza su frecuencia de aparición en un texto.


Cada carpeta trae además su carpeta de **RESULTADOS** en los cuales vienen los archivos de texto generados después de la ejecución, además de capturas de pantalla de las ejecuciones en la terminal con el despliegue de los resultados según la rúbrica.

## 🛠️ Requerimientos Técnicos 

* **Verificación Pylint 10.00/10**: Todos los códigos siguen el estándar de codificación PEP-8 con verificación Pylint 10.00/10
* **Algoritmos Básicos**: Todos los cálculos estadísticos y de conversión de base fueron implementados manualmente, sin utilizar librerías externas o funciones integradas de cálculo (como `statistics` o `bin()`).
* **Manejo de Errores**: Los programas detectan datos inválidos en los archivos de entrada, notifican el error en consola y continúan con la ejecución del resto de los datos.
* **Salida de Resultados**: Los resultados se imprimen en la terminal y se guardan automáticamente en archivos de texto específicos (`StatisticsResults.txt`, `ConvertionResults.txt`, `WordCountResults.txt`).
* **Medición de Tiempo**: Cada programa registra e incluye el tiempo total de ejecución al final de los resultados.

## 🚀 Instrucciones de Ejecución

Para ejecutar cualquiera de los programas, utiliza la terminal y pasa como argumento el nombre del archivo que contiene los datos en cada caso

Por ejemplo para cada uno de los programas este sería el argumento:

```bash
python computeStatistics.py TC1.txt
python convertNumbers.py TC2.txt
python wordCount.py TC3.txt
