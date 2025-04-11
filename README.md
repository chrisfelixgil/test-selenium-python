# 🧪 Pruebas Automatizadas con Selenium y Python

## 👨‍💻 Información Personal

¡Hola! Soy Christian Gil 👋

📌 Matrícula: 2012-1036  
📚 Materia: Programación 3  
👨‍🏫 Profesor: Kelyn Tejada Belliard  
🏫 Institución: ITLA

## 📋 Descripción del Proyecto

Este proyecto implementa pruebas automatizadas para la aplicación SauceDemo utilizando:
- 🐍 Python como lenguaje de programación
- 🔍 Selenium WebDriver para la automatización de pruebas web
- 🧪 Pytest como framework de pruebas
- 📊 Generación de reportes HTML

## 🛠️ Tecnologías Utilizadas

- Python 3.x
- Selenium WebDriver
- Pytest
- Pytest-HTML
- Edge WebDriver

## 📦 Estructura del Proyecto

```
test-selenium-python/
├── pages/              # Objetos de página
├── tests/              # Casos de prueba
├── reports/            # Reportes generados
├── .env               # Variables de entorno
└── requirements.txt    # Dependencias
```

## 🔐 Configuración del Entorno

Antes de ejecutar las pruebas, es necesario crear un archivo `.env` en la raíz del proyecto.

```env
SAUCE_DEMO_USERNAME=user
SAUCE_DEMO_PASSWORD=password
```

## 🚀 Cómo Ejecutar las Pruebas

1. Crear y activar el entorno virtual:
```bash
python -m venv venv
.\venv\Scripts\activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Crear el archivo `.env` con las credenciales (ver sección de configuración)

4. Ejecutar las pruebas:
```bash
python -m pytest tests/test_saucedemo.py -v --html=reports/report.html --self-contained-html
```

## 📊 Reportes

Los reportes se generan en la carpeta `reports/` con el siguiente formato:
- `report_YYYYMMDD_HHMMSS.html`: Reporte HTML con los resultados de las pruebas

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, asegúrate de:
1. Crear una rama para tu característica
2. Hacer commit de tus cambios
3. Enviar un pull request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. 