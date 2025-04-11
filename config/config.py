import os
from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Cargar variables de entorno
load_dotenv()

class Config:
    # Variables de entorno
    USERNAME = os.getenv('SAUCE_DEMO_USERNAME')
    PASSWORD = os.getenv('SAUCE_DEMO_PASSWORD')
    
    # Configuración del navegador
    HEADLESS = False
    IMPLICIT_WAIT = 10
    
    # Configuración de reportes
    REPORT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'reports')
    SCREENSHOT_DIR = os.path.join(REPORT_DIR, f'report_{datetime.now().strftime("%Y%m%d_%H%M%S")}')
    
    @staticmethod
    def get_driver():
        """Configura y retorna una instancia del WebDriver de Edge"""
        options = Options()
        if Config.HEADLESS:
            options.add_argument('--headless')
        
        service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)
        driver.maximize_window()
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        return driver
    
    @staticmethod
    def setup_report_dirs():
        """Crea los directorios necesarios para los reportes y capturas de pantalla"""
        os.makedirs(Config.REPORT_DIR, exist_ok=True)
        os.makedirs(Config.SCREENSHOT_DIR, exist_ok=True) 