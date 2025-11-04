# 🌎 Gestión de Datos de Países en Python  
**Trabajo Práctico Integrador — Programación 1 (UTN, 2° Cuatrimestre 2025)**  

---

## 🧠 Objetivo
Desarrollar una aplicación modular en **Python** que permita gestionar información de países (nombre, población, superficie y continente) aplicando listas, diccionarios, funciones, archivos CSV y validaciones, según los contenidos de la materia **Programación 1**.

---


## 🧩 Estructura del Proyecto

TP_Programacion_Paises/
├── data/
│ └── paises.csv
├── docs/
│ └── informe_teorico.pdf
├── src/
│ ├── init.py
│ ├── datos.py
│ ├── validaciones.py
│ ├── ordenamiento.py
│ ├── estadisticas.py
│ ├── busquedas.py
│ ├── filtros.py
│ ├── reportes.py
│ └── main.py
└── README.md
---


---

## 👥 Integrantes y Ramas

| Integrante | Comisión | Rama | Rol principal |
|-------------|-----------|--------|----------------|
| **Casto Gil** | 5 | `rama-casto` | Gestión de datos, validaciones, ordenamientos y menú principal |
| **Alejo Almada** | 1 | `rama-almada` | Búsquedas, filtros, estadísticas y submenú de reportes |

---

## 🧩 División del trabajo (según rúbrica oficial UTN)

| Categoría de la rúbrica                             | Casto Gil (Comisión 5)    | Alejo Almada (Comisión 1)                                |
| --------------------------------------------------- | ------------------------- | -------------------------------------------------------- |
| **Gestión de datos (alta, modificación, guardado)** | `datos.py`                | —                                                        |
| **Lectura CSV y validaciones**                      | `validaciones.py`         | Verificación de entrada en `busquedas.py` / `filtros.py` |
| **Ordenamientos manuales**                          | `ordenamiento.py`         | —                                                        |
| **Estadísticas (promedios, min, max, conteo)**      | —                         | `estadisticas.py`                                        |
| **Búsquedas (exacta/parcial)**                      | —                         | `busquedas.py`                                           |
| **Filtros (continente, población, superficie)**     | —                         | `filtros.py`                                             |
| **Menú e integración**                              | `main.py` (Casto)         | `reportes.py` (submenú de reportes y estadísticas)       |
| **Persistencia (guardar CSV)**                      | `datos.py`                | —                                                        |
| **Pruebas y presentación**                          | Testear flujo completo    | Testear filtros/búsquedas                                |
| **Trabajo en equipo / documentación**               | Coordinación Git / README | Documentación interna y ejemplos                         |

---

## 🧭 Flujo del Programa (Menú principal)

========================================
GESTIÓN DE PAÍSES EN PYTHON

Agregar país → datos.py (Casto)

Actualizar país → datos.py (Casto)

Buscar país → busquedas.py (Alejo)

Filtrar países → filtros.py (Alejo)

Ordenar países → ordenamiento.py (Casto)

Mostrar estadísticas → reportes.py + estadisticas.py (Alejo)

Guardar cambios → datos.py (Casto)

Salir → main.py (Casto)

## 🧮 Ejemplo de Ejecución

---

## ⚙️ Ejecución

Desde la carpeta `src`:

```bash
python main.py
O desde la raíz del proyecto:
python -m src.main

========================================
     GESTIÓN DE PAÍSES EN PYTHON
========================================
1. Agregar país
2. Actualizar país
3. Buscar país
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
7. Guardar cambios
8. Salir
----------------------------------------
Seleccione una opción:
🌍 País con mayor población: China (1,411,778,724)
🏳️ País con menor población: Uruguay (3,423,108)
📊 Promedio de población: 394,357,149
📐 Promedio de superficie: 4,632,298 km²
Cantidad de países por continente:
 - América: 5
 - Europa: 3
 - Asia: 2


📘 Metodología de Trabajo

Control de versiones con Git y GitHub (flujo por ramas).

Ramas de desarrollo: rama-casto y rama-almada.

Validaciones manuales sin try/except, de acuerdo al nivel de la materia.

Estructura modular: funciones pequeñas, reutilizables y documentadas.

CSV validado: se omiten líneas con errores y se muestra un mensaje claro.

Pruebas individuales antes de fusionar cada módulo a main.

Cumple con los criterios de modularización, legibilidad y validación de datos definidos en la rúbrica de corrección UTN.

📂 Repositorio y Documentación

Repositorio GitHub: https://github.com/CastoGil/Tp_Programacion_Paises

Informe teórico: /docs/informe_teorico.pdf

Datos: /data/paises.csv

🎥 Video de Exposición

Duración estimada: 10 – 15 minutos

Introducción y objetivos — ambos integrantes

Gestión de datos, validaciones y ordenamientos — Casto Gil

Búsquedas, filtros y reportes/estadísticas — Alejo Almada

Conclusiones y reflexión final — ambos

## 📄 Créditos y Cátedra
Proyecto académico presentado en la **Tecnicatura Universitaria en Programación — UTN**  
Materia: **Programación 1**  
Tutores: **Martin Garcia y Matias Torres**  
Comisiones: 1 y 5 — 2° Cuatrimestre 2025
