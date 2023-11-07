# LiveCoding Session

[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Este es el código para la prueba de live coding del día 06.11.2023.

## Instrucciones

- Generar un nuevo proyecto de Flask.
- Crear una ruta `/` que esté abierta.
- Crear una ruta `/login` con la que obtener un token en el header (JWT).
- Crear una ruta `/privada` que esté protegida por un decorador creado desde 0 que comprueba la validez del token.

## Particularidades

- El código principal de la aplicación se ha movido dentro de la carpeta `app` en el archivo `__init__.py` para facilitar la importación entre módulos y ejecutar el comando esperado por Flask `Flask run` sin añadir argumentos.
- La aplicación de Flask se creó con un factory pattern.
- Se ha añadido el archivo .env para la configuración de la aplicación (normalmente se incluiría en el .gitignore).
- Se ha incluido un test para la ruta "publica" que comprueba que la respuesta es 200 y el contenido es el esperado.
- Las respuestas 401 obtenidas en la ruta privada son generadas por el decorador. Este se encuentra en la carpeta `utils`.
- Se ha añadido un archivo `requirements.txt` para la instalación de las dependencias.
- La "base de datos" NO es una propia base de datos. Para simplificar el código se ha utilizado una lista de diccionarios que se encuentra en `app.fake_users_database.py`.

## Postman

Se ha incluido un archivo `LiveCoding.postman_collection.json` con las rutas de la aplicación para poder probarlas desde Postman.
Este archivo contiene configuraciones para poder probar el login y la ruta privada. El token generado se guarda en una variable de entorno para poder ser utilizado en la ruta privada.

## Ejecución

Tras crear un nuevo entorno virtual:

```bash
pip install -r requirements.txt
```

Para ejecutar la aplicación:

```bash
flask run
```

Para ejecutar los tests:

```bash
pytest
```

## Estructura del proyecto

```bash
.
├── app
│   ├── fake_users_database.py
│   ├── __init__.py  # <= Aquí se encuentra la aplicación de Flask
│   └──  main.py
├── LiveCoding.postman_collection.json  # <= Colección de Postman
├── README.md
├── requirements.txt
├── tests
│   ├── conftest.py
│   ├── __init__.py
│   └── test_app.py
└── utils
    ├── __init__.py
    └── livecoding_decorators.py
```
