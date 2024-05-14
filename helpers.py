from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


### se coloco los metodos de espera y apoyo en este modulo a continuacion:
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


# Espera hasta que el elemento sea visible
def wait_visibility_of_element(driver, element, w_time):
    WebDriverWait(driver, w_time).until(expected_conditions.visibility_of_element_located(element))


# Espera hasta que el elemento sea clickeable
def wait_to_be_clickable_of_element(driver, element, w_time):
    WebDriverWait(driver, w_time).until(expected_conditions.element_to_be_clickable(element))
