### declaracion e importacion de paquetes
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


### dessarrollo de las suites y metodos para la creacion de las pruebas
class UrbanRoutesPage:
    ### declaracion de variables asignadas a selectores de elementos
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    log_principal = (By.CLASS_NAME, 'logo-image')
    button_round = (By.XPATH, '/html/body/div/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    comfort_select = (By.CSS_SELECTOR,
                      '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > '
                      'div.tariff-cards > div:nth-child(5)')
    button_phone_num = (By.CLASS_NAME, 'np-text')
    input_phone = (By.ID, 'phone')
    button_phone_num_pop_up_window = (By.CSS_SELECTOR,
                                      '#root > div > div.number-picker.open > div.modal > div.section.active > form > '
                                      'div.buttons > button')
    button_next_phone_code = (By.CSS_SELECTOR,
                              '#root > div > div.number-picker.open > div.modal > div.section.active > form > '
                              'div.buttons > button:nth-child(1)')
    sms_code_field = (By.XPATH, '/html/body/div/div/div[1]/div[2]/div[2]/form/div[1]/div/input')
    button_payment_method = (By.CSS_SELECTOR,
                             '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > '
                             'div.form > div.pp-button.filled')
    button_add_card = (By.CSS_SELECTOR,
                       '#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > '
                       'div.pp-row.disabled')
    card_num_field = (By.CLASS_NAME, 'card-input')
    card_code_num_field = (
        By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]/input')
    button_agree_card = (By.CSS_SELECTOR,
                         '#root > div > div.payment-picker.open > div.modal.unusual > div.section.active.unusual > '
                         'form > div.pp-buttons > button:nth-child(1)')
    check_agree_card = (By.CSS_SELECTOR,
                        '#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > '
                        'div:nth-child(3)')
    message_for_driver_field = (By.ID, 'comment')
    blanket_selector = (By.CSS_SELECTOR,
                        '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form '
                        '> div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > span')
    blanket_value = (By.CSS_SELECTOR,
                     '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > '
                     'div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > input')
    blanket_label = (By.CSS_SELECTOR,
                     '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > '
                     'div.reqs.open > div.reqs-body > div:nth-child(1) > div')
    ice_cream2_plus = (By.CSS_SELECTOR,
                       '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > '
                       'div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child('
                       '1) > div > div.r-counter > div > div.counter-plus')
    button_find_taxi = (By.CSS_SELECTOR, '#root > div > div.workflow > div.smart-button-wrapper > button')
    taxi_driver_selected = (By.XPATH, '/html/body/div/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[1]/img')
    ice2_cream_count = (By.CSS_SELECTOR,
                        '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > '
                        'div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child('
                        '1) > div > div.r-counter > div > div.counter-value')
    order_header_title = (By.CLASS_NAME, 'order-header-title')
    close_pop_up_card_windows = (
        By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > button')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        # Encuentra y envia los datos en el campo de la dirección de origen
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        # Encuentra y envia los datos en el campo de la dirección de destino
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_botton_round(self):
        #click en el boton del home page para pedir un taxi
        self.driver.find_element(*self.button_round).click()

    def click_confort_select(self):
        #click en el boton de confort del home page
        self.driver.find_element(*self.comfort_select).click()

    def click_check_confort_select(self):
        #chequea que el boton de confort se ha seleccionado
        element = self.driver.find_element(*self.blanket_label)
        comfort_is_check = element.is_displayed()
        return comfort_is_check

    def click_phone_number_home_page(self):
        #click en el boton de home page para ingresar el numero de telefono
        self.driver.find_element(*self.button_phone_num).click()

    def set_phone_number(self, number_phone):
        # Encuentra y envia los datos en el campo del numero de telefono
        self.driver.find_element(*self.input_phone).send_keys(number_phone)

    def get_phone_number(self):
        return self.driver.find_element(*self.button_phone_num).get_property('outerText')

    def click_phone_number_pop_up_window(self):
        #click en el boton para agregar el numero de telefono desde la ventana emergente
        self.driver.find_element(*self.button_phone_num_pop_up_window).click()

    def set_sms_code(self, code_sms):
        # Encuentra y envia los datos en el campo del numero del codigo sms
        self.driver.find_element(*self.sms_code_field).send_keys(code_sms)

    def click_next_code_phone(self):
        #click para cerrar la ventana emergente del numero de telefono
        self.driver.find_element(*self.button_next_phone_code).click()

    def click_payment_method(self):
        #click para el boton de metodo de pago de home page
        self.driver.find_element(*self.button_payment_method).click()

    def click_add_card(self):
        #click para el boton de añadir una tarjeta
        self.driver.find_element(*self.button_add_card).click()

    def set_card_number(self, number_card):
        # Encuentra y envia los datos en el campo del numero de tarjeta
        self.driver.find_element(*self.card_num_field).send_keys(number_card)

    def set_code_number(self, code_card):
        # Encuentra el campo del código de la tarjeta y envía el código
        code_field = self.driver.find_element(*self.card_code_num_field)
        code_field.send_keys(code_card)
        # Envía la tecla TAB para cambiar el enfoque
        code_field.send_keys(Keys.TAB)

    def get_card_number(self):
        return self.driver.find_element(*self.card_num_field).get_property('value')

    def get_code_number(self):
        return self.driver.find_element(*self.card_code_num_field).get_property('value')

    def click_add_card_2nd_pop_up_window(self):
        # click para el boton de añadir una tarjeta en la segunda ventana emergente
        self.driver.find_element(*self.button_agree_card).click()

    def check_agree_tcard(self):
        #chequea que el boton de confort se ha seleccionado
        elemento = self.driver.find_element(*self.check_agree_card)
        agree_tcard = elemento.is_displayed()
        return agree_tcard

    def click_close_pop_up_card_windows(self):
        #click para cerrar la ventana emergente del numero de telefono
        self.driver.find_element(*self.close_pop_up_card_windows).click()

    def set_message_for_driver(self, driver_message):
        # Encuentra y envia los datos en el campo de mensaje para el conductor
        self.driver.find_element(*self.message_for_driver_field).send_keys(driver_message)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.message_for_driver_field).get_property('value')

    def click_blanket_selector(self):
        # click para seleccionar manta y pañuelos
        self.driver.find_element(*self.blanket_selector).click()

    def get_blanket_value(self):
        return self.driver.find_element(*self.blanket_value).get_property('value')

    def click_ice_cream_plus(self):
        # click para agregar helados
        self.driver.find_element(*self.ice_cream2_plus).click()

    def get_ice_cream_value(self):
        return self.driver.find_element(*self.ice2_cream_count).get_property('outerText')

    def click_find_taxi(self):
        # click para pedir un taxi
        self.driver.find_element(*self.button_find_taxi).click()

    def check_botton_find_taxi(self):
        #chequea que el boton de buscar taxi aparezca
        elemento = self.driver.find_element(*self.button_find_taxi)
        botton_find_taxi = elemento.is_displayed()
        return botton_find_taxi

    def check_taxi_driver_selected(self):
        #chequea que el boton de confort se ha seleccionado
        elemento = self.driver.find_element(*self.taxi_driver_selected)
        taxi_driver_selected = elemento.is_displayed()
        return taxi_driver_selected

    def check_order_header_title(self):
        #chequea que el boton de confort se ha seleccionado
        elemento = self.driver.find_element(*self.order_header_title)
        order_header_title_show = elemento.is_displayed()
        return order_header_title_show
