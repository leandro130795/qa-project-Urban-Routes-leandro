# PRUEBAS AUTOMATIZADAS PARA URBAN ROUTES

# UrbanRoutes Automation Tests

Este repositorio contiene pruebas automatizadas para la aplicación UrbanRoutes utilizando Selenium WebDriver.

#URBANROUTESPAGE
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
