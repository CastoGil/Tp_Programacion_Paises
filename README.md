# 🌎 Gestión de Datos de Países en Python  
**Trabajo Práctico Integrador — Programación 1 (UTN, 2° Cuatrimestre 2025)**  

---

## 🧠 Objetivo
Desarrollar una aplicación modular en **Python** que permita gestionar información de países (nombre, población, superficie y continente) aplicando las estructuras básicas vistas en clase: listas, diccionarios, funciones, archivos y validaciones.

---

## 🧩 Estructura del Proyecto

TP_Programacion_Paises/
├── data/
│ └── paises.csv
├── docs/
│ └── informe_teorico.pdf
├── src/
│ ├── main.py
│ ├── datos.py
│ ├── estadisticas.py
│ ├── ordenamiento.py
│ ├── validaciones.py
│ ├── busquedas.py
│ └── filtros.py
└── README.md

---

## 👥 Integrantes y Roles

| Rol | Integrante | Comisión | Rama | Módulos |
|------|-------------|-----------|--------|----------|
| **A** | **Casto Gil** | **5** | `rama-casto` | `datos.py`, `estadisticas.py`, `ordenamiento.py`, `validaciones.py` |
| **B** | **Alejo Almada** | **1** | `rama-alejo` | `busquedas.py`, `filtros.py`, `main.py` (menú) |
---

## ⚙️ Funcionalidades

### ✅ Integrante A — Casto Gil
- Lectura, agregado y actualización de países (`datos.py`)
- Estadísticas globales (máx/min, promedios, conteos) (`estadisticas.py`)
- Ordenamientos manuales (nombre, población, superficie) (`ordenamiento.py`)
- Validaciones genéricas (`validaciones.py`)

### 🔜 Integrante B — Alejo Almada
- Búsquedas exactas y parciales (`busquedas.py`)
- Filtros por continente, rango de población o superficie (`filtros.py`)
- Menú principal de integración (`main.py`)

---

## 🧮 Ejemplo de Ejecución

```bash
cd src
python main.py

Salida esperada:
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
---

## 📘 Metodología de Trabajo
- Control de versiones con **Git y GitHub**.  
- División de tareas por ramas (`rama-casto`, `rama-alejo`).  
- Validaciones manuales sin `try/except`, acorde al nivel de Programación 1.  
- Pruebas individuales antes de fusión a `main`.

---

📂 Repositorio y Documentación:
🔗 Repositorio GitHub: https://github.com/CastoGil/TP_Programacion_Paises
📄 Informe teórico: /docs/informe_teorico.pdf
📁 Datos: /data/paises.csv

---

🎥 Video de Exposición

Duración: 10 – 15 minutos
1. Introducción y objetivos — ambos integrantes
2. Módulos de datos, estadísticas y ordenamiento — Casto
3. Búsquedas, filtros y menú — Alejo
4. Conclusiones y reflexión final — ambos
---

## 📄 Créditos y Cátedra
Proyecto académico presentado en la **Tecnicatura Universitaria en Programación — UTN**  
Materia: **Programación 1**  
Tutores: **Martin Garcia y Matias Torres**  
Comisiones: 1 y 5 — 2° Cuatrimestre 2025
