# Fault-Tolerance
Fault Tolerance Practice 
# Universidad de Guadalajara
# CUCEI - Centro Universitario de Ciencias Exactas e Ingenierías
# Carrera: Ingeniería en Computación
# Materia: Computación Tolerante a Fallas
# Maestro: Michel Emanuel Lopez Franco
# Tema: Herramientas para manejo de errores
# Ejercicio 02 - Parte 2
# Fecha: 21/08/23
# Alumno: Maria Fernanda Barroso Monroy
# Sección: D06

# Herramientas para el Manejo de Errores

## Introducción
Este código ha sido desarrollado con el propósito de demostrar algunas herramientas fundamentales que los desarrolladores pueden aplicar para el manejo de errores en sus programas. En particular, se abordan el uso de herramientas de logeo de errores, la implementación de bloques "try-catch" y el uso de afirmaciones (assertions) para validar suposiciones críticas.

## Desarrollo
En la elaboración de este programa, se emplea una librería de registro de errores, lo cual facilita el seguimiento y la identificación de errores en el código. Esta librería registra todos los errores encontrados durante la ejecución, lo que resulta en un control más eficiente y en la solución efectiva de los problemas identificados.

Además, se implementa un "assertion" que asegura la validez de las suposiciones críticas en el código. Específicamente, se verifica que el valor del divisor no sea igual a cero, ya que esta condición generaría una división indefinida. Si la afirmación resulta falsa, se desencadena una excepción "Assertion Error", lo que posibilita una detección temprana de posibles problemas y su respectiva resolución.

Por último, el bloque "try-catch" se utiliza para capturar y gestionar distintas excepciones que podrían surgir durante la interacción del programa con el usuario. Por ejemplo, si el usuario ingresa valores inválidos para la operación de división, se generará una excepción de tipo "ValueError". La implementación del bloque "try-catch" permite manejar de manera ordenada estas situaciones excepcionales, brindando una experiencia más robusta y amigable al usuario.

En resumen, este código ejemplifica la importancia de las herramientas de manejo de errores en el desarrollo de software. Mediante el uso de una librería de registro de errores, afirmaciones y bloques "try-catch", se promueve la detección temprana y el tratamiento adecuado de problemas, mejorando la calidad y confiabilidad del programa.

