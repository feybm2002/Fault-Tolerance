![image](https://github.com/feybm2002/Fault-Tolerance/assets/112119809/9036dd55-1aec-486d-9c18-2b0662aedfbe)# Fault-Tolerance
Fault Tolerance Practice 
Universidad de Guadalajara - CUCEI
Ingeniería en Computación
Materia: Computación Tolerante a Fallas
Maestro: Michel Emanuel Lopez Franco
Tema: Principios y Prevención de Defectos
Ejercicio 03 - Parte 02
Fecha: 28/08/23
Alumno: Maria Fernanda Barroso Monroy
Sección: D06
Orthogonal Defect Classification (ODC) - ¿Qué es?
El Orthogonal Defect Classification (ODC) es un marco sistemático para la Clasificación de Defectos de Software desarrollado por IBM a principios de la década de 1990. ODC es un concepto que permite proporcionar retroalimentación durante el proceso de desarrollo a los desarrolladores, extrayendo firmas del proceso de desarrollo a partir de los defectos.

ODC utiliza información semántica de los defectos para extraer relaciones de causa y efecto en el proceso de desarrollo. Además, ODC incorpora mecanismos integrados para el Análisis de Escape de Fase y el Análisis de Causa Raíz. A menudo se hace referencia a ODC como una "IRM" (Resonancia Magnética) para los defectos de software.

Sección de Apertura
Cuando se identifica un defecto, se pueden clasificar los siguientes atributos:

Actividad: Esta es la actividad real realizada en el momento de descubrimiento del defecto. Por ejemplo, durante la fase de prueba de funciones, un ingeniero podría decidir realizar una inspección de código. La fase sería una prueba de funciones, pero la actividad es la inspección de código.

Disparador: Durante las actividades de revisión e inspección, elige la opción que mejor describa en qué estabas pensando cuando descubriste el defecto.

Impacto: Para los defectos en proceso, selecciona el impacto que crees que el defecto habría tenido en el cliente si hubiera llegado al campo. Para los defectos informados por el cliente, selecciona el impacto que tuvo la falla en el cliente.

Sección de Cierre
Cuando sepas cómo se corrigió el defecto, se pueden clasificar los siguientes atributos:

Objetivo: Representa la identidad de alto nivel de la entidad que se corrigió.

Tipo de Defecto: Representa la naturaleza de la corrección real que se realizó.

Calificador: Aplicable al Tipo de Defecto.

Fuente: Identifica el origen de la entidad que tenía el defecto.

Edad: Identifica la historia de la entidad que tenía el defecto.

![image](https://github.com/feybm2002/Fault-Tolerance/assets/112119809/cbef9c2d-7180-48ca-a227-581c5fbd3b1e)


