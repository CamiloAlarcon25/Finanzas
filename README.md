# Finanzas

## Análisis y Visualización de Finanzas Personales

### 1. Resumen y Objetivos
Este proyecto se centra en ordenar y analizar la situación financiera del hogar, evaluando en detalle los flujos de ingresos y gastos. El objetivo principal es identificar las categorías de mayor egreso y proponer estrategias para amortiguar o solucionar dichos gastos sin comprometer la dinámica familiar.
El análisis se estructura en dos tipos de ingresos (Principal y Secundario), y seis categorías principales de gastos:
#### •	Gasto Único: Pagos relacionados con gastos fijos (colegiaturas, aranceles, servicios).
#### •	Gasto Extra: Pagos vinculados al ocio y la recreación familiar.
#### •	Otros: Mercadería, Bencina, Pasajes y diversas categorías menores.
Además, se identifica el instrumento de pago utilizado para cada transacción (billeteras B01-B02-B03-B04 o efectivo EFE).

### 2. Tecnologías y Herramientas
Herramienta	Función Principal
#### Excel	Almacenamiento inicial de los registros de transacciones.
#### Python	Consolidación y unión de múltiples archivos de datos.
#### Power BI	Modelado, limpieza (Power Query), cálculo (DAX) y visualización (Dashboard).

### 3. Desarrollo y Metodología de Datos
El proyecto inicia con la ingesta de datos provenientes de registros de pagos con tarjetas y efectivo. Inicialmente, cada mes está contenido en un archivo Excel separado (ej. 2025-04.xlsx), con seis columnas clave: Tarea (Descripción), Tipo (Categoría), Valor ($), Estado, Mes y Billetera.

#### A. Consolidación (Python)
Antes de la visualización, se utiliza un script de Python para automatizar la unión de todos los archivos mensuales en una única tabla de salida (dataset general).

#### B. Transformación y Modelado (Power BI)
La tabla general se importa a Power BI y se somete a un proceso de limpieza en Power Query, que incluye:
##### •	Depuración de registros en blanco o detalles irrelevantes.
##### •	Ajuste y validación del tipo de dato de las columnas.
##### •	Cambio de nombres de categorías para facilitar la interpretación en la visualización.
Posteriormente, se crea una tabla calendario utilizando código DAX para permitir filtros temporales (año, mes, día) y un análisis de tendencias más robusto.

### 4. Resultados y Análisis Clave
El dashboard desarrollado en Power BI facilita la identificación inmediata de patrones financieros:
#### •	Identificación de Egresos: Se pueden observar las dos categorías que generan el mayor gasto desde abril de 2025 hasta la fecha (ej. "Gasto Extra" y "Gasto Único").
#### •	Balance General: El balance total acumulado a la fecha es positivo ($1.374.170), con ingresos totales de $16.841.350.
#### •	Relación Gasto/Ingreso: A pesar del balance positivo, el Porcentaje Gasto sobre Ingreso es del 91,84%, un valor considerado alto que indica una relación muy ajustada entre los egresos y los ingresos.
#### •	Tendencia Mensual: Se identifica el mes con mayor poder de ahorro (ej. diciembre, con $1.356.500) y el mes con mayor déficit (ej. octubre, con un balance negativo de $-424.645).


