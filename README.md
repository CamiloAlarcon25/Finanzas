

### 1. Ingesta y Consolidación (Python)

* **Origen:** Reportes mensuales independientes en Excel (`YYYY-MM.xlsx`) con estructura de transacciones (`Tarea`, `Tipo`, `Valor`, `Estado`, `Mes`, `Billetera`).
* **Procesamiento:** Script en Python para la ingesta, validación de esquemas y concatenación automatizada en un dataset general.

### 2. Modelado y Transformación (Power Query & DAX)

* **Power Query:** Depuración de registros nulos, estandarización de tipos de datos de moneda y normalización de nomenclaturas.
* **Modelo Dimensional:** Construcción de una tabla de dimensión temporal (`Dim_Calendario`) en DAX para análisis dinámico por año, mes y día.
* **Métricas DAX Calculadas:**
  * **Ingresos Totales:** SUM() de flujos principales y secundarios.
  * **Gastos Totales:** SUM() por categorías (*Gasto Único, Gasto Extra, Otros, etc.*).
  * **Balance Neto:** `[Ingresos Totales] - [Gastos Totales]`.
  * **% Gasto / Ingreso:** `DIVIDE([Gastos Totales], [Ingresos Totales], 0)`.

### 3. Categorización del Gasto e Instrumentos de Pago

* **Ingresos:** Principal vs. Secundario.
* **Gastos:**
  * `Gasto Único`: Costos fijos estructurales (Colegiaturas, aranceles, servicios básicos).
  * `Gasto Extra`: Ocio, recreación e imprevistos.
  * `Otros`: Consumo diario, mercadería, combustible y pasajes.
* **Billeteras / Canales:** Billeteras digitales (`B01`, `B02`, `B03`, `B04`) y Efectivo (`EFE`).

---

## 📈 Insights y Hallazgos Clave

| Métrica Clave | Valor Registrado | Evaluación / Status |
| :--- | :--- | :--- |
| **Ingresos Totales** | `$16.841.350` | Flujo positivo y constante |
| **Balance General Acumulado** | `$1.374.170` | Superávit positivo al cierre del período |
| **Ratio Gasto / Ingreso** | `91,84%` | ⚠️ **Zona de Alerta** (Margen de maniobra ajustado) |
| **Mes de Mayor Ahorro** | Diciembre (`+$1.356.500`) | Impacto por ingresos estacionales/secundarios |
| **Mes de Mayor Déficit** | Octubre (`-$424.645`) | Pico atípico de egresos fijos/extraordinarios |

### 💡 Principales Conclusiones

* **Relación Ingreso/Gasto Ajustada:** A pesar de registrar un balance superavitario de `$1.374.170`, destinar el **91,84%** de los ingresos a egresos deja un colchón financiero reducido ante contingencias.
* **Concentración del Egreso:** Las categorías `Gasto Único` y `Gasto Extra` representan la mayor proporción del presupuesto, siendo `Gasto Extra` la variable con mayor potencial de optimización a corto plazo.

---

## 🖼️ Vistas Detalladas del Dashboard

<table width="100%">
  <tr>
    <td width="50%" align="center">
      <b>Análisis de Gastos por Categoría y Canal</b><br><br>
      <img src="https://raw.githubusercontent.com/CamiloAlarcon25/Finanzas/main/assets/categoria_gastos.png" alt="Categorías de Gastos" width="100%"/>
    </td>
    <td width="50%" align="center">
      <b>Evolución Temporal e Histórico Mensual</b><br><br>
      <img src="https://raw.githubusercontent.com/CamiloAlarcon25/Finanzas/main/assets/tendencia_mensual.png" alt="Tendencia Mensual" width="100%"/>
    </td>
  </tr>
</table>

---

## 💡 Recomendaciones de Gestión Financiera

1. **Ajuste en la Categoría "Gasto Extra":** Establecer un techo presupuestario mensual para reducir la tasa global de egreso del **91,84% al 80%**, destinando la diferencia a un fondo de reserva.
2. **Estrategia de Amortiguación Temporal:** Planificar el déficit recurrente observado en meses de alta carga (como octubre) mediante el traspaso de excedentes generados en meses de mayor ahorro (como diciembre).
3. **Monitoreo por Billetera:** Optimizar el uso de los instrumentos de pago (`B01`-`B04`) centralizando egresos para facilitar la conciliación bancaria automatizada.

---

## 📂 Recursos del Repositorio

* 📄 **Reporte Completo en PDF:** [Descargar pbix_final_Finanzas.pdf](https://github.com/CamiloAlarcon25/Finanzas/blob/main/pbix_final_Finanzas.pdf)
* 🐍 **Script de Consolidación:** Código en Python para la unión automática de fuentes Excel.
* 📊 **Modelo Power BI:** Archivo `.pbix` con medidas DAX y transformaciones en Power Query.
