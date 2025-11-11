# 🌎 Gestión de Datos de Países en Python  
**Trabajo Práctico Integrador — Programación 1 (UTN, 2° Cuatrimestre 2025)**  

---

## 🧠 Objetivo  
Desarrollar una aplicación modular en **Python** que permita gestionar información de países (nombre, población, superficie y continente) aplicando **listas**, **diccionarios**, **funciones**, **archivos CSV** y **validaciones**, El sistema simula un proceso administrativo de gestión de datos de países, permitiendo altas, modificaciones, búsquedas y análisis estadísticos.

---

## 🧩 Estructura del Proyecto  
```bash
TP_Programacion_Paises/
├── data/
│   └── paises.csv
├── docs/
│   └── informe_teorico.pdf
├── src/
│   ├── datos.py
│   ├── validaciones.py
│   ├── ordenamiento.py
│   ├── estadisticas.py
│   ├── busquedas.py
│   ├── filtros.py
│   └── main.py
└── README.md
```

---

## 👥 Integrantes y Roles

| Integrante       | Comisión | Rama GitHub   | Rol principal                                                  |
| ---------------- | -------- | ------------- | -------------------------------------------------------------- |
| **Casto Gil**    | 5        | `rama-casto`  | Gestión de datos, validaciones, ordenamientos y menú principal |
| **Alejo Almada** | 1        | `rama-alejo` | Búsquedas, filtros y estadísticas                              |

---

## 📊 Distribución de Responsabilidades

| Categoría de la rúbrica                             | Casto Gil (Com. 5)         | Alejo Almada (Com. 1)                               |
| --------------------------------------------------- | -------------------------- | --------------------------------------------------- |
| **Gestión de datos (alta, modificación, guardado)** | `datos.py`                 | —                                                   |
| **Lectura CSV y validaciones**                      | `validaciones.py`          | Validaciones en `busquedas.py` / `filtros.py`       |
| **Ordenamientos manuales**                          | `ordenamiento.py`          | —                                                   |
| **Estadísticas (promedios, min, max, conteo)**      | —                          | `estadisticas.py`                                   |
| **Búsquedas (exacta/parcial)**                      | —                          | `busquedas.py`                                      |
| **Filtros (continente, población, superficie)**     | —                          | `filtros.py`                                        |
| **Menú e integración general**                      | `main.py` (Casto)          | `estadisticas.py` (consultas y reportes)            |
| **Persistencia (guardar CSV)**                      | `datos.py`                 | —                                                   |
| **Pruebas y presentación**                          | Pruebas de integración y validación de flujo completo del sistema.                       |
| **Trabajo en equipo / documentación**               | Coordinación Git / README  | Ejemplos y documentación interna                    |

---

## 🧭 Flujo del Programa (Menú Principal)

```
========================================
     GESTIÓN DE PAÍSES EN PYTHON
========================================
1. Agregar país              → datos.py (Casto)
2. Actualizar país           → datos.py (Casto)
3. Buscar país               → busquedas.py (Alejo)
4. Filtrar países            → filtros.py (Alejo)
5. Ordenar países            → ordenamiento.py (Casto)
6. Mostrar estadísticas      → estadisticas.py (Alejo)
7. Guardar cambios           → datos.py (Casto)
8. Salir                     → main.py (Casto)
----------------------------------------
Seleccione una opción:
```

---

## ⚙️ Ejecución del Programa

Desde la carpeta `src`:

```bash
python main.py
```

---

## 📊 Ejemplo de Salida

- Ejemplo de resultados obtenidos al ejecutar las funciones de estadísticas:
```
País con mayor población: China (1,411,778,724)
País con menor población: Uruguay (3,423,108)
Promedio de población: 394,357,149.00
Promedio de superficie: 4,632,298.00 km²

Cantidad de países por continente:
- América: 5
- Europa: 3
- Asia: 2

```

---

## 🧱 Metodología de Trabajo

- **Control de versiones:** Flujo colaborativo con **Git y GitHub**, mediante ramas paralelas y Pull Requests.  
- **Ramas de desarrollo:** `rama-casto` y `rama-alejo`.  
- **Validaciones bloqueantes:**  
  - Cada ingreso de dato se controla con bucles while que solicitan nuevamente hasta ser válido.
  - No se utilizan estructuras avanzadas como try/except.  
- **Estructuras de control:**  
  - Uso de while y if con contadores manuales.
  - Validación de opciones incorrectas del menú.  
- **Estructura modular:** Funciones pequeñas, reutilizables y documentadas.  
- **Validación de CSV:** Se omiten líneas con errores mostrando mensajes claros.  
- **Pruebas unitarias:** Cada módulo probado antes de fusionarse a `main`.  
- No se utilizaron librerías externas; únicamente módulos nativos de Python.

---

## 📂 Repositorio y Documentación

📁 **Repositorio GitHub:**  
🔗 [https://github.com/CastoGil/Tp_Programacion_Paises](https://github.com/CastoGil/Tp_Programacion_Paises)

📘 **Informe teórico:**  
`/docs/informe_teorico.pdf`

🌍 **Datos:**  
`/data/paises.csv`

---


### 🎥 Video Explicativo — TPI Programación 1 (UTN 2025)
[![Ver Video en YouTube](https://img.youtube.com/vi/yu6_il5qRdo/0.jpg)](https://www.youtube.com/watch?v=yu6_il5qRdo)

> 📹 **Duración:** 13:15 minutos  
> 👥 **Integrantes:** Casto Gil (Comisión 5) — Alejo Almada (Comisión 1)  
> 🎯 En este video se explica el funcionamiento completo del sistema de gestión de países desarrollado en Python, mostrando las validaciones, filtros, ordenamientos y estadísticas, junto al flujo modular del código en Visual Studio Code.

---

## 🏫 Cátedra

**Tecnicatura Universitaria en Programación — UTN**  
Materia: **Programación 1**  
Tutores: *Martín García* y *Matías Torres*  
Comisiones: **1 y 5 — 2° Cuatrimestre 2025**
