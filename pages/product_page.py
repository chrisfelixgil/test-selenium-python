from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    """Clase para manejar la página de productos de SauceDemo"""
    
    # Locators
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    def add_items_to_cart(self):
        """Añade todos los productos disponibles al carrito"""
        buttons = self.wait.until(EC.presence_of_all_elements_located(self.ADD_TO_CART_BUTTONS))
        for button in buttons:
            button.click()
    
    def go_to_cart(self):
        """Navega al carrito de compras"""
        self.wait.until(EC.element_to_be_clickable(self.CART_BUTTON)).click()
    
    def remove_backpack(self):
        """Elimina la mochila del carrito"""
        self.wait.until(EC.element_to_be_clickable(self.REMOVE_BACKPACK_BUTTON)).click()
    
    def proceed_to_checkout(self):
        """Procede al checkout"""
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()
    
    def fill_checkout_form(self, first_name, last_name, postal_code):
        """Completa el formulario de checkout"""
        self.wait.until(EC.presence_of_element_located(self.FIRST_NAME_INPUT)).send_keys(first_name)
        self.wait.until(EC.presence_of_element_located(self.LAST_NAME_INPUT)).send_keys(last_name)
        self.wait.until(EC.presence_of_element_located(self.POSTAL_CODE_INPUT)).send_keys(postal_code)
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()
    
    def finish_checkout(self):
        """Finaliza el proceso de checkout"""
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()
    
    def go_back_home(self):
        """Vuelve a la página principal"""
        self.wait.until(EC.element_to_be_clickable(self.BACK_HOME_BUTTON)).click()
    
    def open_menu(self):
        """Abre el menú lateral"""
        self.wait.until(EC.element_to_be_clickable(self.MENU_BUTTON)).click()
    
    def logout(self):
        """Cierra la sesión"""
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON)).click() 