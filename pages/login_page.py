from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """Clase para manejar la página de inicio de sesión de SauceDemo"""
    
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    def load(self):
        """Carga la página de inicio de sesión"""
        self.driver.get("https://www.saucedemo.com/")
    
    def login(self, username, password):
        """Realiza el inicio de sesión con las credenciales proporcionadas"""
        self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT)).send_keys(username)
        self.wait.until(EC.presence_of_element_located(self.PASSWORD_INPUT)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
    
    def get_error_message(self):
        """Obtiene el mensaje de error si existe"""
        try:
            return self.wait.until(EC.presence_of_element_located(self.ERROR_MESSAGE)).text
        except:
            return "" 