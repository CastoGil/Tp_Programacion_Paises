# 🌎 Gestión de Datos de Países en Python  
**Trabajo Práctico Integrador — Programación 1 (UTN, 2° Cuatrimestre 2025)**  

---

## 🧠 Objetivo  
Desarrollar una aplicación modular en **Python** que permita gestionar información de países (nombre, población, superficie y continente) aplicando **listas**, **diccionarios**, **funciones**, **archivos CSV** y **validaciones**, según los contenidos de la materia **Programación 1**.

---

## 🧩 Estructura del Proyecto  
```bash
TP_Programacion_Paises/
├── data/
│   └── paises.csv
├── docs/
│   └── informe_teorico.pdf
├── src/
│   ├── __init__.py
│   ├── datos.py
│   ├── validaciones.py
│   ├── ordenamiento.py
│   ├── estadisticas.py
│   ├── busquedas.py
│   ├── filtros.py
│   ├── reportes.py
│   └── main.py
└── README.md
```



| Integrante       | Comisión | Rama GitHub   | Rol principal                                                  |
| ---------------- | -------- | ------------- | -------------------------------------------------------------- |
| **Casto Gil**    | 5        | `rama-casto`  | Gestión de datos, validaciones, ordenamientos y menú principal |
| **Alejo Almada** | 1        | `rama-almada` | Búsquedas, filtros, estadísticas y submenú de reportes         |

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
| **Menú e integración general**                      | `main.py` (Casto)          | `reportes.py` (submenú de estadísticas/reportes)    |
| **Persistencia (guardar CSV)**                      | `datos.py`                 | —                                                   |
| **Pruebas y presentación**                          | Testeo de flujo completo   | Testeo de búsquedas y filtros                       |
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
6. Mostrar estadísticas      → reportes.py + estadisticas.py (Alejo)
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

O desde la raíz del proyecto:

```bash
python -m src.main
```

---

## 📊 Ejemplo de Salida

```
🌍 País con mayor población: China (1,411,778,724)
🏳️ País con menor población: Uruguay (3,423,108)
📊 Promedio de población: 394,357,149
📐 Promedio de superficie: 4,632,298 km²

Cantidad de países por continente:
 - América: 5
 - Europa: 3
 - Asia: 2
```

---

## 🧱 Metodología de Trabajo

- **Control de versiones:** Flujo colaborativo con **Git y GitHub**, mediante ramas paralelas y Pull Requests.  
- **Ramas de desarrollo:** `rama-casto` y `rama-almada`.  
- **Validaciones:** Sin uso de `try/except`, solo estructuras vistas en la cursada.  
- **Estructura modular:** Funciones pequeñas, reutilizables y documentadas.  
- **Validación de CSV:** Se omiten líneas con errores mostrando mensajes claros.  
- **Pruebas unitarias:** Cada módulo probado antes de fusionarse a `main`.  
- **Cumplimiento académico:** Alineado con la rúbrica UTN (modularización, validación, legibilidad).

---

## 📂 Repositorio y Documentación

📁 **Repositorio GitHub:**  
🔗 [https://github.com/CastoGil/Tp_Programacion_Paises](https://github.com/CastoGil/Tp_Programacion_Paises)

📘 **Informe teórico:**  
`/docs/informe_teorico.pdf`

🌍 **Datos:**  
`/data/paises.csv`

---

## 🎥 Video de Exposición

**Duración estimada:** 10 – 15 minutos  
**Estructura sugerida:**

1. 🎬 Introducción y objetivos — *ambos integrantes*  
2. 🧱 Gestión de datos, validaciones y ordenamientos — *Casto Gil*  
3. 🔎 Búsquedas, filtros y reportes/estadísticas — *Alejo Almada*  
4. 🧭 Conclusiones y reflexión final — *ambos integrantes*

---

## 🏫 Cátedra

**Tecnicatura Universitaria en Programación — UTN**  
Materia: **Programación 1**  
Tutores: *Martín García* y *Matías Torres*  
Comisiones: **1 y 5 — 2° Cuatrimestre 2025**
