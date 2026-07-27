# 📊 Dashboard de Análisis y Visualización de Finanzas

> **Un enfoque data-driven para la gestión del flujo de caja familiar:** Consolidación de transacciones multicanal, modelado multidimensional y visualización ejecutiva en Power BI para la optimización del ahorro y control del gasto.

[![Power BI](https://img.shields.io/badge/Power_BI-F2C94C?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Excel](https://img.shields.io/badge/Excel-1D6F42?style=for-the-badge&logo=microsoft-excel&logoColor=white)](https://www.microsoft.com/excel)
[![Status](https://img.shields.io/badge/Estado-Concluido-brightgreen?style=for-the-badge)]()

---

## 📌 Navegación Rápida
[← Volver al Portafolio Principal](https://camiloalarcon25.github.io/Mi_Portafolio_v1/)

- [Vista General del Dashboard](#-vista-general-del-dashboard)
- [El Desafío de Negocio](#-el-desafío-de-negocio)
- [Arquitectura de Datos y Metodología](#-arquitectura-de-datos-y-metodología)
- [Insights y Hallazgos Clave](#-insights-y-hallazgos-clave)
- [Vistas Detalladas](#-vistas-detalladas-del-dashboard)
- [Recomendaciones y Plan de Acción](#-recomendaciones-de-gestión-financiera)
- [Recursos del Repositorio](#-recursos-del-repositorio)

---

## 📸 Vista General del Dashboard

> *El cuadro de mando permite evaluar de un vistazo el balance neto, la estructura de egresos por categoría y la liquidez histórica del hogar.*

![Dashboard Principal de Finanzas Personales](https://raw.githubusercontent.com/CamiloAlarcon25/Finanzas/main/assets/dashboard_overview.png)
*(Reemplaza la URL de arriba por la captura de pantalla de la vista principal de tu dashboard)*

---

## 🎯 El Desafío de Negocio

El control financiero familiar suele verse afectado por la dispersión de transacciones en múltiples billeteras físicas y digitales, dificultando la visibilidad del flujo de caja real. 

El objetivo de este proyecto fue **sistematizar el registro y análisis financiero de un hogar**, estructurando fuentes heterogéneas para responder a preguntas críticas de gestión:
1. **¿Cuál es la tasa real de gasto sobre el ingreso acumulado?**
2. **¿Qué categorías de egreso comprometen la capacidad de ahorro mensual?**
3. **¿Cómo varían los saldos según la estacionalidad del año?**

---

## 🛠️ Arquitectura de Datos y Metodología

El proyecto implementa un pipeline ETL (Extracción, Transformación y Carga) estructurado en tres etapas:

```text
[ Archivos Excel Mensuales ] ──( Python Script )──> [ Dataset Consolidado ] ──( Power Query & DAX )──> [ Dashboard Power BI ]

# Generate Markdown and an HTML preview or script if needed
# We will construct a beautifully structured Markdown file and convert it into a crisp PDF reference if needed,
# or simply output the rich Markdown content.
# The user wants a clean, executive-level README.md file structure with image placeholders.

markdown_content = """# 📊 Dashboard de Análisis y Visualización de Finanzas Personales

> **Un enfoque data-driven para la gestión del flujo de caja familiar:** Consolidación de transacciones multicanal, modelado multidimensional y visualización ejecutiva en Power BI para la optimización del ahorro y control del gasto.

[![Power BI](https://img.shields.io/badge/Power_BI-F2C94C?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Excel](https://img.shields.io/badge/Excel-1D6F42?style=for-the-badge&logo=microsoft-excel&logoColor=white)](https://www.microsoft.com/excel)
[![Status](https://img.shields.io/badge/Estado-Concluido-brightgreen?style=for-the-badge)]()

---

## 📌 Navegación Rápida
[← Volver al Portafolio Principal](https://camiloalarcon25.github.io/Mi_Portafolio_v1/)

- [Vista General del Dashboard](#-vista-general-del-dashboard)
- [El Desafío de Negocio](#-el-desafío-de-negocio)
- [Arquitectura de Datos y Metodología](#-arquitectura-de-datos-y-metodología)
- [Insights y Hallazgos Clave](#-insights-y-hallazgos-clave)
- [Recomendaciones y Plan de Acción](#-recomendaciones-y-plan-de-acción)
- [Recursos del Repositorio](#-recursos-del-repositorio)

---

## 📸 Vista General del Dashboard

> *El cuadro de mando permite evaluar de un vistazo el balance neto, la estructura de egresos por categoría y la liquidez histórica del hogar.*

![Dashboard Principal de Finanzas Personales](https://raw.githubusercontent.com/CamiloAlarcon25/Finanzas/main/assets/dashboard_overview.png)
*Nota: Reemplaza este enlace por la captura de pantalla de la vista principal de tu dashboard en Power BI.*

---

## 🎯 El Desafío de Negocio

El control financiero familiar suele verse afectado por la dispersión de transacciones en múltiples billeteras físicas y digitales, dificultando la visibilidad del flujo de caja real. 

El objetivo de este proyecto fue **sistematizar el registro y análisis financiero de un hogar**, estructurando fuentes heterogéneas para responder a preguntas críticas de gestión:
1. **¿Cuál es la tasa real de gasto sobre el ingreso acumulado?**
2. **¿Qué categorías de egreso comprometen la capacidad de ahorro mensual?**
3. **¿Cómo varían los saldos según la estacionalidad del año?**

---

## 🛠️ Arquitectura de Datos y Metodología

El proyecto implementa un pipeline ETL (Extracción, Transformación y Carga) estructurado en tres etapas:
