# **Portfolio**

![Versión](https://img.shields.io/badge/version-1.0.0-green)
![Python](https://img.shields.io/badge/Python-3.9-blue)
![Docker](https://img.shields.io/badge/Docker-20.10-blue?logo=docker&logoColor=white)
![Build In Progress](https://img.shields.io/badge/build-In%20Progress-blue)



**El siguiente proyecto es una solución propuesta a un problema de una startUp en el sector inmobiliario mediante un algoritmo de Data Science. Ofreciendo al usuario final un sistema de recomendación con una interfaz limpia e intuitiva.**

---

## **Índice**

1. [Introducción](#introducción)  
2. [Características](#características)  
3. [Instalación](#instalación)  
4. [Uso](#uso)  
5. [Configuración](#configuración)  
6. [Contribuciones](#contribuciones)  
7. [Roadmap](#roadmap)  
8. [Licencia](#licencia)  
9. [Contacto](#contacto)  

---

## **Introducción**
[Habitacion.com](https://habitacion.com) es una innovadora plataforma de compraventa de habitaciones cuya misión es facilitar el acceso al sector inmobiliario, especialmente a los jóvenes que enfrentan dificultades para ahorrar y acceder a la vivienda.

Entonces, el proyecto **Roomie** se surgió como respuesta para optimizar la búsqueda de inquilinos compatibles en el mercado inmobiliario, un proceso que puede ser tedioso y poco eficiente si se realiza manualmente. La automatización de este proceso con un sistema de recomendación ayuda a los usuarios a encontrar opciones más adecuadas de manera rápida.

Con esta aplicación, los empleados de [Habitacion.com](https://habitacion.com) podrán:

- Crear perfiles para propietarios e inquilinos, incluyendo hábitos de vida y preferencias.

- Ofrecer consejos sobre convivencia basados en el perfil de los usuarios.

- Ofrecer opciones para crear grupos de interés entre inquilinos y propietarios.
- Organizar eventos para fomentar la camaradería.

- Recopilar datos para mejorar el emparejamiento.

---

## **Características**


- **Sistema de Recomendación:** Algoritmos para sugerir propietarios y propiedades compatibles.
- **Análisis de Datos:** Manejo de 12,000 potenciales propietarios con análisis de sus características.
- **Interfaz de Usuario:** Aplicación o dashboard intuitivo.
- **Personalización:** Recomendaciones basadas en preferencias específicas de los usuarios.
- **Optimización de Procesos:** Eficiencia mejorada en la búsqueda de propietarios e inquilinos.
- **Visualización de Datos:** Herramientas para facilitar la comprensión de la información.
- **Modelos Predictivos:** Previsión de tendencias del mercado inmobiliario.
- **Escalabilidad:** Capacidad de manejar más datos y usuarios con el crecimiento de la startup.

<!-- - **Integración de Feedback:** Sistema que aprende y mejora con las calificaciones de los usuarios. -->
<!-- - **Seguridad y Privacidad:** Medidas para proteger la información personal y datos sensibles. -->
---

## **Instalación**

### Requisitos previos

- Docker 

### Pasos

```bash
# Clona el repositorio
git clone https://github.com/iCruzDaniel/Roomie.git

# Ve al directorio del proyecto
cd Roomie

# Construyes la Imagen de docker
docker build -t roomie-app .

#Ejecuta la contenerdor con la Imagen docker
docker run -p 8501:8501 roomie-app
```

---

## **Uso**

1. Una vez construida la imagend de docker y ejecutado el contenedor, ve a la siguiente dirección IP en tu navegador de confianza: http://localhost:8501 .

2. Si deseas detener el programa de manera segura, en la terminal ejecuta el siguiente comando:

```bash
# Detener ejecución del contenedor
docker stop roomie-app
```


---

<!-- ## **Configuración**

- Detalles sobre archivos de configuración como `.env`, `config.json`, etc.  
- Variables de entorno importantes:

```env
API_KEY=tu_api_key
DB_HOST=localhost
``` -->

---

<!-- ## **Contribuciones**

¡Las contribuciones son bienvenidas! Sigue estos pasos para contribuir:  

1. Haz un fork del repositorio.  
2. Crea una nueva rama: `git checkout -b feature/nueva-funcionalidad`.  
3. Realiza tus cambios y haz un commit: `git commit -m 'Añadir nueva funcionalidad'`.  
4. Envía un pull request.

Consulta las [guías de contribución](CONTRIBUTING.md) para más detalles. -->

---

## **Roadmap**

- **Versión actual**:  
  - ✔️ Interfaz intuitiva.  
  - ✔️ Generación de tablas y gráficas de compatibilidad.
  - ✔️ Sistema de recomendación.    


- **Futuras versiones**:  
  - 🛠️ En desarrollo:
    - Ajuste de pesos en la compatibilidad.  
  - 🕒 Planeado:
    - Integración de Feedback.
    - Escalabilidad de datos.

---
<!-- 
## **Licencia**

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles. -->

---

## **Contacto**

- **Autores**: [Daniel Cruz](https://github.com/iCruzDaniel)
- **Correo electrónico**: sp_dicruz@hotmail.com
- **Sitio web**: [DanielCruzPortfolio](https://icruzdaniel.github.io/portfolio/)  
