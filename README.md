# 💰 Calculadora de Presupuesto

> Aplicación de gestión de presupuesto personal desarrollada en Python, siguiendo los principios de TDD y SOLID.

## 📋 Descripción del Proyecto

Aplicación de línea de comandos (CLI) para registrar ingresos y gastos personales con persistencia de datos.

**Estado:** 🚧 En desarrollo  
**Fase actual:** Implementación (TDD)

## 🎯 Objetivos de Aprendizaje

- Desarrollo guiado por pruebas (*TDD*)
- Arquitectura limpia (*3 capas*)
- Principios *SOLID*
- Prácticas profesionales de Python (type hints, docstrings)
- Herramientas de calidad de código (pytest, black, flake8, mypy)

## 🏗️ Arquitectura

┌─────────────────────┐
│   Presentacion      │  CLI Interfaz
│      (cli.py)       │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│  Logica de Negocio  │  Transaction, Budget
│     (models/)       │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│    Persistencia     │  Almacenamiento JSON 
│     (storage/)      │
└─────────────────────┘


## ✨ Funcionalidades

### Fase 1 (MVP)
- ✅ Historias de usuario definidas  
- ✅ Arquitectura diseñada  
- 🚧 Modelo de transacción (en progreso)  
- ⏳ Gestión de presupuesto  
- ⏳ Persistencia en JSON  
- ⏳ Interfaz CLI  

### Fase 2 (Futuro)
- ⏳ Exportación de datos (CSV, PDF)  
- ⏳ Reportes mensuales  
- ⏳ Alertas de presupuesto  

## 🛠️ Tecnologías

- **Lenguaje:** Python 3.12+  
- **Pruebas:** pytest  
- **Calidad de código:** black, flake8, mypy, isort  
- **Almacenamiento:** JSON  

## 📦 Instalación
bash
# Clonar el repositorio
git clone https://github.com/Josdasim/budget-calculator.git
cd budget-calculator

# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt


## 🧪 Ejecutar Tests
bash
pytest tests/ -v --cov=src


## 📚 Documentacion

- [Historias de Usuario](docs/user_stories.md)
- [Diseño de Architectura](docs/architecture.md)

---

**Parte de:** Python Junior Developer Learning Path  
**Projecto:** #1