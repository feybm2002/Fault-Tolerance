# Fault-Tolerance
Fault Tolerance Practice 
|Universidad de Guadalajara
|Centro Universitario de Ciencias Exactas e Ingenierías (CUCEI)
|Carrera de Ingeniería en Computación
|Materia: Computación Tolerante a Fallas
|Maestro: Michel Emanuel Lopez Franco
|Tema: Herramientas para Manejo de Errores
|Actividad 02
|Fecha: 21/08/23
|Alumno: Maria Fernanda Barroso Monroy
|Sección: D06

Introducción
En el ámbito de la programación, es común enfrentarse a diversos errores durante la etapa de compilación y ejecución. La falta de conocimiento sobre las herramientas disponibles para abordar y resolver estos errores puede resultar tediosa. En este documento, exploraremos algunas de las herramientas fundamentales para el manejo de errores en la programación.

Desarrollo
Dentro del proceso de desarrollo de software, contamos con una serie de herramientas valiosas para el manejo de errores. Algunas de las más utilizadas y efectivas son:

Try-Catch:
La estructura try-catch es una técnica común para manejar excepciones en diversos lenguajes de programación. Permite rodear un bloque de código potencialmente problemático con un bloque try, y en caso de que se lance una excepción, capturarla y manejarla en el bloque catch. Esto ayuda a evitar que los errores detengan por completo la ejecución del programa y proporciona la oportunidad de tomar medidas correctivas.

Excepciones Personalizadas:
Además de las excepciones proporcionadas por el lenguaje, es posible crear tus propias excepciones personalizadas. Esto es útil cuando deseas identificar y manejar situaciones específicas dentro de tu aplicación de manera más precisa y significativa.

Validación de Entradas:
Una estrategia proactiva para prevenir errores es validar las entradas y datos antes de procesarlos. Al verificar la integridad y el formato correcto de los datos antes de su uso, puedes evitar errores y fallas inesperadas.

Guard Clauses:
Las declaraciones "guard" se utilizan al comienzo de una función para verificar condiciones especiales antes de que se ejecute el cuerpo principal de la función. Esta técnica ayuda a evitar que el flujo de ejecución alcance puntos donde podrían ocurrir errores, mejorando la robustez de la aplicación.

Logeo de Errores:
Registrar los errores en archivos de registro o en sistemas de monitoreo es fundamental para el diagnóstico de problemas en entornos de producción. Los registros detallados permiten identificar patrones de errores y tomar medidas correctivas de manera eficiente.

Assertions:
Las afirmaciones son declaraciones que especifican condiciones que deben cumplirse en puntos específicos del código. Si una afirmación resulta falsa, se lanza una excepción, lo que facilita la detección temprana de errores durante el desarrollo y las pruebas.

Pruebas Unitarias y TDD:
La práctica de desarrollar pruebas unitarias y seguir el enfoque de Desarrollo Guiado por Pruebas (TDD) puede ayudar a identificar y prevenir errores desde las primeras etapas del ciclo de desarrollo. Las pruebas unitarias garantizan que las partes individuales del código funcionen correctamente.

Conclusión
En muchas ocasiones, los desarrolladores no están completamente conscientes de la amplia variedad de herramientas disponibles para resolver problemas y errores en sus aplicaciones. La selección adecuada de estrategias de manejo de errores puede resultar crucial, no solo para ahorrar recursos y tiempo, sino también para garantizar la confiabilidad y el rendimiento de las aplicaciones. La comprensión y aplicación efectiva de estas herramientas pueden marcar la diferencia en la calidad y el éxito del software desarrollado. 
