import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.report_utils import ReportUtils
import os
from datetime import datetime

class TestSauceDemo:
    # Variable de clase para almacenar el directorio de reporte
    report_dir = None
    
    @pytest.fixture(autouse=True)
    def setup(self, request):
        """Configuración inicial para cada prueba"""
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.login_page = LoginPage(self.driver)
        self.product_page = ProductPage(self.driver)
        
        # Crear directorio de reporte solo si no existe
        if TestSauceDemo.report_dir is None:
            TestSauceDemo.report_dir = os.path.join("reports", f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
            os.makedirs(TestSauceDemo.report_dir, exist_ok=True)
        
        # Agregar información al reporte
        request.node.user_properties.append(("Browser", "Edge"))
        request.node.user_properties.append(("Environment", "Test"))
        
        yield
        self.driver.quit()
    
    def take_screenshot(self, test_name):
        """Toma una captura de pantalla y la guarda en el directorio del reporte"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(TestSauceDemo.report_dir, f"{test_name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)
        return screenshot_path
    
    def test_invalid_username(self):
        """Prueba de inicio de sesión con nombre de usuario inválido"""
        self.login_page.load()
        self.take_screenshot("test_invalid_username_initial")
        self.login_page.login("usuario_invalido", "secret_sauce")
        self.take_screenshot("test_invalid_username_after_login")
        error_message = self.login_page.get_error_message()
        assert "Username and password do not match" in error_message
    
    def test_invalid_password(self):
        """Prueba de inicio de sesión con contraseña inválida"""
        self.login_page.load()
        self.take_screenshot("test_invalid_password_initial")
        self.login_page.login("standard_user", "contraseña_invalida")
        self.take_screenshot("test_invalid_password_after_login")
        error_message = self.login_page.get_error_message()
        assert "Username and password do not match" in error_message
    
    def test_empty_credentials(self):
        """Prueba de inicio de sesión con credenciales vacías"""
        self.login_page.load()
        self.take_screenshot("test_empty_credentials_initial")
        self.login_page.login("", "")
        self.take_screenshot("test_empty_credentials_after_login")
        error_message = self.login_page.get_error_message()
        assert "Username is required" in error_message
    
    def test_complete_purchase_flow(self):
        """Prueba completa del flujo de compra, incluyendo inicio de sesión, 
        agregar productos al carrito, checkout y cierre de sesión"""
        # Inicio de sesión exitoso
        self.login_page.load()
        self.take_screenshot("test_complete_purchase_flow_initial")
        self.login_page.login("standard_user", "secret_sauce")
        self.take_screenshot("test_complete_purchase_flow_after_login")
        
        # Añadir productos al carrito
        self.product_page.add_items_to_cart()
        self.take_screenshot("test_complete_purchase_flow_after_adding_items")
        
        # Ir al carrito
        self.product_page.go_to_cart()
        self.take_screenshot("test_complete_purchase_flow_cart")
        
        # Eliminar un artículo
        self.product_page.remove_backpack()
        self.take_screenshot("test_complete_purchase_flow_after_removing_item")
        
        # Proceder al checkout
        self.product_page.proceed_to_checkout()
        self.take_screenshot("test_complete_purchase_flow_checkout")
        
        # Completar el formulario
        self.product_page.fill_checkout_form(
            first_name="Juan Pablo",
            last_name="Duarte",
            postal_code="809829849"
        )
        self.take_screenshot("test_complete_purchase_flow_after_filling_form")
        
        # Finalizar el checkout
        self.product_page.finish_checkout()
        self.take_screenshot("test_complete_purchase_flow_after_finish")
        
        # Volver a la página principal
        self.product_page.go_back_home()
        
        # Abrir el menú
        self.product_page.open_menu()
        
        # Cerrar sesión
        self.product_page.logout()
        self.take_screenshot("test_complete_purchase_flow_logout")

    def pytest_terminal_summary(self, terminalreporter, exitstatus, config):
        """Genera el reporte HTML al finalizar las pruebas"""
        self.report_utils.generate_html_report()