import pytest
import pytest_html
from datetime import datetime
import os
import time

def pytest_configure(config):
    """Configuración inicial de pytest"""
    # Crear directorio de reportes si no existe
    if not os.path.exists("reports"):
        os.makedirs("reports")
    
    # Configurar el reporte HTML
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    config.option.htmlpath = os.path.join("reports", f"report_{timestamp}.html")

def pytest_html_report_title(report):
    """Configurar el título del reporte"""
    report.title = "Reporte de Pruebas SauceDemo"

def pytest_html_results_table_header(cells):
    """Configurar las cabeceras de la tabla de resultados"""
    cells.insert(1, "Test")
    cells.insert(2, "Duration")

def pytest_html_results_table_row(report, cells):
    """Configurar las filas de la tabla de resultados"""
    # Agregar nombre del test
    test_name = report.nodeid.split("::")[-1]
    cells.insert(1, test_name)
    
    # Agregar duración
    duration = report.duration
    cells.insert(2, f"{duration:.2f}s")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook para agregar información al reporte"""
    outcome = yield
    report = outcome.get_result()
    
    # Agregar información adicional
    report.extra = []
    if report.when == "call":
        # Agregar descripción del test
        report.description = str(item.function.__doc__)
        
        # Agregar información del navegador
        report.extra.append(pytest_html.extras.text("Browser: Edge"))
        
        # Agregar información del entorno
        report.extra.append(pytest_html.extras.text("Environment: Test"))
        
        # Agregar mensaje de error si el test falló
        if report.outcome == "failed":
            report.extra.append(pytest_html.extras.text(f"Error: {str(report.longrepr)}")) 