# PRUEBAS AUTOMATIZADAS PARA URBAN ROUTES

# UrbanRoutes Automation Tests

Este repositorio contiene pruebas automatizadas para la aplicación UrbanRoutes utilizando Selenium WebDriver.

#URBANROUTESPAGE

Este código define una clase llamada `UrbanRoutesPage`, que representa la página web de la aplicación UrbanRoutes y contiene métodos para interactuar con diferentes elementos de la página.

1. **Importaciones de paquetes**:
   - `Keys`: Importa la clase `Keys` del módulo `selenium.webdriver` para simular la pulsación de teclas.
   - `By`: Importa la clase `By` del módulo `selenium.webdriver.common.by` para identificar elementos mediante diferentes criterios.

2. **Variables de selección de elementos**:
   - Define variables para identificar diferentes elementos de la página web utilizando diferentes estrategias de localización, como ID, XPATH, CSS_SELECTOR, etc.

3. **Método `__init__`**:
   - Este método inicializa un objeto `UrbanRoutesPage` con un controlador WebDriver.

4. **Métodos de acción y obtención**:
   - Cada método realiza una acción específica en la página web, como establecer una dirección de origen, hacer clic en un botón, ingresar un número de teléfono, etc.
   - Algunos métodos también devuelven valores, como obtener el valor de un campo de entrada o verificar si un elemento está visible en la página.

5. **Comentarios explicativos**:
   - Se agregan comentarios descriptivos antes de cada método para indicar qué acción realiza ese método.

En resumen, este código proporciona una interfaz para interactuar con la página web de la aplicación UrbanRoutes mediante Selenium WebDriver, facilitando la automatización de pruebas y tareas. Cada método encapsula una acción específica que puede realizar un usuario en la página web.

## Requisitos
- Python 3.x
- Selenium WebDriver
- Google Chrome (u otro navegador compatible)

## Instalación
1. Clona este repositorio en tu máquina local:
```bash
git clone https://github.com/tu_usuario/urbanroutes-automation.git
Instala las dependencias necesarias:
bash
pip install selenium
Descarga el WebDriver correspondiente a tu navegador y versión, y asegúrate de que esté en tu PATH.
Configuración
Antes de ejecutar las pruebas, asegúrate de configurar los siguientes parámetros en el archivo config.py:

BASE_URL: URL base de la aplicación UrbanRoutes.
DRIVER_PATH: Ruta al archivo ejecutable del WebDriver.
Ejecución de Pruebas
Para ejecutar las pruebas, simplemente ejecuta el archivo test_suite.py:

bash
python test_suite.py
Estructura del Proyecto
test_suite.py: Archivo principal que ejecuta todas las pruebas.
config.py: Configuración del proyecto, incluyendo la URL base y la ruta al WebDriver.
urban_routes_tests.py: Contiene las pruebas de Selenium para las diferentes funcionalidades de UrbanRoutes.
README.md: Documentación del proyecto.



#HELPERS

Este código contiene métodos de espera y apoyo útiles para automatizar pruebas con Selenium WebDriver. Aquí hay una descripción detallada:

1. **`retrieve_phone_code(driver) -> str`**:
   - Este método busca y devuelve un código de confirmación de teléfono como una cadena.
   - Funciona esperando y analizando los registros de rendimiento del navegador para encontrar el código de confirmación.
   - Utiliza el WebDriver proporcionado como argumento para acceder a los registros del navegador y obtener el código.
   - Si no se encuentra ningún código después de 10 intentos, genera una excepción.
   - Útil para obtener códigos de confirmación que pueden ser necesarios durante las pruebas automatizadas, como al verificar la autenticación de un número de teléfono.

2. **`wait_visibility_of_element(driver, element, w_time)`**:
   - Este método espera hasta que un elemento en la página web sea visible.
   - Utiliza la clase `WebDriverWait` de Selenium para esperar hasta que se cumpla la condición de visibilidad del elemento especificado.
   - Toma el WebDriver, el elemento y el tiempo máximo de espera como argumentos.
   - Útil para asegurarse de que un elemento esté presente y visible antes de realizar acciones en él durante las pruebas.

3. **`wait_to_be_clickable_of_element(driver, element, w_time)`**:
   - Este método espera hasta que un elemento en la página web sea clickeable.
   - Utiliza la clase `WebDriverWait` de Selenium para esperar hasta que se cumpla la condición de clickeabilidad del elemento especificado.
   - Toma el WebDriver, el elemento y el tiempo máximo de espera como argumentos.
   - Útil para asegurarse de que un elemento esté listo para ser clickeado antes de interactuar con él durante las pruebas.

Estos métodos son esenciales para garantizar que las pruebas automatizadas se ejecuten de manera confiable y se comporten como se espera en diferentes situaciones de la interfaz de usuario. Permiten gestionar tiempos de espera y obtener información relevante de la página web, como códigos de confirmación.

# Selenium WebDriver Support Module

Este módulo proporciona métodos de espera y apoyo para mejorar la estabilidad y confiabilidad de las pruebas automatizadas utilizando Selenium WebDriver.

## Métodos de Espera y Apoyo

### retrieve_phone_code(driver) -> str

Este método permite recuperar el código de confirmación de un número de teléfono. Es útil cuando la aplicación espera el código de confirmación para ser utilizado en las pruebas. Ten en cuenta que el código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación.

### wait_visibility_of_element(driver, element, w_time)

Espera hasta que un elemento sea visible en la página. Esto es útil para asegurarse de que los elementos estén presentes antes de interactuar con ellos en las pruebas.

### wait_to_be_clickable_of_element(driver, element, w_time)

Espera hasta que un elemento sea clickeable. Esto asegura que el elemento esté listo para ser interactuado, lo que evita errores relacionados con la interacción con elementos no clickeables.

## Uso

Para utilizar estos métodos en tus pruebas, simplemente importa el módulo y llama a los métodos correspondientes, pasando el objeto WebDriver, el elemento y el tiempo de espera como parámetros.

```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from tu_modulo import retrieve_phone_code, wait_visibility_of_element, wait_to_be_clickable_of_element

# Inicializar el WebDriver
driver = webdriver.Chrome()

# Ejemplo de uso de retrieve_phone_code
codigo_telefono = retrieve_phone_code(driver)
print("Código de confirmación del teléfono:", codigo_telefono)

# Ejemplo de uso de wait_visibility_of_element
elemento = (By.ID, 'mi_elemento')
wait_visibility_of_element(driver, elemento, 10)  # Espera máximo 10 segundos

# Ejemplo de uso de wait_to_be_clickable_of_element
wait_to_be_clickable_of_element(driver, elemento, 10)  # Espera máximo 10 segundos




#MAIN

Este código es un conjunto de pruebas automatizadas para la aplicación UrbanRoutes utilizando Selenium WebDriver. Aquí está una descripción paso a paso:

1. **Importaciones de módulos**: 
   - Importa el módulo `data`, que contiene datos de configuración para las pruebas.
   - Importa las clases y funciones necesarias de los módulos `selenium.webdriver`, `selenium.webdriver.chrome.options`, `helpers`, y `UrbanRoutesPage`.

2. **Clase `TestUrbanRoutes`**: 
   - Esta clase contiene métodos de prueba para diferentes funcionalidades de la aplicación UrbanRoutes.
   - `driver = webdriver.Chrome`: Define la clase del WebDriver que se utilizará para las pruebas como `webdriver.Chrome`.

3. **Método `setup_class(cls)`**:
   - Este método es decorado con `@classmethod` y se ejecuta una vez antes de ejecutar todas las pruebas de la clase.
   - Configura las opciones del navegador Chrome para el WebDriver, como tamaño de ventana y preferencias de registro de rendimiento.
   - Inicializa el WebDriver de Chrome con las opciones configuradas.

4. **Métodos de prueba**:
   - Cada método de prueba comienza con `test_` y contiene la lógica para probar una funcionalidad específica de la aplicación.
   - Se crea una instancia de `UrbanRoutesPage` para interactuar con la página web de UrbanRoutes.
   - Se accede a la URL de la aplicación UrbanRoutes utilizando el WebDriver.
   - Se realizan diversas acciones en la página web, como establecer una ruta, seleccionar comodidades, ingresar un número de teléfono, agregar una tarjeta de crédito, etc.
   - Se realizan afirmaciones para verificar que el comportamiento de la aplicación sea el esperado después de cada acción.

5. **Método `teardown_class(cls)`**:
   - Este método es decorado con `@classmethod` y se ejecuta una vez después de ejecutar todas las pruebas de la clase.
   - Cierra el WebDriver después de completar todas las pruebas.

En resumen, este código representa un conjunto completo de pruebas automatizadas que cubren diferentes aspectos y funcionalidades de la aplicación UrbanRoutes utilizando Selenium WebDriver.

## Requisitos

- Python 3.x
- Selenium WebDriver
- Google Chrome (u otro navegador compatible)

## Instalación

1. Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu_usuario/pruebas-urbanroutes.git
Instala las dependencias necesarias:
bash
pip install selenium
Descarga el WebDriver correspondiente a tu navegador y versión, y asegúrate de que esté en tu PATH.
Configuración
Asegúrate de configurar los siguientes parámetros en el archivo data.py:

urban_routes_url: URL de la aplicación UrbanRoutes.
address_from: Dirección de origen para las pruebas.
address_to: Dirección de destino para las pruebas.
phone_number: Número de teléfono para las pruebas.
card_number: Número de tarjeta de crédito para las pruebas.
card_code: Código de seguridad de la tarjeta de crédito para las pruebas.
message_for_driver: Mensaje para el conductor del taxi para las pruebas.
Ejecución de Pruebas
Para ejecutar las pruebas, simplemente ejecuta el archivo test_urbanroutes.py:

bash
python test_urbanroutes.py
Estructura del Proyecto
test_urbanroutes.py: Archivo principal que contiene las pruebas automatizadas.
data.py: Archivo de datos que contiene la configuración necesaria para las pruebas.
helpers.py: Módulo con funciones auxiliares para las pruebas.
urbanroutespage.py: Módulo que define la clase UrbanRoutesPage para interactuar con la página de UrbanRoutes.
README.md: Documentación del proyecto.
