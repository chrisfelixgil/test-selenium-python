import os
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ReportUtils:
    """Clase utilitaria para manejar reportes y capturas de pantalla"""
    
    def __init__(self, driver):
        self.driver = driver
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.report_dir = os.path.join(self.base_dir, f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
        self.screenshots_dir = os.path.join(self.report_dir, "screenshots")
        os.makedirs(self.screenshots_dir, exist_ok=True)
    
    def take_screenshot(self, test_name):
        """Toma una captura de pantalla y la guarda en el directorio correspondiente"""
        screenshot_dir = os.path.join(self.screenshots_dir, test_name)
        os.makedirs(screenshot_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(screenshot_dir, f"{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)
        return screenshot_path
    
    def get_test_status(self, test_name):
        """Obtiene el estado de la prueba actual"""
        return pytest.mark.status(test_name)
    
    def generate_html_report(self):
        """Genera un reporte HTML detallado"""
        report_path = os.path.join(self.report_dir, "report.html")
        pytest.main([
            "--html", report_path,
            "--self-contained-html",
            "--capture", "tee-sys",
            "--show-capture", "all"
        ])
        return report_path 