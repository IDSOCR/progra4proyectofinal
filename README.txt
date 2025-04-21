

INNOVAWEB

Descripción de la Startup:

InnovaWeb es una plataforma web innovadora para promocionar servicios de desarrollo web, revisión de artículos y asesoría en estudios tecnológicos. Ofrece una experiencia interactiva en una sola página (SPA) con diseño responsivo, login seguro y presentación profesional de portafolio.

Objetivos del sitio web:

•	Crear una SPA clara, estética y funcional.
•	Usar HTML5, CSS3, JavaScript y Bootstrap 5.
•	Permitir registro y login de usuarios con almacenamiento en SQLite.
•	Mostrar una interfaz dinámica y personalizada tras iniciar sesión.
•	Aplicar el patrón de diseño MVC con Flask y Python.

Funcionamiento

Se va a describir con imágenes la funcionalidad del programa.

Login exitoso:

 




 

 










Login fallido:

 





















Registro exitoso:

 

 


 

Flujo MVC aplicado en el Proyecto

Modelo (Model) dentro de la carpeta principal:
El archivo init_db.py crea y define la base de datos SQLite (usuarios).
El archivo app.py contiene la lógica para insertar, consultar y validar datos.

Vista (View):
Los archivos HTML dentro de la carpeta templates/ (login.html, register.html, index.html) muestran la interfaz al usuario y se renderizan con datos desde Flask.

Controlador (Controller):
El archivo app.py maneja las rutas (/login, /register, /logout) y decide qué vista mostrar, validando información y controlando el flujo de navegación.

