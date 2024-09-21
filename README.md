# Jesús Mauro Becerra Galván
# Sprint 07
# Proyecto Urban Grocers 
# Guía de Creación de Usuarios y Kits para Urban Grocers

## Introducción

Este documento proporciona una guía para la creación de usuarios y kits, incluyendo la validación de datos y los procedimientos de prueba asociados. 

## Fuente de Documentación
Documentación creada con apiDoc.

## Tecnologías y Técnicas
- **Lenguaje:** Python
- **Pruebas:** pytest
- **Otras tecnologías: Solicitud API

# Instalación adicional
- **Pytest
Para poder hacer uso de esto es necesario especificar en la terminal "pip install pytest" donde se procede a realizar la instalación pytest para ejecutar pruebas
- **Import requests
Para su uso solo es necesario declarar "import requests" al inicio del código en el archivo "create_kit_name_kit_test.py"

## Uso de import
Para que el código funcione de manera correcta, se necesitan importar los archivos "sender_stand_requests.py, data.py, configuration.py al archivo create_kit_name_kit_test.py" ya que este último es el archivo principal para ejecutar las pruebas, los demás archivos son funciones o variables que se mandan llamar al archivo principal, también son rutas especificas para hacer las solicitudes HTTP.

## Ruta del proyecto
Para poder ejecutar las pruebas necesitas trabajar desde la ruta donde se almacenan los archivos, para este caso necesitamos C:\Users\1\projects\qa-project-Urban-Grocers-app-es, puede variar la ruta especifica en la terminal.


## Creación de un Usuario

Para crear un nuevo usuario, sigue estos pasos:

1. **Envío de Solicitud:**
   Envía una solicitud HTTP para crear un nuevo usuario.
   
2. **Autenticación:**
   Obtén y guarda el token de autenticación (`authToken`) que se te proporcionará en la respuesta. Este token es necesario para autenticar las solicitudes posteriores relacionadas con el usuario.

## Creación de un Kit

Una vez que hayas creado un usuario y obtenido el `authToken`, puedes proceder a crear un kit para este usuario siguiendo estos pasos:

1. **Envío de Solicitud:**
   Envía una solicitud HTTP para crear un kit. Asegúrate de incluir el encabezado `Authorization` con el `authToken` obtenido en el paso anterior.

2. **Cuerpo de la Solicitud:**
   El cuerpo de la solicitud debe incluir los parámetros necesarios, como el nombre del kit (`name`).

## Lista de Comprobación para la Creación de Kits

Para asegurar que la funcionalidad de creación de kits está funcionando correctamente, utiliza la siguiente lista de comprobación. Los resultados de las pruebas pueden variar según el cuerpo de la solicitud:

1. **Longitud Mínima Permitida:**
   - **Solicitud:** `{ "name": "a" }`
   - **Código de Respuesta Esperado:** 201
   - **Verificación:** El campo "name" en la respuesta coincide con el campo "name" en la solicitud.

2. **Longitud Máxima Permitida:**
   - **Solicitud:** `{ "name": "El valor de prueba para esta comprobación será inferior a..." }` (511 caracteres)
   - **Código de Respuesta Esperado:** 201
   - **Verificación:** El campo "name" en la respuesta coincide con el campo "name" en la solicitud.

3. **Longitud Insuficiente:**
   - **Solicitud:** `{ "name": "" }`
   - **Código de Respuesta Esperado:** 400

4. **Longitud Excesiva:**
   - **Solicitud:** `{ "name": "El valor de prueba para esta comprobación será inferior a..." }` (512 caracteres)
   - **Código de Respuesta Esperado:** 400

5. **Caracteres Especiales Permitidos:**
   - **Solicitud:** `{ "name": "№%@"," }`
   - **Código de Respuesta Esperado:** 201
   - **Verificación:** El campo "name" en la respuesta coincide con el campo "name" en la solicitud.

6. **Espacios Permitidos:**
   - **Solicitud:** `{ "name": " A Aaa " }`
   - **Código de Respuesta Esperado:** 201
   - **Verificación:** El campo "name" en la respuesta coincide con el campo "name" en la solicitud.

7. **Números Permitidos:**
   - **Solicitud:** `{ "name": "123" }`
   - **Código de Respuesta Esperado:** 201
   - **Verificación:** El campo "name" en la respuesta coincide con el campo "name" en la solicitud.

8. **Parámetro Faltante:**
   - **Solicitud:** `{ }`
   - **Código de Respuesta Esperado:** 400

9. **Tipo de Parámetro Incorrecto:**
   - **Solicitud:** `{ "name": 123 }`
   - **Código de Respuesta Esperado:** 400

## Ejecución de pruebas
- **Pruebas grupal con terminal:** pytest .\create_kit_name_kit_test.py
- **Pruebas individuales:** Se ejecutan en el archivo que contiene el código, por defecto aparece un triangulo verde que al hacer clic permite ejecutar una sola prueba


## Conclusión

Esta guía cubre el proceso para crear un usuario y un kit, así como la lista de comprobación necesaria para validar la correcta funcionalidad en la creación de kits. Asegúrate de seguir cada paso y verificar los resultados de acuerdo con la lista de comprobación para garantizar que el sistema funcione como se espera.

Para cualquier duda o problema, por favor, contacta con el equipo de soporte técnico.