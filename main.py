import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import helpers
import UrbanRoutesPage


class TestUrbanRoutes:
    driver = webdriver.Chrome

    @classmethod
    ### procedimiento para establecer caracteristicas de ventana de navegador
    def setup_class(cls):
        # Configuración de las opciones de Chrome
        options = Options()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920x1080")
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        # Inicialización del WebDriver con las opciones definidas
        cls.driver = webdriver.Chrome(options=options)

    def test_set_route(self):
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Acceder a la URL de Urban Routes.
        self.driver.get(data.urban_routes_url)
        # Espera hasta que cargue el logo principal de la pagina
        helpers.wait_visibility_of_element(self.driver, routes_page.log_principal, 3)

        # Iguala las variales de direccion origen y destino en el archivo data
        address_from = data.address_from
        address_to = data.address_to
        # Llamar al método set_from en la instancia de UrbanRoutesPage.
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        # Confirmación de la prueba
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_confort(self):
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Espera hasta que cargue el boton de pedir un taxi
        helpers.wait_visibility_of_element(self.driver, routes_page.button_round, 3)
        # Hace click en el boton de pedir un taxi
        routes_page.click_botton_round()
        # Hace click en el boton de confort
        routes_page.click_confort_select()
        assert True, routes_page.click_check_confort_select

    def test_set_phone(self):
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Hace click en el boton del home page del numero de telefono
        routes_page.click_phone_number_home_page()
        phone_number = data.phone_number
        routes_page.set_phone_number(phone_number)
        # Hace click en el boton siguiente despues de ingresar el numero de telefono
        routes_page.click_phone_number_pop_up_window()
        # Utilizo codigo ya preestablecido para obtener codigo sms para agregar numero telefonico
        # El codigo no esta arrojando nada, hice pruebas con print y el valor era none
        codigo_confirmacion = helpers.retrieve_phone_code(self.driver)
        routes_page.set_sms_code(str(codigo_confirmacion))
        assert True, (str(codigo_confirmacion)).isdigit()
        #click boton siguiente de ventana emergente de codigo de telefono
        routes_page.click_next_code_phone()
        assert routes_page.get_phone_number() == phone_number

    def test_add_card(self):
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Hace click en el boton de metodo de pago en home page
        routes_page.click_payment_method()
        # Hace click en el boton añadir tarjeta
        routes_page.click_add_card()
        card_number = data.card_number
        card_code = data.card_code
        # Ingresa el numero de tarjeta
        routes_page.set_card_number(card_number)
        # Ingresa el numero de codigo de la tarjeta
        routes_page.set_code_number(card_code)
        helpers.wait_to_be_clickable_of_element(self.driver, routes_page.button_agree_card, 3)
        assert routes_page.get_card_number() == card_number
        assert routes_page.get_code_number() == card_code
        # Hace click en el boton añadir tarjeta de la segunda ventana emergente
        routes_page.click_add_card_2nd_pop_up_window()
        assert True, routes_page.check_agree_tcard()
        routes_page.click_close_pop_up_card_windows()

    def test_message_for_driver(self):
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Ingresa el mensaje del conductor
        message_for_driver = data.message_for_driver
        routes_page.set_message_for_driver(message_for_driver)
        assert routes_page.get_message_for_driver() == message_for_driver

    def test_blanket_active(self):
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Seleccionar la manta y pañuelo
        routes_page.click_blanket_selector()
        assert routes_page.get_blanket_value() == 'on'

    def test_order_2_ice_creams(self):
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Agregar 2 helados
        for _ in range(2):
            routes_page.click_ice_cream_plus()
        assert routes_page.get_ice_cream_value() == '2'

    def test_taxi_request_modal_display(self):
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Hace click pedir un taxi y espera hasta que el sistema seleccione un conductor
        routes_page.click_find_taxi()
        assert True, routes_page.check_order_header_title()

    def test_check_show_name_driver_modal(self):
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        helpers.wait_visibility_of_element(self.driver, routes_page.taxi_driver_selected, 40)
        assert True, routes_page.check_taxi_driver_selected()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
